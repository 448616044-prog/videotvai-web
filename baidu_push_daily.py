#!/usr/bin/env python3
"""videotvai.com 百度每日推送 — 推送10条最新URL；over quota 时减半降级重试"""
import requests, os, glob
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
TOKEN = 'UAVg0xt7rxpTjzaL'  # videotvai.com Baidu token (2026-07-27 更新)
API = f'http://data.zz.baidu.com/urls?site=www.videotvai.com&token={TOKEN}'

PUSHED = os.path.join(BASE, 'baidu_pushed.txt')


def collect_urls():
    """收集全部 HTML URL（递归），排除无需推送的页面"""
    urls = []
    for f in glob.glob(f'{BASE}/**/*.html', recursive=True):
        if '404' in f or 'baidu_verify' in f or 'blog-old' in f or 'admin' in f:
            continue
        path = f.replace(BASE, '').replace('/index.html', '/')
        if path == '/index':
            path = '/'
        urls.append(f'https://www.videotvai.com{path}')
    return urls


def push(urls):
    """推 URL，over quota 时减半降级重试，返回成功条数"""
    batch = urls[:]
    while batch:
        resp = requests.post(API, data='\n'.join(batch), headers={'Content-Type': 'text/plain'}, timeout=15)
        try:
            data = resp.json()
        except Exception:
            print(f'  响应异常: {resp.text[:200]}')
            return 0
        msg = str(data.get('message', '')).lower()
        if data.get('error') == 400 and 'over quota' in msg:
            if len(batch) == 1:
                print('  配额已耗尽(over quota)，今日结束')
                return 0
            batch = batch[:len(batch) // 2]
            print(f'  over quota，降级重试 {len(batch)} 条')
            continue
        success = data.get('success', 0)
        remain = data.get('remain', '?')
        print(f'  成功 {success}/{len(batch)}, 剩余配额 {remain}')
        return success
    return 0


def main():
    urls = collect_urls()

    pushed_set = set()
    if os.path.exists(PUSHED):
        with open(PUSHED) as f:
            pushed_set = set(line.strip() for line in f if line.strip())

    new_urls = [u for u in urls if u not in pushed_set]
    priority = sorted(new_urls, key=lambda u: 0 if '/live-surgery-' in u or '/case-' in u or 'calculator' in u else 1)

    to_push = priority[:10]
    if not to_push:
        print(f'{date.today()} videotvai Baidu Push: 无新URL')
        return

    print(f'{date.today()} videotvai Baidu Push: 待推送 {len(to_push)} 条')
    success = push(to_push)
    if success > 0:
        with open(PUSHED, 'a') as f:
            for u in to_push[:success]:
                f.write(u + '\n')
        print(f'  已标记 {success} 条到 baidu_pushed.txt')


if __name__ == '__main__':
    main()
