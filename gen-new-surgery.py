#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 4 个新手术科室直播方案页：皮肤科/康复/内分泌/呼吸科"""
import importlib.util, os
spec = importlib.util.spec_from_file_location("gs", "gen-surgery-pages.py")
gs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gs)
gen_page = gs.gen_page

NEW = [
    ("dermatology", "皮肤科", "皮肤外科/激光美容/毛发移植手术"),
    ("rehabilitation", "康复医学科", "运动康复/术后康复/康复评定示教"),
    ("endocrinology", "内分泌科", "甲状腺手术/糖尿病足/代谢手术"),
    ("pulmonology", "呼吸科", "支气管镜/肺结节/胸腔镜手术"),
]

for key, name, desc in NEW:
    fname, html = gen_page(key, name, desc)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {fname} 已写盘")
