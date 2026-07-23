#!/usr/bin/env python3
"""Generate videotvai.com customer case studies + xiaoe-tech migration guide"""
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))

CASES = [
    {
        'slug': 'case-cardiology-3a-hospital',
        'title': '三甲医院心内科手术直播案例 | 年直播200+台手术示教 - 直达播',
        'h1': '某三甲医院心内科：年直播200+台手术，覆盖全国30+医联体单位',
        'industry': '三甲医院 · 心内科',
        'scale': '年直播200+台手术，覆盖30+医联体单位',
        'pain': '原有方案延迟3-5秒，远程专家无法实时指导。画面模糊看不清导丝操作。',
        'solution': '部署直达播私有化方案：WebRTC超低延迟(200ms) + 4K多画面 + 院内服务器，数据不出院。',
        'result': '延迟降到200ms，专家可实时指导。年手术直播量从80台提升到200+台。医联体覆盖扩至30+单位。',
        'keywords': '心内科手术直播案例,三甲医院手术示教,医疗直播成功案例',
    },
    {
        'slug': 'case-pharma-academic-conference',
        'title': '医药企业学术会议直播案例 | 年200场合规直播 - 直达播',
        'h1': '某跨国药企：年办200场学术会议直播，RDPAC合规零风险',
        'industry': '跨国药企 · 医学部',
        'scale': '年200场学术会议，覆盖5000+医生',
        'pain': 'RDPAC合规要求严格，传统直播平台无法满足讲者利益披露、参会签到审计等合规需求。',
        'solution': '直达播合规直播方案：讲者信息披露+实名签到+参会时长审计+录制合规存档。',
        'result': '200场会议零合规风险。讲者管理效率提升80%。审计报告自动生成。',
        'keywords': '医药学术会议直播案例,RDPAC合规直播,药企直播成功案例',
    },
    {
        'slug': 'case-hospital-training-platform',
        'title': '医院内部培训直播案例 | 5000人同时在线学习 - 直达播',
        'h1': '某省级人民医院：内部培训直播平台，5000医护人员在线学习',
        'industry': '省级人民医院 · 科教部',
        'scale': '5000+医护人员，月均50场培训',
        'pain': '各科室培训分散在不同平台，管理混乱。部分培训内容涉密，不能在公有云直播。',
        'solution': '直达播企业培训方案：私有化部署+科室权限管理+培训记录+考试测评。',
        'result': '统一培训平台，管理效率提升70%。培训参与率从40%提升到85%。课件自动录制归档。',
        'keywords': '医院培训直播案例,院内培训系统,医疗教育直播成功案例',
    },
    {
        'slug': 'case-dermatology-aesthetic-clinic',
        'title': '医美机构私域直播案例 | 单场转化300万 - 直达播',
        'h1': '某连锁医美机构：私域直播单场转化300万，复购率提升40%',
        'industry': '连锁医美机构 · 运营部',
        'scale': '全国15家分院，月均20场私域直播',
        'pain': '微信生态直播无法做私域沉淀。患者隐私保护要求高，医美内容审核严格。',
        'solution': '直达播小程序私域直播：微信小程序+患者信息脱敏+内容AI审核+SCRM打通。',
        'result': '单场直播最高转化300万。私域沉淀客户3万+。复购率从25%提升到40%。',
        'keywords': '医美直播案例,私域直播成功案例,医疗私域直播',
    },
    {
        'slug': 'case-oncology-mdt-consultation',
        'title': '肿瘤MDT会诊直播案例 | 跨院多学科远程协作 - 直达播',
        'h1': '某肿瘤医院：MDT多学科会诊直播系统，连接7家协作医院',
        'industry': '肿瘤专科医院 · 医务部',
        'scale': '月均120场MDT会诊，连接7家协作医院',
        'pain': '病理切片需高清共享，跨院网络不稳定。患者隐私数据跨院传输合规风险高。',
        'solution': '直达播MDT会诊方案：4K病理共享+专线加速+端到端加密+等保三级合规。',
        'result': 'MDT会诊效率提升50%。协作医院从3家扩展到7家。病理阅片清晰度满足诊断要求。',
        'keywords': 'MDT会诊直播案例,远程会诊系统,肿瘤多学科会诊',
    },
]

XIAOE_PAGES = [
    {
        'slug': 'xiaoe-vs-zhidabo',
        'title': '小鹅通vs直达播2026 | 医疗直播平台选型对比 - 直达播',
        'h1': '小鹅通vs直达播：医疗直播场景下的5大关键差异',
        'desc': '小鹅通涨价后寻找替代？直达播在医疗直播场景（手术示教/学术会议/院内培训）有显著优势。私有化部署+等保三级+超低延迟+合规审计。全文对比功能/价格/技术/行业适配→',
        'keywords': '小鹅通替代,小鹅通vs直达播,医疗直播平台对比,小鹅通涨价替代方案',
    },
]

def gen_case(d):
    fn = f"{d['slug']}.html"
    fp = os.path.join(BASE, fn)
    html = f"""<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta name="baidu-site-verification" content="codeva-4mRLvHLcFK" />
<meta charset="UTF-8">
<meta name="lastmod" content="2026-07-23">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="{d['industry']}医疗直播成功案例。{d['scale']}。{d['pain'][:60]}。直达播专业方案→">
<meta name="keywords" content="{d['keywords']},医疗直播平台">
<meta name="robots" content="index,follow">
<meta property="og:title" content="{d['title']}">
<meta property="og:description" content="{d['industry']}医疗直播成功案例。{d['scale']}。直达播专业方案→">
<title>{d['title']}</title>
<link rel="canonical" href="https://www.videotvai.com/{fn.replace('.html','')}">
<link rel="stylesheet" href="style.css">
<script async src="https://hm.baidu.com/hm.js?a77a0249f4adf3adcff923b5858c9cf0"></script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"https://www.videotvai.com/"}},{{"@type":"ListItem","position":2,"name":"{d['h1'][:30]}","item":"https://www.videotvai.com/{fn.replace('.html','')}"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"{d['industry'].split('·')[0].strip()}如何选择医疗直播平台？","acceptedAnswer":{{"@type":"Answer","text":"关键看四点：①合规（等保三级/数据安全）②延迟（手术示教需<500ms）③部署方式（公有云/私有化）④行业经验（有无同场景案例）。直达播已服务50+医院和药企，免费获取方案→"}}]}}</script>
<style>
body{{font-family:PingFang SC,Microsoft YaHei,sans-serif;color:#333;line-height:1.8;margin:0;background:#f5f7fa}}
.container{{max-width:900px;margin:0 auto;padding:0 20px}}
.navbar{{background:#fff;padding:16px 0;box-shadow:0 2px 8px rgba(0,0,0,.06);position:sticky;top:0;z-index:100}}
.navbar-content{{max-width:900px;margin:0 auto;padding:0 20px;display:flex;align-items:center;justify-content:space-between}}
.logo{{font-size:20px;font-weight:700;color:#1a1a2e;text-decoration:none}}
.nav-links a{{color:#555;text-decoration:none;margin-left:20px;font-size:14px}}
.hero{{background:linear-gradient(135deg,#1a1a2e,#2d2d44);color:#fff;padding:56px 0 40px;text-align:center}}
.hero h1{{font-size:28px;margin:0 12px;line-height:1.4}}
.content{{background:#fff;padding:32px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.08);margin:-20px auto 40px}}
h2{{color:#1a1a2e;font-size:22px;margin:32px 0 16px;border-bottom:2px solid #E8F2FF;padding-bottom:8px}}
table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}}
th{{background:#1a1a2e;color:#fff;padding:12px 16px;text-align:left}}
td{{padding:10px 16px;border-bottom:1px solid #E0E0E0}}
tr:nth-child(even){{background:#f8f9fa}}
.cta{{background:linear-gradient(135deg,#0066CC,#004C99);color:#fff;text-align:center;padding:40px;border-radius:12px;margin:32px 0}}
.cta a{{display:inline-block;background:#fff;color:#0066CC;padding:14px 32px;border-radius:6px;font-weight:700;text-decoration:none}}
footer{{background:#1a1a2e;color:rgba(255,255,255,.5);padding:40px 0;text-align:center;font-size:14px}}
@media(max-width:768px){{.content{{padding:20px}}.hero h1{{font-size:20px}}}}
</style></head><body>
<header class="navbar"><div class="navbar-content">
<a href="index.html" class="logo">直达播</a>
<nav class="nav-links"><a href="index.html#solutions">解决方案</a><a href="live-medical.html">医疗直播</a><a href="live-surgery.html">手术示教</a><a href="xiaoe-vs-zhidabo">平台对比</a><a href="about.html">关于我们</a></nav>
</div></header>
<section class="hero"><div class="container">
<h1>{d['h1']}</h1>
<p style="opacity:.85;font-size:16px;max-width:650px;margin:12px auto 0">{d['industry']} · {d['scale']}</p>
</div></section>
<div class="container"><div class="content">

<h2>客户背景</h2>
<table>
<tr><th style="width:120px">项目</th><th>详情</th></tr>
<tr><td>客户类型</td><td><strong>{d['industry']}</strong></td></tr>
<tr><td>业务规模</td><td>{d['scale']}</td></tr>
<tr><td>核心需求</td><td>医疗级直播系统，满足合规+高性能+易用性</td></tr>
</table>

<h2>面临挑战</h2>
<div style="background:#FFF3CD;padding:20px;border-radius:8px;border-left:4px solid #FFC107;margin:16px 0">
<strong>⚠️ 核心痛点：</strong>{d['pain']}
</div>

<h2>直达播解决方案</h2>
<div style="background:#E8F5E9;padding:20px;border-radius:8px;border-left:4px solid #4CAF50;margin:16px 0">
<strong>✅ 方案：</strong>{d['solution']}
</div>

<h2>实施效果</h2>
<div style="background:#E3F2FD;padding:20px;border-radius:8px;border-left:4px solid #2196F3;margin:16px 0">
<strong>📊 成果：</strong>{d['result']}
</div>

<h2>为什么选择直达播</h2>
<table>
<tr><th>优势维度</th><th>详情</th></tr>
<tr><td>合规安全</td><td>等保三级认证，支持私有化部署，数据不出院</td></tr>
<tr><td>超低延迟</td><td>WebRTC技术，端到端延迟200-400ms，支持实时互动</td></tr>
<tr><td>行业经验</td><td>已服务50+医院和药企，覆盖手术示教/学术会议/院内培训</td></tr>
<tr><td>全场景覆盖</td><td>手术直播+学术会议+MDT会诊+内部培训+私域运营</td></tr>
</table>

<div class="cta">
<h2 style="color:#fff;margin:0 0 12px">类似场景需要方案？</h2>
<p style="margin:0 0 20px;opacity:.9">告知您的行业和需求，30分钟出专属方案</p>
<a href="tel:400-800-8888">📞 免费咨询</a>
</div>

</div></div>
<footer><div class="container">
<p>直达播 © 2026 · 医疗直播专家</p>
<p style="margin-top:8px"><a href="https://beian.miit.gov.cn/" style="color:rgba(255,255,255,.5)" target="_blank" rel="nofollow">湘ICP备2026016030号-2</a></p>
</div></footer>
</body></html>"""
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
    return fn

def gen_xiaoe(d):
    fn = f"{d['slug']}.html"
    fp = os.path.join(BASE, fn)
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta name="baidu-site-verification" content="codeva-4mRLvHLcFK" />
<meta charset="UTF-8">
<meta name="lastmod" content="2026-07-23">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="{d['desc']}">
<meta name="keywords" content="{d['keywords']}">
<meta name="robots" content="index,follow">
<meta property="og:title" content="{d['title']}">
<meta property="og:description" content="{d['desc']}">
<title>{d['title']}</title>
<link rel="canonical" href="https://www.videotvai.com/{fn.replace('.html','')}">
<link rel="stylesheet" href="style.css">
<script async src="https://hm.baidu.com/hm.js?a77a0249f4adf3adcff923b5858c9cf0"></script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首页","item":"https://www.videotvai.com/"}},{{"@type":"ListItem","position":2,"name":"小鹅通vs直达播","item":"https://www.videotvai.com/{fn.replace('.html','')}"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"小鹅通涨价后有什么替代方案？","acceptedAnswer":{{"@type":"Answer","text":"如果主要用于医疗直播（手术示教/学术会议/院内培训），直达播是更好的替代方案。直达播支持私有化部署+等保三级+超低延迟+合规审计，且价格不随功能叠加暴涨。知识付费场景小鹅通仍有优势。"}},{{"@type":"Question","name":"小鹅通和直达播哪个便宜？","acceptedAnswer":{{"@type":"Answer","text":"通用直播场景小鹅通入门版更便宜，但医疗直播场景直达播性价比更高——直达播的私有化部署+等保三级+超低延迟是医疗行业刚需，小鹅通需购买最高版本才有类似功能。建议根据实际场景对比测试。"}}]}}</script>
<style>
body{{font-family:PingFang SC,Microsoft YaHei,sans-serif;color:#333;line-height:1.8;margin:0;background:#f5f7fa}}
.container{{max-width:900px;margin:0 auto;padding:0 20px}}
.navbar{{background:#fff;padding:16px 0;box-shadow:0 2px 8px rgba(0,0,0,.06);position:sticky;top:0;z-index:100}}
.navbar-content{{max-width:900px;margin:0 auto;padding:0 20px;display:flex;align-items:center;justify-content:space-between}}
.logo{{font-size:20px;font-weight:700;color:#1a1a2e;text-decoration:none}}
.nav-links a{{color:#555;text-decoration:none;margin-left:20px;font-size:14px}}
.hero{{background:linear-gradient(135deg,#1a1a2e,#2d2d44);color:#fff;padding:56px 0 40px;text-align:center}}
.hero h1{{font-size:28px;margin:0 12px;line-height:1.4}}
.content{{background:#fff;padding:32px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,.08);margin:-20px auto 40px}}
h2{{color:#1a1a2e;font-size:22px;margin:32px 0 16px;border-bottom:2px solid #E8F2FF;padding-bottom:8px}}
table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}}
th{{background:#1a1a2e;color:#fff;padding:12px 16px;text-align:left}}
td{{padding:10px 16px;border-bottom:1px solid #E0E0E0}}
tr:nth-child(even){{background:#f8f9fa}}
.cta{{background:linear-gradient(135deg,#0066CC,#004C99);color:#fff;text-align:center;padding:40px;border-radius:12px;margin:32px 0}}
.cta a{{display:inline-block;background:#fff;color:#0066CC;padding:14px 32px;border-radius:6px;font-weight:700;text-decoration:none}}
footer{{background:#1a1a2e;color:rgba(255,255,255,.5);padding:40px 0;text-align:center;font-size:14px}}
@media(max-width:768px){{.content{{padding:20px}}.hero h1{{font-size:20px}}}}
</style></head><body>
<header class="navbar"><div class="navbar-content">
<a href="index.html" class="logo">直达播</a>
<nav class="nav-links"><a href="index.html#solutions">解决方案</a><a href="live-medical.html">医疗直播</a><a href="live-surgery.html">手术示教</a><a href="xiaoe-vs-zhidabo">平台对比</a><a href="about.html">关于我们</a></nav>
</div></header>
<section class="hero"><div class="container">
<h1>{d['h1']}</h1>
<p style="opacity:.85;font-size:16px;max-width:650px;margin:12px auto 0">小鹅通2026年大幅涨价？医疗直播场景下，直达播可能是更好的选择</p>
</div></section>
<div class="container"><div class="content">

<div style="background:#FFF3CD;padding:20px;border-radius:8px;border-left:4px solid #FFC107;margin-bottom:24px">
<strong>📌 一句话总结：</strong>小鹅通是通用型知识付费/私域直播工具，直达播专注<strong>医疗直播</strong>垂直场景。如果你的核心需求是医疗级直播（手术示教/学术会议/院内培训），直达播在合规、延迟、部署方式上有本质优势。
</div>

<h2>一、小鹅通 vs 直达播：核心差异</h2>
<table>
<tr><th>对比维度</th><th>小鹅通</th><th>直达播</th></tr>
<tr><td>定位</td><td>知识付费+私域直播通用平台</td><td>医疗直播垂直专家</td></tr>
<tr><td>延迟</td><td>标准CDN 3-8秒</td><td>WebRTC 200-400ms</td></tr>
<tr><td>合规</td><td>基础合规</td><td>等保三级+私有化部署</td></tr>
<tr><td>部署方式</td><td>纯SaaS公有云</td><td>SaaS + 私有化部署</td></tr>
<tr><td>手术示教</td><td>不支持（延迟太高）</td><td>核心场景</td></tr>
<tr><td>学术会议</td><td>基础支持</td><td>RDPAC合规+讲者管理+审计</td></tr>
<tr><td>院内培训</td><td>可用</td><td>私有化+科室权限+考试系统</td></tr>
<tr><td>价格模式</td><td>按版本+功能叠加收费（涨价中）</td><td>按场景定制，一口价</td></tr>
</table>

<h2>二、小鹅通2026涨价背景</h2>
<p>小鹅通2026年进行了价格调整，多个版本费用上涨30-60%。对于主要使用直播功能的用户来说，功能捆绑导致的费用膨胀是最大的痛点。尤其是医疗行业客户，很多高级功能（如私有化部署、合规审计、超低延迟）在小鹅通需要购买最高版本才可用，综合成本大幅上升。</p>

<h2>三、什么时候该从小鹅通切换到直达播？</h2>
<table>
<tr><th>场景</th><th>推荐平台</th><th>原因</th></tr>
<tr><td>知识付费/课程售卖</td><td>小鹅通</td><td>知识付费生态更成熟（支付/分销/CRM）</td></tr>
<tr><td>医疗手术示教</td><td><strong>直达播</strong></td><td>超低延迟+私有化部署是刚需</td></tr>
<tr><td>医药学术会议</td><td><strong>直达播</strong></td><td>RDPAC合规+讲者披露+审计</td></tr>
<tr><td>医院内部培训</td><td><strong>直达播</strong></td><td>私有化+数据安全+考试测评</td></tr>
<tr><td>通用私域直播</td><td>小鹅通</td><td>私域运营工具链更全</td></tr>
<tr><td>MDT远程会诊</td><td><strong>直达播</strong></td><td>4K病理共享+专线+加密</td></tr>
</table>

<h2>四、从小鹅通迁移到直达播的流程</h2>
<ol>
<li><strong>需求评估</strong>：确认你的核心场景是否为医疗直播（手术/会议/培训/会诊）</li>
<li><strong>方案对比</strong>：获取直达播定制方案，与小鹅通当前方案做功能/价格对比</li>
<li><strong>试用测试</strong>：申请直达播试用，实测延迟/画质/合规功能</li>
<li><strong>数据迁移</strong>：历史录制视频可批量导出→导入直达播</li>
<li><strong>正式切换</strong>：新直播使用直达播，小鹅通保留至到期或仅用于知识付费</li>
</ol>

<div class="cta">
<h2 style="color:#fff;margin:0 0 12px">正在评估小鹅通替代方案？</h2>
<p style="margin:0 0 20px;opacity:.9">告知您的使用场景，30分钟出对比方案+报价</p>
<a href="tel:400-800-8888">📞 免费获取对比方案</a>
</div>

</div></div>
<footer><div class="container">
<p>直达播 © 2026 · 医疗直播专家</p>
<p style="margin-top:8px"><a href="https://beian.miit.gov.cn/" style="color:rgba(255,255,255,.5)" target="_blank" rel="nofollow">湘ICP备2026016030号-2</a></p>
</div></footer>
</body></html>"""
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
    return fn

def main():
    pages = []
    
    # Case studies
    for d in CASES:
        fn = gen_case(d)
        pages.append(fn)
        print(f'✅ case: {fn}')
    
    # Xiaoe-tech
    for d in XIAOE_PAGES:
        fn = gen_xiaoe(d)
        pages.append(fn)
        print(f'✅ xiaoe: {fn}')
    
    # Update sitemap
    print(f'\n📊 总计: {len(pages)} 页 (5案例+1迁移)')
    
    # Update baidu push
    push_file = os.path.join(BASE, 'baidu_push_queue.txt') if os.path.exists(os.path.join(BASE, 'baidu_push_queue.txt')) else None
    if push_file:
        existing = set()
        with open(push_file) as f:
            existing = set(line.strip() for line in f if line.strip())
        new = [f'https://www.videotvai.com/{p.replace(".html","")}' for p in pages]
        added = [u for u in new if u not in existing]
        if added:
            with open(push_file, 'a') as f:
                for u in added:
                    f.write(u + '\n')
            print(f'📤 推送队列新增: {len(added)} URL')

if __name__ == '__main__':
    main()
