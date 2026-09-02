# videotvai.com 百度推送 automation 执行历史

## 2026-09-02
- 结果：**over quota（今日配额已耗尽）**，10→5→2→1 降级重试后仍配额耗尽，正常退出（exit 0）。无新 URL 推送。
- ⚠️ 用户 query 给的命令用系统 python3.13.12，但该 python 缺 requests 模块；实际用 venv python（`/Users/mac/.workbuddy/binaries/python/envs/default/bin/python`）执行成功。
- baidu_pushed.txt 仍为 158 条。

## 2026-09-01
- 结果：**over quota（今日配额已耗尽）**，10→5→2→1 降级重试后仍配额耗尽，正常退出。无新 URL 推送。
- 🔴 根因修复：脚本 `baidu_push_daily.py` 的 `requests.post` 原本缺 `proxies={'http':None,'https':None}`，会走环境变量 HTTP_PROXY（127.0.0.1:62470 connector-proxy）访问百度 API 导致 hang → 被 120s 超时 SIGTERM(exit 137)。已补 proxies 参数，验证脚本正常退出（exit 0）。
- ⚠️ 运行要点：必须用 venv python（`/Users/mac/.workbuddy/binaries/python/envs/default/bin/python`），系统 python3.13 缺 requests 模块。
- baidu_pushed.txt 已累计 158 条。
