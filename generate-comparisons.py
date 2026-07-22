#!/usr/bin/env python3
"""Generate competitor comparison pages for videotvai.com — 百度搜索截流"""

import os

TODAY = "2026-07-22"
BASE = "https://www.videotvai.com"

COMPARISONS = [
    {
        "slug": "xiaoe-vs-zhidabo",
        "title": "小鹅通替代方案2026 | 直达播vs小鹅通功能/价格/场景全对比",
        "h1": "小鹅通替代方案2026：直达播vs小鹅通 功能、价格、场景全面对比",
        "meta": "小鹅通2026年涨价后，越来越多企业寻找替代方案。直达播vs小鹅通全维度对比：直播功能、价格模式、医疗合规、私有化部署、售后服务。帮你选对平台→",
        "keywords": "小鹅通替代,小鹅通vs直达播,小鹅通涨价替代,小鹅通对比,企业直播平台对比,私域直播平台选型",
        "competitor": "小鹅通",
        "competitor_desc": "国内知名的知识付费和私域直播SaaS平台，覆盖知识店铺、直播、社群运营等功能。2026年调整价格策略后，部分企业开始寻找更具性价比的替代方案。",
        "zhidabo_advantage": "直达播在医疗直播合规、私有化部署、超低延迟方面具有小鹅通不具备的技术优势。特别适合医疗医药、大型企业等对数据安全和合规要求高的场景。",
        "features": [
            ("私有化部署", "❌ 仅SaaS", "✅ 支持私有化", "直达播"),
            ("医疗合规（等保三级）", "❌ 不支持", "✅ 等保三级", "直达播"),
            ("HCP身份验证", "❌ 无", "✅ 内置", "直达播"),
            ("手术示教（<1秒延迟）", "❌ 不支持", "✅ WebRTC", "直达播"),
            ("电商直播", "✅ 成熟", "✅ 成熟", "平手"),
            ("小程序直播", "✅ 微信生态", "✅ 支持", "平手"),
            ("内容付费/知识店铺", "✅ 核心功能", "⚠️ 非核心", "小鹅通"),
            ("API开放程度", "⚠️ 有限", "✅ 全面开放", "直达播"),
        ],
        "pricing_note": "小鹅通2026年起调整价格策略，基础版年费上涨30-50%。直达播按实际用量灵活计费，无强制年费，大客户可定制私有化方案。",
        "verdict": "如果你做知识付费/内容变现 → 小鹅通更合适。如果你需要医疗合规/私有化部署/超低延迟直播 → 直达播性价比更高。",
        "faq": [
            ("小鹅通涨价后有什么替代方案？", "如果你主要做直播（非知识付费），直达播是一个高性价比选择。直达播在医疗合规、私有化部署方面具有小鹅通不具备的优势，且无强制年费。"),
            ("从���鹅通迁移到直达播麻烦吗？", "不麻烦。直达播提供迁移技术支持，包括：直播流程对接、观众数据导入、API接口切换。一般1-2周完成完整迁移。"),
            ("直达播和小鹅通哪个便宜？", "看场景。小鹅通按年付费+功能叠加，年费从数千到数万不等。直达播按实际用量灵活计费，直播量不大的企业反而更省。大客户可定制私有化报价。"),
        ],
    },
    {
        "slug": "tencent-meeting-vs-zhidabo",
        "title": "腾讯会议能替代医疗直播平台吗 | 直达播vs腾讯会议2026对比",
        "h1": "医疗直播用腾讯会议够吗？直达播vs腾讯会议2026全维度对比",
        "meta": "很多医院用腾讯会议做学术直播，但它真的是最佳选择吗？直达播vs腾讯会议：医疗合规、延迟、录制、HCP管理、品牌定制、数据安全全对比。医疗直播专用方案→",
        "keywords": "腾讯会议医疗直播,腾讯会议vs直播平台,医疗学术直播平台对比,腾讯会议替代医疗,医学会议直播系统",
        "competitor": "腾讯会议",
        "competitor_desc": "腾讯旗下视频会议产品，疫情期间广泛用于医疗学术会议。但作为通用会议工具，在医疗合规、品牌展示、专业录制方面有天然局限。",
        "zhidabo_advantage": "直达播是专为医疗场景设计的直播平台，内置HCP身份验证、等保三级合规、品牌定制、专业录制回放等功能，比通用会议工具更适合医疗学术传播。",
        "features": [
            ("医疗合规（等保三级/HIPAA）", "❌ 通用工具", "✅ 医疗专用", "直达播"),
            ("HCP身份验证", "❌ 无", "✅ 内置", "直达播"),
            ("品牌定制（Logo/皮肤/域名）", "⚠️ 有限", "✅ 深度定制", "直达播"),
            ("手术直播（<1秒延迟）", "❌ 不支持", "✅ WebRTC", "直达播"),
            ("录制+回放管理", "⚠️ 基础", "✅ 专业CMS", "直达播"),
            ("观众互动（问答/投票/抽奖）", "⚠️ 基础", "✅ 丰富", "直达播"),
            ("观看数据统计", "⚠️ 基础", "✅ 详细分析", "直达播"),
            ("并发人数上限", "✅ 2000人", "✅ 10万+", "直达播"),
            ("免费使用", "✅ 基础版免费", "— 付费服务", "腾讯会议"),
        ],
        "pricing_note": "腾讯会议基础版免费（限100人/60分钟），商业版和企业版按账号收费。直达播按实际直播用量灵活计费，大客户可定制。医疗场景通常需要付费版本才能满足合规要求。",
        "verdict": "内部小范围会议 → 腾讯会议够用。对外学术会议/手术示教/品牌直播 → 直达播更专业合规。很多客户的做法是：日常沟通用腾讯会议，正式学术活动用直达播。",
        "faq": [
            ("腾讯会议做医疗直播有什么问题？", "三个核心问题：① 缺乏医疗合规认证（等保三级）② 无法验证参会医生身份（HCP）③ 品牌展示能力弱。对于正式学术会议和手术示教，这些问题可能影响合规和品牌形象。"),
            ("医疗学术直播用腾讯会议还是专业平台？", "取决于场景。内部科室讨论用腾讯会议足够。对外大型学术会议、手术直播、需要品牌展示和合规记录的场合，专业医疗直播平台（如直达播）更合适。"),
            ("用直达播做医疗直播，观众需要下载APP吗？", "不需要。直达播支持微信/浏览器直接观看，观众无需下载任何APP。这点和腾讯会议不同（腾讯会议要求下载客户端）。"),
        ],
    },
    {
        "slug": "weizan-vs-zhidabo",
        "title": "微赞替代方案2026 | 直达播vs微赞企业直播平台对比",
        "h1": "微赞替代方案2026：直达播vs微赞 企业直播功能/价格/技术对比",
        "meta": "微赞是国内企业直播老牌平台，但2026年技术架构和医疗合规方面有短板。直达播vs微赞全维度对比：直播延迟、医疗合规、定制能力、API开放度、价格模式→",
        "keywords": "微赞替代,微赞vs直达播,企业直播平台对比,微赞直播替代方案,企业直播选型,微赞对比",
        "competitor": "微赞",
        "competitor_desc": "国内老牌企业直播平台，覆盖企业培训、营销直播、年会直播等场景，以SaaS模式为主。2026年在技术架构和垂直行业方案（特别是医疗）方面相对薄弱。",
        "zhidabo_advantage": "直达播采用新一代WebRTC架构实现超低延迟，在医疗直播等垂直场景有深度定制能力。支持私有化部署，满足大型企业对数据安全的严格要求。",
        "features": [
            ("端到端延迟", "3-8秒（CDN）", "<1秒（WebRTC）", "直达播"),
            ("私有化部署", "❌ 仅SaaS", "✅ 支持", "直达播"),
            ("医疗合规（等保三级）", "❌ 无", "✅ 通过", "直达播"),
            ("API开放程度", "⚠️ 有限", "✅ 全面开放", "直达播"),
            ("企业培训", "✅ 成熟", "✅ 支持", "平手"),
            ("营销直播", "✅ 成熟", "✅ 支持", "平手"),
            ("年会直播", "✅ 成熟", "✅ 支持", "平手"),
            ("品牌定制", "⚠️ 有限", "✅ 深度定制", "直达播"),
        ],
        "pricing_note": "微赞按年付费模式，基础版数千元/年起。直达播按实际用量灵活计费，无强制年费。对于直播频次不高或需要私有化部署的企业，直达播可能更经济。",
        "verdict": "一般企业培训/营销直播 → 微赞够用。需要超低延迟/医疗合规/私有化部署/深度定制 → 直达播优势明显。",
        "faq": [
            ("微赞直播延迟高怎么办？", "微赞采用传统CDN直播架构，延迟通常3-8秒，不适合互动性强的场景。直达播使用WebRTC技术实现<1秒延迟，适合手术示教、互动培训等场景。"),
            ("微赞能私有化部署吗？", "微赞目前仅提供SaaS服务，不支持私有化部署。如果企业对数据安全有严格要求（如医院、药企、金融机构），直达播的私有化方案更合适。"),
            ("从微赞切换到直达播有什么好处？", "三大好处：① 延迟从3-8秒降到<1秒 ② 获得医疗合规认证 ③ 支持私有化部署。迁移过程直达播提供全程技术支持。"),
        ],
    },
    {
        "slug": "shengwang-vs-zhidabo",
        "title": "声网替代方案 | 直达播vs声网 实时音视频技术2026对比",
        "h1": "声网替代方案2026：直达播vs声网 实时音视频PaaS/SaaS对比",
        "meta": "声网是底层RTC PaaS，直达播是上层应用SaaS。直达播vs声网对比：开发成本、业务对接速度、医疗行业方案、运维成本。需要快速上线还是深度定制？选对方案→",
        "keywords": "声网替代,声网vs直达播,实时音视频平台对比,声网PaaS对比,RTC方案选型,直播技术选型",
        "competitor": "声网（Agora）",
        "competitor_desc": "全球领先的实时音视频PaaS平台，提供底层RTC SDK。适合有技术团队、需要深度定制的大型企业。但需要自行开发上层应用，开发周期长、成本高。",
        "zhidabo_advantage": "直达播是基于WebRTC/TRTC的完整SaaS解决方案，开箱即用。适合需要快速上线的企业，无需自建技术团队。同时提供API深度集成能力，兼顾灵活性和效率。",
        "features": [
            ("产品形态", "PaaS（需开发）", "SaaS（开箱即用）", "场景不同"),
            ("上线周期", "2-6个月", "1-3天", "直达播"),
            ("技术团队要求", "需要5+开发人员", "无需技术团队", "直达播"),
            ("定制灵活度", "✅ 极高", "✅ 高（API开放）", "声网"),
            ("医疗合规方案", "❌ 需自建", "✅ 内置", "直达播"),
            ("端到端延迟", "✅ <400ms", "✅ <1秒", "声网"),
            ("运维成本", "高（自运维）", "低（全托管）", "直达播"),
            ("SDK丰富度", "✅ 全平台", "✅ 主流平台", "声网"),
        ],
        "pricing_note": "声网按使用分钟数计费，价格透明但需考虑开发+运维成本。直达播为场景化打包定价，无需额外开发投入。对于大多数企业，直达播的总拥有成本更低。",
        "verdict": "有自建技术团队+需要极致定制 → 声网更合适。想要快速上线+医疗合规+零运维 → 直达播是更好的选择。两者也可以配合使用：声网做底层，直达播做应用层。",
        "faq": [
            ("声网和直达播有什么区别？", "声网是PaaS（平台即服务），提供底层音视频SDK，你需要自己开发应用。直达播是SaaS（软件即服务），提供完整的直播解决方案，开箱即用。简单说：声网是'零件'，直达播是'成品'。"),
            ("我们有技术团队，还用直达播吗？", "有技术团队不一定就要从零开发。直达播提供全面API，你的技术团队可以基于直达播进行二次开发和集成，既省去底层开发时间，又保留定制灵活性。"),
            ("声网做医疗直播需要什么额外工作？", "需要自行实现：HCP身份验证、等保合规、录制管理、内容审核、数据统计等。这些功能在直达播中已内置，单独开发至少需要2-3个月。"),
        ],
    },
]


def generate_comparison(c):
    s = c["slug"]
    fname = f"{s}.html"
    features_html = ""
    for f in c["features"]:
        features_html += f'<tr><td>{f[0]}</td><td>{f[1]}</td><td>{f[2]}</td><td style="text-align:center;font-size:12px;color:#666">{f[3]}</td></tr>\n'

    faq_html = ""
    for q, a in c["faq"]:
        faq_html += f'<div style="margin-bottom:16px"><strong style="color:#1a1a2e">❓ {q}</strong><p style="color:#555;margin-top:4px">{a}</p></div>\n'

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta name="baidu-site-verification" content="codeva-4mRLvHLcFK" />
  <meta charset="UTF-8">
  <meta name="lastmod" content="{TODAY}">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <meta name="description" content="{c["meta"]}">
  <meta name="keywords" content="{c["keywords"]}">
  <meta name="robots" content="index,follow">
  <meta property="og:title" content="{c["title"]}">
  <meta property="og:description" content="{c["meta"]}">
  <meta property="og:url" content="{BASE}/{s}">
  <meta property="og:type" content="article">
  <title>{c["title"]}</title>
  <link rel="canonical" href="{BASE}/{s}">
  <link rel="stylesheet" href="style.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"{BASE}/"}},{{"@type":"ListItem","position":2,"name":"{c["h1"].split("：")[0] if"："in c["h1"] else c["h1"][:20]}","item":"{BASE}/{s}"}}]}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ','.join(['{{"@type":"Question","name":"'+q+'","acceptedAnswer":{{"@type":"Answer","text":"'+a+'"}}}}' for q,a in c["faq"]]) + f']}}}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{c["h1"]}","description":"{c["meta"]}","author":{{"@type":"Organization","name":"直达播"}},"publisher":{{"@type":"Organization","name":"直达播","url":"{BASE}"}},"datePublished":"{TODAY}","dateModified":"{TODAY}"}}</script>
  <script async src="https://hm.baidu.com/hm.js?a77a0249f4adf3adcff923b5858c9cf0"></script>
<style>
body{{font-family:PingFang SC,Microsoft YaHei,sans-serif;color:#333;line-height:1.8;margin:0;background:#f5f7fa}}
.container{{max-width:900px;margin:0 auto;padding:0 20px}}
.navbar{{background:#fff;padding:16px 0;box-shadow:0 2px 8px rgba(0,0,0,.06);position:sticky;top:0;z-index:100}}
.navbar-content{{display:flex;align-items:center;justify-content:space-between}}
.logo{{font-size:20px;font-weight:700;color:#1a1a2e;text-decoration:none}}
.nav-links a{{color:#555;text-decoration:none;margin-left:24px;font-size:14px}}
.nav-links a:hover{{color:#0066CC}}
.hero{{background:linear-gradient(135deg,#1a1a2e,#2d2d44);color:#fff;padding:48px 0 32px;text-align:center}}
.hero h1{{font-size:28px;margin:0 0 12px;line-height:1.4}}
.content{{background:#fff;padding:32px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.08);margin:-20px auto 40px}}
h2{{color:#1a1a2e;font-size:22px;margin:32px 0 16px;border-bottom:2px solid #E8F2FF;padding-bottom:8px}}
table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}}
th{{background:#1a1a2e;color:#fff;padding:12px 16px;text-align:left}}
td{{padding:10px 16px;border-bottom:1px solid #E0E0E0}}
tr:nth-child(even){{background:#f8f9fa}}
.verdict{{background:#FFF3CD;padding:20px;border-radius:8px;border-left:4px solid #FFC107;margin:24px 0}}
.cta{{background:linear-gradient(135deg,#0066CC,#004C99);color:#fff;text-align:center;padding:40px 20px;border-radius:12px;margin:32px 0}}
.cta a{{display:inline-block;background:#fff;color:#0066CC;padding:14px 32px;border-radius:6px;font-weight:700;text-decoration:none;margin:8px}}
footer{{background:#1a1a2e;color:rgba(255,255,255,.5);padding:40px 0;text-align:center;font-size:14px}}
footer a{{color:rgba(255,255,255,.5)}}
@media(max-width:768px){{.content{{padding:20px}}.hero h1{{font-size:22px}}table{{font-size:12px}}}}
</style>
</head>
<body>
<header class="navbar"><div class="container navbar-content">
  <a href="index.html" class="logo">直达播</a>
  <nav class="nav-links">
    <a href="index.html#solutions">解决方案</a>
    <a href="live-medical.html">医疗直播</a>
    <a href="live-ecommerce.html">电商直播</a>
    <a href="about.html">关于我们</a>
  </nav>
</div></header>

<section class="hero"><div class="container">
  <h1>{c["h1"]}</h1>
  <p style="opacity:.9;font-size:16px;max-width:700px;margin:0 auto">2026年更新 | 基于真实功能对比，帮你选对直播平台</p>
</div></section>

<div class="container"><div class="content">

<div class="verdict">
  <strong>📌 30秒结论：</strong>{c["verdict"]}
</div>

<h2>一、{c["competitor"]}是什么？</h2>
<p>{c["competitor_desc"]}</p>

<h2>二、直达播的优势</h2>
<p>{c["zhidabo_advantage"]}</p>

<h2>三、功能详细对比</h2>
<table>
  <tr><th>对比维度</th><th>{c["competitor"]}</th><th>直达播</th><th>优势方</th></tr>
  {features_html}
</table>

<h2>四、价格模式对比</h2>
<p>{c["pricing_note"]}</p>

<h2>五、适用场景建议</h2>
<table>
  <tr><th>场景</th><th>推荐方案</th><th>原因</th></tr>'''

    if "小鹅通" in c["competitor"]:
        html += '''
  <tr><td>知识付费/内容变现</td><td>小鹅通</td><td>知识店铺是核心功能</td></tr>
  <tr><td>医疗学术会议直播</td><td>直达播</td><td>合规+低延迟+品牌定制</td></tr>
  <tr><td>私域电商直播</td><td>两者均可</td><td>功能相近，看价格偏好</td></tr>
  <tr><td>私有化部署</td><td>直达播</td><td>小鹅通仅SaaS</td></tr>'''
    elif "腾讯会议" in c["competitor"]:
        html += '''
  <tr><td>内部科室讨论</td><td>腾讯会议</td><td>免费/低成本，够用</td></tr>
  <tr><td>对外学术会议</td><td>直达播</td><td>品牌展示+合规+专业感</td></tr>
  <tr><td>手术示教直播</td><td>直达播</td><td>超低延迟+安全合规</td></tr>
  <tr><td>日常沟通协作</td><td>腾讯会议</td><td>通用工具更适合</td></tr>'''
    elif "微赞" in c["competitor"]:
        html += '''
  <tr><td>企业培训/年会</td><td>两者均可</td><td>功能相近</td></tr>
  <tr><td>医疗学术直播</td><td>直达播</td><td>合规+低延迟</td></tr>
  <tr><td>营销直播</td><td>两者均可</td><td>看定制需求</td></tr>
  <tr><td>私有化部署</td><td>直达播</td><td>微赞仅SaaS</td></tr>'''
    else:
        html += '''
  <tr><td>自建直播应用</td><td>声网</td><td>PaaS灵活度最高</td></tr>
  <tr><td>快速上线直播</td><td>直达播</td><td>SaaS开箱即用</td></tr>
  <tr><td>医疗合规场景</td><td>直达播</td><td>内置合规方案</td></tr>
  <tr><td>极致性能定制</td><td>声网</td><td>PaaS底���控制</td></tr>'''

    html += f'''
</table>

<h2>六、常见问题</h2>
{faq_html}

<div class="cta">
  <h2 style="color:#fff;margin:0 0 12px">正在对比{c["competitor"]}和直达播？</h2>
  <p style="margin:0 0 20px;font-size:16px">告诉我们你的场景和需求，30分钟出对比方案+专属报价</p>
  <a href="tel:13026603164">📞 立即咨询</a>
  <a href="index.html#contact" style="background:transparent;border:2px solid #fff;color:#fff">📋 在线提交需求</a>
  <p style="margin-top:16px;font-size:13px;opacity:.8">或访问 <a href="index.html" style="color:#fff">www.videotvai.com</a> 了解更多</p>
</div>

</div></div>

<footer><div class="container">
  <p>© 2026 直达播 — 湖南复胜科技有限公司</p>
  <p><a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener">湘ICP备2026016030号</a></p>
</div></footer>
</body></html>'''

    return fname, html


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    for c in COMPARISONS:
        fname, html = generate_comparison(c)
        path = os.path.join(out_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ {fname}")

    print(f"\n📊 {len(COMPARISONS)} 个竞品对比页已生成")
    print(f"📂 {out_dir}")


if __name__ == "__main__":
    main()
