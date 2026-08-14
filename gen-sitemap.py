#!/usr/bin/env python3
"""Generate sitemap.xml for videotvai.com"""
import glob, os
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))

urls = []
for f in sorted(glob.glob(f'{BASE}/**/*.html', recursive=True)):
    if '404' in f or 'baidu_verify' in f or 'blog-old' in f or 'admin' in f:
        continue
    # .html 为 canonical：保留 .html 后缀（仅 index.html 归一为 /）
    path = f.replace(BASE, '').replace('/index.html', '/')
    if path == '/index':
        path = '/'
    urls.append(f'https://www.videotvai.com{path}')

today = date.today().isoformat()
xml = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    xml.append(f'  <url><loc>{u}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>')
xml.append('</urlset>')

spath = os.path.join(BASE, 'sitemap.xml')
with open(spath, 'w') as f:
    f.write('\n'.join(xml))
print(f'videotvai.com sitemap: {len(urls)} URLs')
