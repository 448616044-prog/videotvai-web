#!/usr/bin/env python3
"""
百度主动推送脚本
用法: python3 baidu_push.py

依赖: 标准库 (urllib.request, subprocess) + curl
"""
import subprocess, json, os, glob

SITE = "www.videotvai.com"
BAIDU_TOKEN = "K4kVPs6NwjtWr4ij"
API_URL = f"http://data.zz.baidu.com/urls?site=https://{SITE}&token={BAIDU_TOKEN}"

def get_local_urls():
    urls = set()
    html_dir = os.path.dirname(os.path.abspath(__file__))
    skip = {"baidu_verify_codeva-4mRLvHLcFK.html", "admin.html"}
    for f in glob.glob(os.path.join(html_dir, "*.html")):
        fname = os.path.basename(f)
        if fname in skip:
            continue
        if fname == "index.html":
            urls.add(f"https://{SITE}/")
        else:
            urls.add(f"https://{SITE}/{fname}")
    return sorted(urls)

def push(urls):
    data = "\n".join(urls)
    cmd = [
        "curl", "-s", "-X", "POST",
        API_URL,
        "-H", "Content-Type: text/plain",
        "-d", data
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        resp = json.loads(result.stdout)
        print(f"✅ 推送成功: {resp.get('success',0)} 条, 剩余: {resp.get('remain','?')} 次")
        if resp.get("not_same_site"):
            print(f"   非本站: {resp['not_same_site']}")
        if resp.get("not_valid"):
            print(f"   无效URL: {resp['not_valid']}")
    except:
        print(f"❌ 响应: {result.stdout[:200]}")

def main():
    urls = get_local_urls()
    print(f"📋 百度主动推送 - {SITE}")
    print(f"   待推送: {len(urls)} 个URL")
    for u in urls:
        print(f"   - {u}")
    print()
    push(urls)

if __name__ == "__main__":
    main()
