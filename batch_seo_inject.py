#!/usr/bin/env python3
"""
videotvai.com Batch SEO Injector
Handles 5 tasks simultaneously:
  #899 BreadcrumbList Schema (20 pages)
  #900 Article Schema (1 page: surgery-teaching-live-system.html)
  #901 Organization Schema (1 page: surgery-teaching-live-system.html)
  #903 Baidu auto-push JS (20 pages)
  #904 OG tags (5 blog pages)
"""
import re, os, json, html as html_mod

BASE_URL = "https://www.videotvai.com"
SITE_NAME = "直达播"
OG_IMAGE = f"{BASE_URL}/og-default.png"

# Skip these files (noindex/verification/admin)
SKIP_FILES = {
    '404.html',
    'admin.html',
    'baidu_verify_codeva-4mRLvHLcFK.html',
    'baidu_verify_codeva-PybX5z0P4T.html',
    'blog-old.html',
}

# Breadcrumb name mapping for non-blog pages
BREADCRUMB_NAMES = {
    'index.html': '首页',
    'about.html': '关于直达播',
    'ai-products.html': 'AI产品',
    'face-auth.html': '人脸识别认证',
    'live-ecommerce.html': '电商直播',
    'live-health.html': '医疗直播',
    'live-medical.html': '医疗学术直播',
    'live-miniprogram.html': '小程序直播',
    'live-products.html': '产品方案',
    'live-surgery.html': '手术示教直播',
    'remote-consultation.html': '远程会诊',
    'blog.html': '博客',
}

def get_title(content):
    """Extract page title from <title> tag"""
    m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    if m:
        return html_mod.unescape(m.group(1).strip())
    return SITE_NAME

def get_description(content):
    """Extract meta description"""
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    if m:
        return html_mod.unescape(m.group(1).strip())
    return ""

def get_canonical(content):
    """Extract canonical URL"""
    m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return ""

def generate_breadcrumb_jsonld(filepath, content):
    """Generate BreadcrumbList JSON-LD based on page location"""
    filename = os.path.basename(filepath)
    canonical = get_canonical(content) or f"{BASE_URL}/{filename.replace('.html', '')}"

    if filename == 'index.html':
        items = [{"name": "首页", "url": BASE_URL + "/"}]
    elif 'blog/' in filepath:
        title = get_title(content)
        items = [
            {"name": "首页", "url": BASE_URL + "/"},
            {"name": "博客", "url": BASE_URL + "/blog"},
            {"name": title, "url": canonical}
        ]
    elif filename in BREADCRUMB_NAMES:
        name = BREADCRUMB_NAMES[filename]
        if filename == 'index.html':
            items = [{"name": "首页", "url": BASE_URL + "/"}]
        else:
            items = [
                {"name": "首页", "url": BASE_URL + "/"},
                {"name": name, "url": canonical}
            ]
    else:
        title = get_title(content)
        items = [
            {"name": "首页", "url": BASE_URL + "/"},
            {"name": title, "url": canonical}
        ]

    item_list = []
    for i, item in enumerate(items, 1):
        item_list.append({
            "@type": "ListItem",
            "position": i,
            "name": item["name"],
            "item": item["url"]
        })

    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": item_list
    }

def generate_article_jsonld(filepath, content):
    """Generate Article JSON-LD for blog pages"""
    title = get_title(content)
    desc = get_description(content)
    canonical = get_canonical(content) or f"{BASE_URL}/{filepath.replace('./', '')}"

    # Try to extract date from filename or use default
    date_published = "2026-06-15"
    date_modified = "2026-07-19"

    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc[:200] if desc else title,
        "image": OG_IMAGE,
        "datePublished": date_published,
        "dateModified": date_modified,
        "author": {
            "@type": "Organization",
            "name": SITE_NAME
        },
        "publisher": {
            "@type": "Organization",
            "name": SITE_NAME,
            "logo": {
                "@type": "ImageObject",
                "url": OG_IMAGE
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": canonical
        }
    }

def generate_organization_jsonld():
    """Generate Organization JSON-LD"""
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": SITE_NAME,
        "alternateName": "VideoTV",
        "url": BASE_URL,
        "description": "直达播是一家专业的企业级直播平台服务商，提供医疗学术直播、手术示教直播、私域电商直播、小程序直播等解决方案。",
        "foundingDate": "2024",
        "contactPoint": {
            "@type": "ContactPoint",
            "contactType": "customer service",
            "availableLanguage": ["Chinese", "English"]
        },
        "logo": OG_IMAGE
    }

BAIDU_PUSH_JS = """
<script>
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    } else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
"""

def generate_og_tags(filepath, content):
    """Generate OG meta tags"""
    title = get_title(content)
    desc = get_description(content)
    canonical = get_canonical(content) or f"{BASE_URL}/{filepath.replace('./', '').replace('.html', '')}"
    og_type = "article" if 'blog/' in filepath else "website"

    tags = f'''<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc[:200] if desc else title}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{SITE_NAME}">'''
    return tags

def inject_jsonld_before_head_close(content, jsonld_dict):
    """Inject JSON-LD script before </head>"""
    jsonld_str = json.dumps(jsonld_dict, ensure_ascii=False, indent=2)
    script_tag = f'\n<script type="application/ld+json">\n{jsonld_str}\n</script>\n'

    if '</head>' in content:
        return content.replace('</head>', script_tag + '</head>')
    return content

def inject_multiple_jsonld_before_head_close(content, jsonld_list):
    """Inject multiple JSON-LD scripts before </head>"""
    scripts = ""
    for jld in jsonld_list:
        jsonld_str = json.dumps(jld, ensure_ascii=False, indent=2)
        scripts += f'\n<script type="application/ld+json">\n{jsonld_str}\n</script>\n'

    if '</head>' in content:
        return content.replace('</head>', scripts + '</head>')
    return content

def inject_push_js_before_body_close(content):
    """Inject Baidu push JS before </body>"""
    if '</body>' in content:
        return content.replace('</body>', BAIDU_PUSH_JS + '\n</body>')
    elif '</html>' in content:
        return content.replace('</html>', BAIDU_PUSH_JS + '\n</html>')
    return content + BAIDU_PUSH_JS

def inject_og_tags_in_head(content, og_tags):
    """Inject OG tags in <head>, after canonical or before </head>"""
    # Try to insert after canonical link
    canonical_pattern = r'(<link\s+rel=["\']canonical["\'][^>]*>)'
    if re.search(canonical_pattern, content):
        return re.sub(canonical_pattern, r'\1\n' + og_tags, content)

    # Try to insert after first meta description
    desc_pattern = r'(<meta\s+name=["\']description["\'][^>]*>)'
    if re.search(desc_pattern, content):
        return re.sub(desc_pattern, r'\1\n' + og_tags, content)

    # Fallback: insert before </head>
    if '</head>' in content:
        return content.replace('</head>', og_tags + '\n</head>')
    return content

def process_file(filepath):
    """Process a single HTML file"""
    filename = os.path.basename(filepath)
    if filename in SKIP_FILES:
        return None

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # Task #899: BreadcrumbList Schema
    if 'BreadcrumbList' not in content:
        bc_jsonld = generate_breadcrumb_jsonld(filepath, content)
        jsonld_list = [bc_jsonld]

        # Task #900: Article Schema (blog pages only)
        if 'blog/' in filepath and '"@type": "Article"' not in content and '"@type":"Article"' not in content:
            art_jsonld = generate_article_jsonld(filepath, content)
            jsonld_list.append(art_jsonld)
            changes.append('Article Schema')

        # Task #901: Organization Schema
        if '"@type": "Organization"' not in content and '"@type":"Organization"' not in content:
            org_jsonld = generate_organization_jsonld()
            jsonld_list.append(org_jsonld)
            changes.append('Organization Schema')

        content = inject_multiple_jsonld_before_head_close(content, jsonld_list)
        changes.append('BreadcrumbList Schema')
    else:
        # Even if breadcrumb exists, check for Article and Organization
        if 'blog/' in filepath and '"@type": "Article"' not in content and '"@type":"Article"' not in content:
            art_jsonld = generate_article_jsonld(filepath, content)
            content = inject_jsonld_before_head_close(content, art_jsonld)
            changes.append('Article Schema')

        if '"@type": "Organization"' not in content and '"@type":"Organization"' not in content:
            org_jsonld = generate_organization_jsonld()
            content = inject_jsonld_before_head_close(content, org_jsonld)
            changes.append('Organization Schema')

    # Task #903: Baidu auto-push JS
    if 'push.zhanzhang.baidu.com' not in content and 'zz.bdstatic.com' not in content:
        content = inject_push_js_before_body_close(content)
        changes.append('Push JS')

    # Task #904: OG tags
    if 'og:title' not in content:
        og_tags = generate_og_tags(filepath, content)
        content = inject_og_tags_in_head(content, og_tags)
        changes.append('OG tags')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return None

def main():
    # Collect all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
    html_files.sort()

    stats = {
        'breadcrumb': 0,
        'article': 0,
        'organization': 0,
        'push_js': 0,
        'og': 0,
        'total_modified': 0,
    }

    for fp in html_files:
        result = process_file(fp)
        if result:
            stats['total_modified'] += 1
            if 'BreadcrumbList Schema' in result: stats['breadcrumb'] += 1
            if 'Article Schema' in result: stats['article'] += 1
            if 'Organization Schema' in result: stats['organization'] += 1
            if 'Push JS' in result: stats['push_js'] += 1
            if 'OG tags' in result: stats['og'] += 1
            print(f"  [MODIFIED] {fp}: {', '.join(result)}")
        else:
            print(f"  [SKIP] {fp}")

    print(f"\n=== Summary ===")
    print(f"Total files modified: {stats['total_modified']}")
    print(f"  BreadcrumbList added: {stats['breadcrumb']}")
    print(f"  Article Schema added: {stats['article']}")
    print(f"  Organization Schema added: {stats['organization']}")
    print(f"  Push JS added: {stats['push_js']}")
    print(f"  OG tags added: {stats['og']}")

if __name__ == '__main__':
    main()
