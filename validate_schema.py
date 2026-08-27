#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schema 一致性校验 hook（防回归）
扫描站点全部 HTML 的 JSON-LD：
  1) 语法可解析（致命错误 → exit 1）
  2) Article/WebPage headline 与 <title> 一致性（偏离过大 → 警告）
  3) 错套主题 boilerplate（如医疗 headline 出现在非医疗页 → 致命错误）
用法：python3 validate_schema.py [站点根目录]   （默认当前目录）
"""
import os, re, sys, json, glob

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
WRONG_BOILERPLATE = "医疗学术会议直播平台_私域电商直播系统 | 直达播"

json_err = 0
hard_topic = 0
soft_mismatch = 0
pages = 0

for fp in sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)):
    pages += 1
    h = open(fp, encoding="utf-8", errors="ignore").read()
    rel = os.path.relpath(fp, ROOT)
    # 1) JSON-LD 语法
    for i, b in enumerate(re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)):
        try:
            json.loads(b)
        except Exception as e:
            json_err += 1
            print(f"[JSON错误] {rel} block#{i}: {e}")
    # 2) 错套主题 boilerplate
    if WRONG_BOILERPLATE in h:
        hard_topic += 1
        print(f"[错主题] {rel}: 仍含医疗 boilerplate headline")
    # 3) headline vs title 一致性
    tm = re.search(r"<title>(.*?)</title>", h, re.S)
    hm = re.search(r'"headline":"([^"]*)"', h)
    if tm and hm:
        t = re.split(r"\s*[\|\｜]\s*", tm.group(1))[0].strip()
        hl = re.split(r"\s*[\|\｜]\s*", hm.group(1))[0].strip()
        if t and hl and t != hl:
            # 容差：互相包含或前 8 字相同视为可接受（Schema 关键词更丰满属良性）
            if not (t in hl or hl in t or t[:8] == hl[:8]):
                soft_mismatch += 1
                print(f"[headline≠title] {rel}: title='{t[:30]}' headline='{hl[:30]}'")

print(f"\n扫描页面={pages} | JSON语法错误={json_err} | 错主题={hard_topic} | headline偏离(警告)={soft_mismatch}")
if json_err > 0 or hard_topic > 0:
    print("❌ 存在致命问题，阻止部署")
    sys.exit(1)
print("✅ 校验通过（headline 偏离为良性，可部署）")
sys.exit(0)
