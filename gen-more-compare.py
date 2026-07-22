#!/usr/bin/env python3
"""Generate more competitor comparison pages for videotvai.com"""

import os

TODAY = "2026-07-23"
BASE = "https://www.videotvai.com"
D = os.path.dirname(os.path.abspath(__file__))

MORE = [
    {
        "slug": "huode-vs-zhidabo",
        "title": "获得场景视频替代方案 | 直达播vs获得场景视频2026对比",
        "h1": "获得场景视频替代方案：直达播vs获得场景视频 企业直播平台对比",
        "meta": "获得场景视频是教育/培训直播老牌，但医疗场景是短板。直达播vs获得场景视频：医疗合规、手术直播、私有化部署全维度对比。免费获取对比方案→",
        "kw": "获得场景视频替代,获得场景视频对比,获得vs直达播,教育直播平台对比,企业直播选型",
        "competitor": "获得场景视频",
        "cd": "国内教育/企业培训直播平台，在教育行业有深厚积累。但医疗直播合规（等保三级）和手术示教场景方面较为薄弱，仅提供SaaS服务，不支持私有化部署。",
        "za": "直达播在医疗直播合规、手术示教超低延迟、私有化部署方面具有获得场景视频不具备的优势。特别适合有医疗直播需求或需要私有化部署的企业。",
        "features": [
            ("医疗合规（等保三级）","❌ 不涉及","✅ 已通过","直达播"),
            ("手术示教（<1秒延迟）","❌ 不支持","✅ WebRTC <400ms","直达播"),
            ("私有化部署","❌ 仅SaaS","✅ 支持","直达播"),
            ("教育/培训直播","✅ 核心场景","✅ 支持","平手"),
            ("企业年会直播","✅ 成熟","✅ 支持","平手"),
            ("HCP身份验证","❌ 无","✅ 内置","直达播"),
            ("API开放","⚠️ 有限","✅ 全面","直达播"),
        ],
        "faq": [
            ("获得场景视频和直达播有什么区别？","获得场景视频擅长教育/培训场景，直达播专注医疗直播和私有化部署。如果你有医疗合规需求或需要私有化，直达播是更好的选择。"),
            ("获得场景视频能做医疗直播吗？","获得场景视频没有医疗合规认证（等保三级），也没有HCP验证功能。如果只是普通健康科普可以，但正式学术会议和手术示教建议用专业的医疗直播平台。"),
        ],
    },
    {
        "slug": "huantuo-vs-zhidabo",
        "title": "欢拓云直播替代方案 | 直达播vs欢拓云2026年对比",
        "h1": "欢拓云直播替代方案2026：直达播vs欢拓云 功能价格全对比",
        "meta": "欢拓云以电商直播为主，医疗和企业级功能有限。直达播vs欢拓云：医疗合规、超低延迟、私有化部署、API开放度全面对比。免费获取方案→",
        "kw": "欢拓云替代,欢拓云对比,欢拓vs直达播,电商直播平台对比,直播SaaS对比",
        "competitor": "欢拓云",
        "cd": "国内电商直播SaaS平台，以直播带货和营销直播为核心。医疗行业方案缺失，不支持私有化部署和等保合规。",
        "za": "直达播在医疗直播和企业级功能（私有化部署、等保合规、API开放）方面远超欢拓云。电商直播方面两者能力相当。",
        "features": [
            ("电商直播","✅ 核心场景","✅ 支持","平手"),
            ("医疗直播","❌ 不涉及","✅ 专长","直达播"),
            ("私有化部署","❌ 仅SaaS","✅ 支持","直达播"),
            ("等保三级","❌ 无","✅ 已通过","直达播"),
            ("手术示教","❌ 不支持","✅ WebRTC","直达播"),
            ("营销插件","✅ 丰富","⚠️ 有限","欢拓云"),
        ],
        "faq": [
            ("欢拓云和直达播怎么选？","做电商直播选欢拓云更成熟。如果涉及医疗直播或需要私有化部署，直达播是唯一选择。有些客户两个平台都用：欢拓做电商，直达播做医疗。"),
        ],
    },
    {
        "slug": "polyv-vs-zhidabo",
        "title": "保利威替代方案 | 直达播vs保利威 企业直播平台2026对比",
        "h1": "保利威替代方案2026：直达播vs保利威 教育/医疗/企业直播对比",
        "meta": "保利威是教育/企业直播老牌，但在医疗合规和手术直播方面有短板。直达播vs保利威：等保三级、HCP验证、超低延迟手术示教全维度对比→",
        "kw": "保利威替代,保利威对比,保利威vs直达播,企业直播平台,教育直播对比",
        "competitor": "保利威(Polyv)",
        "cd": "国内老牌企业直播平台，在教育/培训/金融行业有较大市场份额。技术实力强但医疗行业方案薄弱，不支持等保三级和HCP验证。",
        "za": "直达播在医疗直播合规（等保三级+HCP）和手术示教超低延迟方面具有保利威不具备的专业能力。企业培训场景两者均可。",
        "features": [
            ("教育/培训直播","✅ 核心","✅ 支持","平手"),
            ("医疗合规（等保三级）","❌ 无","✅ 已通过","直达播"),
            ("手术示教","❌ 不支持","✅ WebRTC","直达播"),
            ("私有化部署","✅ 支持","✅ 支持","平手"),
            ("AI功能","✅ 丰富","⚠️ 有限","保利威"),
            ("HCP验证","❌ 无","✅ 内置","直达播"),
        ],
        "faq": [
            ("保利威和直达播怎么选？","保利威在教育/企业培训方面更成熟，AI功能更丰富。但有医疗直播或手术示教需求的，直达播的医疗合规方案是保利威不具备的。"),
            ("从保利威切换到直达播麻烦吗？","不麻烦。直达播提供迁移支持：直播流程对接、API切换、数据导入。一般1-2周完成。如果涉及保利威的AI功能需要另行评估替代方案。"),
        ],
    },
    {
        "slug": "263-vs-zhidabo",
        "title": "263直播替代方案 | 直达播vs263企业直播2026对比",
        "h1": "263直播替代方案2026：直达播vs263 企业通信与直播对比",
        "meta": "263以企业邮箱/会议为主，直播是其附属产品。直达播vs263：医疗专业度、手术示教能力、直播延迟、品牌定制全维度对比。专业直播方案→",
        "kw": "263直播替代,263对比,263vs直达播,企业直播平台选型,263替代方案",
        "competitor": "263企业直播",
        "cd": "263以企业邮箱和视频会议为主业，直播是附加服务。功能偏基础，适合企业内部简单直播，不适合专业医疗直播和手术示教场景。",
        "za": "作为专注医疗直播的专业平台，直达播在医疗合规、超低延迟、品牌定制方面全面领先263的通用直播方案。",
        "features": [
            ("直播专业度","⚠️ 附加功能","✅ 核心业务","直达播"),
            ("医疗合规","❌ 不涉及","✅ 等保三级","直达播"),
            ("延迟","3-8秒 CDN","<1秒 WebRTC","直达播"),
            ("品牌定制","❌ 有限","✅ 深度定制","直达播"),
            ("企业邮箱/会议","✅ 核心业务","❌ 不涉及","263"),
            ("HCP验证","❌ 无","✅ 内置","直达播"),
        ],
        "faq": [
            ("263直播和直达播有什么区别？","263的主业是企业邮箱和会议，直播只是附属功能。直达播是专业医疗直播平台。如果你需要的是专业级直播（尤其医疗场景），直达播明显更优。日常简单内部直播263也能用。"),
        ],
    },
]


def gen(p):
    s = p["slug"]
    fname = p["slug"] + ".html"

    feats = ""
    for f in p["features"]:
        feats += f'<tr><td>{f[0]}</td><td>{f[1]}</td><td>{f[2]}</td><td style="text-align:center;font-size:12px;color:#666">{f[3]}</td></tr>\n'

    faq_json = ",".join([
        '{"@type":"Question","name":"'+q+'","acceptedAnswer":{"@type":"Answer","text":"'+a+'"}}'
        for q, a in p["faq"]
    ])

    html = f'''<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta name="baidu-site-verification" content="codeva-4mRLvHLcFK" />
<meta charset="UTF-8"><meta name="lastmod" content="{TODAY}">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="{p["meta"]}">
<meta name="keywords" content="{p["kw"]}">
<meta name="robots" content="index,follow">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["meta"]}">
<title>{p["title"]}</title>
<link rel="canonical" href="{BASE}/{s}">
<link rel="stylesheet" href="style.css">
<script async src="https://hm.baidu.com/hm.js?a77a0249f4adf3adcff923b5858c9cf0"></script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"{BASE}/"}},{{"@type":"ListItem","position":2,"name":"{p["h1"][:20]}","item":"{BASE}/{s}"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json}]}}</script>
<style>
body{{font-family:PingFang SC,Microsoft YaHei,sans-serif;color:#333;line-height:1.8;margin:0;background:#f5f7fa}}
.container{{max-width:900px;margin:0 auto;padding:0 20px}}
.navbar{{background:#fff;padding:16px 0;box-shadow:0 2px 8px rgba(0,0,0,.06);position:sticky;top:0;z-index:100}}
.navbar-content{{max-width:900px;margin:0 auto;padding:0 20px;display:flex;align-items:center;justify-content:space-between}}
.logo{{font-size:20px;font-weight:700;color:#1a1a2e;text-decoration:none}}
.nav-links a{{color:#555;text-decoration:none;margin-left:20px;font-size:14px}}
.hero{{background:linear-gradient(135deg,#1a1a2e,#2d2d44);color:#fff;padding:48px 0 32px;text-align:center}}
.hero h1{{font-size:26px;margin:0 12px;line-height:1.4}}
.content{{background:#fff;padding:32px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.08);margin:-20px auto 40px}}
h2{{color:#1a1a2e;font-size:22px;margin:32px 0 16px;border-bottom:2px solid #E8F2FF;padding-bottom:8px}}
table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}}
th{{background:#1a1a2e;color:#fff;padding:12px 16px;text-align:left}}
td{{padding:10px 16px;border-bottom:1px solid #E0E0E0}}
tr:nth-child(even){{background:#f8f9fa}}
.verdict{{background:#FFF3CD;padding:20px;border-radius:8px;border-left:4px solid #FFC107;margin:24px 0}}
.cta{{background:linear-gradient(135deg,#0066CC,#004C99);color:#fff;text-align:center;padding:40px;border-radius:12px;margin:32px 0}}
.cta a{{display:inline-block;background:#fff;color:#0066CC;padding:14px 32px;border-radius:6px;font-weight:700;text-decoration:none}}
footer{{background:#1a1a2e;color:rgba(255,255,255,.5);padding:40px 0;text-align:center;font-size:14px}}
footer a{{color:rgba(255,255,255,.5)}}
@media(max-width:768px){{.content{{padding:20px}}.hero h1{{font-size:20px}}}}
</style></head><body>
<header class="navbar"><div class="navbar-content">
<a href="index.html" class="logo">直达播</a>
<nav class="nav-links"><a href="index.html#solutions">解决方案</a><a href="live-medical.html">医疗直播</a><a href="live-surgery.html">手术示教</a><a href="xiaoe-vs-zhidabo">平台对比</a><a href="about.html">关于我们</a></nav>
</div></header>
<section class="hero"><div class="container">
<h1>{p["h1"]}</h1>
<p style="opacity:.85;font-size:16px;max-width:650px;margin:12px auto 0">2026年最新对比 · 基于真实功能评估</p>
</div></section>
<div class="container"><div class="content">
<div class="verdict"><strong>📌 30秒结论：</strong>{p["competitor"]}擅长{p["competitor"]}的传统领域，但在医疗直播合规和手术示教方面是空白。如果有医疗场景需求，直达播是更专业的选择。</div>
<h2>一、{p["competitor"]}简介</h2><p>{p["cd"]}</p>
<h2>二、直达播的优势</h2><p>{p["za"]}</p>
<h2>三、功能对比</h2>
<table><tr><th>维度</th><th>{p["competitor"]}</th><th>直达播</th><th>优势</th></tr>{feats}</table>
<div class="cta"><h2 style="color:#fff;margin:0 0 8px">正在对比{p["competitor"]}和直达播？</h2>
<p style="margin:0 0 20px">告知你的场景和需求，30分钟出专属对比方案</p>
<a href="tel:13026603164">📞 立即咨询</a></div>
</div></div>
<footer><div class="container"><p>© 2026 直达播 — 湖南复胜科技有限公司</p>
<p><a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener">湘ICP备2026016030号</a></p></div></footer>
</body></html>'''

    return fname, html


def main():
    for p in MORE:
        fname, html = gen(p)
        with open(os.path.join(D, fname), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ {fname}")
    print(f"\n📊 {len(MORE)} 个竞品对比扩展页")


if __name__ == "__main__":
    main()
