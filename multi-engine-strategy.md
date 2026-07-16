# videotvai.com 多引擎覆盖方案：360 搜索 + 搜狗 + 神马 + 头条搜索

> 百度是核心，但国内搜索流量分散，360 搜索占 20%+，搜狗占 10%+（含微信搜一搜）

---

## 一、360 搜索 (so.com) 优化

### 站长平台
- 注册入口：https://zhanzhang.so.com/
- 验证方式：HTML文件上传 / meta标签

### 360 搜索特点
- 更注重网站安全性（SSL证书必须有效）
- 更喜欢老域名（域名年龄是排名因子）
- 对标题关键词匹配度要求更高
- 360浏览器内置搜索，PC端占比高

### 优化要点
1. **提交 sitemap** 到 360 站长平台
2. **确保 SSL 有效**（Let's Encrypt 也接受）
3. **标题中关键词前置**（和百度一样 ≤30 字）
4. **避免弹窗广告**（360 安全检测严格）

### 360 站长平台 API 推送
```
POST http://zhanzhang.so.com/sitetool/urlSubmit
参数: site={videotvai.com}&token={token}&urls={URL列表}
```

---

## 二、搜狗搜索 (sogou.com) 优化

### 核心价值：微信搜一搜
搜狗是微信搜一搜的默认搜索引擎。如果内容能在搜狗排名好，就能在微信搜索中获得曝光。

### 站长平台
- 注册入口：https://zhanzhang.sogou.com/
- 验证方式：HTML文件 + CNAME解析

### 优化要点
1. **微信生态内容优先**：搜狗偏好收录微信公众号文章
2. **移动端适配**：搜狗移动端流量占比 85%+
3. **页面结构清晰**：H1-H6 层级、面包屑导航
4. **结构化数据**：搜狗支持 Schema.org 标记

### 搜狗推送 API
```
POST https://zhanzhang.sogou.com/api/urlSubmit
```

---

## 三、神马搜索 (sm.cn) 

### 特点
- UC 浏览器默认引擎，纯移动端
- 阿里系产品矩阵（淘宝/UC/高德内部搜索入口）
- 对电商类内容更友好

### 优化要点
1. **极致移动端优化**（页面 <50KB、图片压缩）
2. **AMP/MIP 支持**（神马推自己的移动加速页面）
3. **电商属性内容**：产品页、价格页的 Schema 标记

---

## 四、头条搜索 (toutiao.com)

### 特点
- 字节跳动旗下，头条/抖音内部搜索
- 偏爱"新"内容（发布时间越近越好）
- 标题党反而友好（吸引点击的标题加分）

### 优化要点
1. **发布头条号内容**并同步到网站
2. **频繁更新**（日更比周更的收录率高 3 倍）
3. **结构化数据**：头条支持 JSON-LD

---

## 五、多引擎一键提交脚本

```
#!/bin/bash
# 同时推送到百度+360+搜狗

URL="https://www.videotvai.com/sitemap.xml"

# 百度
curl -s "http://data.zz.baidu.com/urls?site=${BAIDU_SITE}&token=${BAIDU_TOKEN}" -H 'Content-Type:text/plain' --data-binary "$URL"

# 360
curl -s "http://zhanzhang.so.com/sitetool/urlSubmit?site=${SO360_SITE}&token=${SO360_TOKEN}&urls=${URL}"

# 搜狗
curl -s "https://zhanzhang.sogou.com/api/urlSubmit?site=${SOGOU_SITE}&token=${SOGOU_TOKEN}&urls=${URL}"
```

---

## 六、执行优先级

| 优先级 | 平台 | 投入 | 预期流量贡献 |
|:---:|:---|:---:|:---:|
| P0 | 百度 | 已全面部署 | 60% |
| P1 | 360 搜索 | 注册站长平台+提交sitemap | 20% |
| P2 | 搜狗/微信搜一搜 | 注册+开通公众号同步 | 15% |
| P3 | 神马搜索 | 移动端极致优化 | 3% |
| P4 | 头条搜索 | 开通头条号并同步 | 2% |

## 结论

**当前阶段建议**：先把 360 和搜狗的站长平台注册验证，提交 sitemap。这两个平台加起来能贡献 35% 的搜索流量，且操作成本极低（只需要注册+验证+sitemap提交，2小时内搞定）。
