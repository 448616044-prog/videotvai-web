#!/usr/bin/env python3
"""
百度主动推送脚本（urllib版）
用法: python3 baidu_push.py
由 WorkBuddy 生成, 2026-06-21
"""
import urllib.request, urllib.error, json, os, glob

SITE = "https://www.videotvai.com"
BAIDU_TOKEN = "UAVg0xt7rxpTjzaL"  # 2026-07-27 阿龙更新
API_URL = f"http://data.zz.baidu.com/urls?site={SITE}&token={BAIDU_TOKEN}"
BATCH_SIZE = 10

def get_local_urls():
    urls = set()
    html_dir = os.path.dirname(os.path.abspath(__file__))
    skip = {"baidu_verify_codeva-4mRLvHLcFK.html", "admin.html"}
    # 根目录HTML
    for f in glob.glob(os.path.join(html_dir, "*.html")):
        fname = os.path.basename(f)
        if fname in skip:
            continue
        if fname == "index.html":
            urls.add(f"https://{SITE}/")
        else:
            urls.add(f"https://{SITE}/{fname}")
    # blog目录HTML
    blog_dir = os.path.join(html_dir, "blog")
    if os.path.exists(blog_dir):
        for f in glob.glob(os.path.join(blog_dir, "*.html")):
            fname = os.path.basename(f)
            urls.add(f"https://{SITE}/blog/{fname}")
    return sorted(urls)

def push(urls):
    total_success = 0
    for i in range(0, len(urls), BATCH_SIZE):
        batch = urls[i:i+BATCH_SIZE]
        data = "\n".join(batch).encode('utf-8')
        req = urllib.request.Request(API_URL, data=data, method='POST')
        req.add_header('Content-Type', 'text/plain')
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read().decode())
            s = result.get('success', 0)
            r = result.get('remain', '?')
            total_success += s
            print(f"  批次 {i//BATCH_SIZE+1}: 成功 {s} 条, 剩余 {r} 次")
            if r == 0 or r == '0':
                print(f"  ⚠️ 配额已用完，剩余 {len(urls)-i-BATCH_SIZE} 条待明天推送")
                break
        except urllib.error.HTTPError as e:
            body = e.read().decode() if hasattr(e, 'read') else str(e)
            error_info = json.loads(body) if body.startswith('{') else body
            print(f"  批次 {i//BATCH_SIZE+1}: ❌ {e.code} - {error_info}")
            if e.code == 400 and 'over quota' in str(body).lower():
                print(f"  ⚠️ 配额已用完，剩余 {len(urls)-i-BATCH_SIZE} 条待明天推送")
                break
        except Exception as e:
            print(f"  批次 {i//BATCH_SIZE+1}: ❌ {e}")
    return total_success

def main():
    urls = get_local_urls()
    print(f"📋 百度主动推送 - {SITE}")
    print(f"   待推送: {len(urls)} 个URL (每批{BATCH_SIZE}条)")
    total = push(urls)
    print(f"\n✅ 本次推送成功: {total} 条 (共 {len(urls)} 条)")

if __name__ == "__main__":
    main()
