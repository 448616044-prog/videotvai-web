#!/bin/bash
# GitHub Actions 部署诊断脚本
# 用于排查 videotvai-web 项目的部署问题

echo "=========================================="
echo "VideoTV GitHub Actions 部署诊断工具"
echo "=========================================="
echo ""

# 检查1: Git仓库状态
echo "📋 检查1: Git仓库状态"
if [ -d ".git" ]; then
    echo "✅ 当前目录是Git仓库"
    git remote -v | grep origin && echo "✅ 远程仓库已配置"
else
    echo "⚠️  当前目录不是Git仓库"
fi
echo ""

# 检查2: GitHub Secrets 配置检查（本地无法直接检查，提示用户）
echo "📋 检查2: GitHub Secrets 配置"
echo "⚠️  请在 GitHub 仓库的 Settings > Secrets 中确认以下配置:"
echo "   - CVM_HOST: 腾讯云服务器公网IP"
echo "   - CVM_USER: 服务器用户名 (通常是 root)"
echo "   - CVM_SSH_KEY: SSH私钥 (需要包含 -----BEGIN OPENSSH PRIVATE KEY-----)"
echo ""
echo "💡 验证方法: 在GitHub仓库点击 Settings > Secrets and variables > Actions"
echo ""

# 检查3: GitHub Actions 工作流文件
echo "📋 检查3: GitHub Actions 工作流文件"
if [ -f ".github/workflows/deploy.yml" ]; then
    echo "✅ deploy.yml 存在"
    echo "📝 工作流内容预览:"
    head -20 .github/workflows/deploy.yml | grep -E "name:|on:|uses:|with:"
else
    echo "❌ deploy.yml 不存在!"
fi
echo ""

# 检查4: 最近的 Git 提交
echo "📋 检查4: 最近的 Git 提交"
git log --oneline -5 2>/dev/null || echo "无法获取提交历史"
echo ""

# 检查5: GitHub Actions 最近运行状态（需要 gh CLI）
echo "📋 检查5: GitHub Actions 状态"
if command -v gh &> /dev/null; then
    echo "🔄 尝试获取Actions运行状态..."
    gh run list --limit 5 2>/dev/null || echo "无法获取Actions状态，请确认已登录 GitHub CLI"
else
    echo "⚠️  GitHub CLI (gh) 未安装"
    echo "💡 安装方法: brew install gh"
    echo "💡 登录方法: gh auth login"
fi
echo ""

# 检查6: CVM 连接测试（需要目标IP）
echo "📋 检查6: CVM 连接测试"
read -p "请输入 CVM 公网IP (或按回车跳过): " cvm_ip
if [ ! -z "$cvm_ip" ]; then
    echo "🔄 测试 SSH 连接..."
    if ssh -o ConnectTimeout=5 -o BatchMode=yes $cvm_ip "echo '✅ SSH连接成功'" 2>/dev/null; then
        echo "✅ SSH 连接正常"
    else
        echo "❌ SSH 连接失败，请检查:"
        echo "   1. IP地址是否正确"
        echo "   2. SSH密钥是否已添加到服务器"
        echo "   3. 服务器SSH服务是否运行"
    fi
fi
echo ""

# 检查7: 常见问题解决方案
echo "=========================================="
echo "📚 常见问题与解决方案"
echo "=========================================="
echo ""
echo "问题1: 'Host key verification failed'"
echo "   解决: 确保 secrets.CVM_SSH_KEY 使用的是正确的私钥"
echo ""
echo "问题2: 'Permission denied (publickey)'"
echo "   解决: "
echo "   - 确认SSH私钥格式正确"
echo "   - 确认公钥已添加到服务器的 ~/.ssh/authorized_keys"
echo ""
echo "问题3: 'Connection refused'"
echo "   解决:"
echo "   - 确认服务器IP和端口(默认22)正确"
echo "   - 确认服务器SSH服务正在运行"
echo ""
echo "问题4: 'Workflow not found'"
echo "   解决: 确认 deploy.yml 在仓库的 .github/workflows/ 目录下"
echo ""
echo "问题5: 'Secrets not configured'"
echo "   解决: 在 GitHub 仓库 Settings > Secrets 配置以下变量:"
echo "   - CVM_HOST"
echo "   - CVM_USER"  
echo "   - CVM_SSH_KEY"
echo ""
echo "=========================================="
echo "诊断完成！"
echo "=========================================="
