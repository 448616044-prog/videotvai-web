#!/usr/bin/env python3
"""videotvai.com 百度每日推送 — 推送10条最新URL"""
import requests, os, glob
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
TOKEN = '2zqNR8QtonmBaAF4'  # videotvai.com Baidu token
API = f'http://data.zz.baidu.com/urls?site=www.videotvai.com&token={TOKEN}'

PUSHED = os.path.join(BASE, 'baidu_pushed.txt')

# Collect all HTML URLs
urls = []
for f in glob.glob(f'{BASE}/**/*.html', recursive=True):
    if '404' in f or 'baidu_verify' in f: continue
    path = f.replace(BASE, '').replace('/index.html', '/').replace('.html', '')
    if path == '/index': path = '/'
    urls.append(f'https://www.videotvai.com{path}')

# Load pushed history
pushed_set = set()
if os.path.exists(PUSHED):
    with open(PUSHED) as f:
        pushed_set = set(line.strip() for line in f if line.strip())

# Prioritize: new pages first
new_urls = [u for u in urls if u not in pushed_set]
priority = sorted(new_urls, key=lambda u: 0 if '/live-surgery-' in u or '/case-' in u or 'calculator' in u else 1)

to_push = priority[:10]
if not to_push:
    print(f'{date.today()} videotvai Baidu Push: 无新URL')
    exit(0)

resp = requests.post(API, data='\n'.join(to_push), headers={'Content-Type': 'text/plain'}, timeout=15)
print(f'{date.today()} videotvai Baidu Push: {resp.text}')

try:
    data = resp.json()
    success = data.get('success', 0)
    if success > 0:
        with open(PUSHED, 'a') as f:
            for u in to_push[:success]:
                f.write(u + '\n')
    print(f'  成功: {success}/{len(to_push)}, 剩余配额: {data.get("remain", "?")}')
except:
    print(f'  响应: {resp.text[:200]}')
