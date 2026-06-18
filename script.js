/**
 * VideoTV 官网交互脚本
 * 功能：移动端菜单、数字滚动动画、Tab切换、平滑滚动等
 */

(function() {
    'use strict';

    // ========================================
    // 工具函数
    // ========================================
    
    /**
     * 防抖函数
     * @param {Function} func - 要执行的函数
     * @param {number} wait - 等待时间
     * @returns {Function}
     */
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    /**
     * 节流函数
     * @param {Function} func - 要执行的函数
     * @param {number} limit - 限制时间
     * @returns {Function}
     */
    function throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }

    // ========================================
    // 移动端菜单功能
    // ========================================
    
    const MobileMenu = {
        menuBtn: null,
        mobileMenu: null,
        isOpen: false,

        init() {
            this.menuBtn = document.getElementById('mobileMenuBtn');
            this.mobileMenu = document.getElementById('mobileMenu');

            if (!this.menuBtn || !this.mobileMenu) return;

            this.menuBtn.addEventListener('click', () => this.toggle());

            // 点击菜单外部关闭
            document.addEventListener('click', (e) => {
                if (this.isOpen &&
                    !this.mobileMenu.contains(e.target) &&
                    !this.menuBtn.contains(e.target)) {
                    this.close();
                }
            });

            // 点击菜单内链接后关闭
            this.mobileMenu.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    if (this.isOpen) this.close();
                });
            });

            // ESC键关闭菜单
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && this.isOpen) {
                    this.close();
                }
            });
        },

        toggle() {
            this.isOpen ? this.close() : this.open();
        },

        open() {
            this.isOpen = true;
            this.menuBtn.classList.add('active');
            this.mobileMenu.classList.add('active');
            document.body.style.overflow = 'hidden';
        },

        close() {
            this.isOpen = false;
            this.menuBtn.classList.remove('active');
            this.mobileMenu.classList.remove('active');
            document.body.style.overflow = '';
        }
    };

    // ========================================
    // 导航栏滚动效果
    // ========================================
    
    const HeaderScroll = {
        header: null,
        lastScrollY: 0,

        init() {
            this.header = document.getElementById('navbar') || document.querySelector('.navbar');
            if (!this.header) return;

            window.addEventListener('scroll', throttle(() => {
                this.handleScroll();
            }, 100));
        },

        handleScroll() {
            const currentScrollY = window.scrollY;

            // 添加/移除滚动样式
            if (currentScrollY > 50) {
                this.header.classList.add('scrolled');
            } else {
                this.header.classList.remove('scrolled');
            }

            this.lastScrollY = currentScrollY;
        }
    };

    // ========================================
    // 数字滚动动画
    // ========================================
    
    const CountUpAnimation = {
        elements: [],
        hasAnimated: false,

        init() {
            this.elements = document.querySelectorAll('.stat-number .number');
            if (this.elements.length === 0) return;

            // 使用 Intersection Observer 检测元素是否进入视口
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !this.hasAnimated) {
                        this.animate();
                        this.hasAnimated = true;
                    }
                });
            }, {
                threshold: 0.5
            });

            const statsSection = document.querySelector('.stats-section');
            if (statsSection) {
                observer.observe(statsSection);
            }
        },

        animate() {
            this.elements.forEach(element => {
                const target = parseInt(element.getAttribute('data-target'), 10);
                const duration = 2000; // 动画持续时间（毫秒）
                const startTime = performance.now();
                const startValue = 0;

                const updateCount = (currentTime) => {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    
                    // 使用 easeOutExpo 缓动函数
                    const easeProgress = 1 - Math.pow(2, -10 * progress);
                    const currentValue = Math.floor(startValue + (target - startValue) * easeProgress);
                    
                    element.textContent = currentValue;

                    if (progress < 1) {
                        requestAnimationFrame(updateCount);
                    } else {
                        element.textContent = target;
                    }
                };

                requestAnimationFrame(updateCount);
            });
        }
    };

    // ========================================
    // Tab 切换功能
    // ========================================
    
    const TabSwitcher = {
        init() {
            const tabBtns = document.querySelectorAll('.tab-btn');

            if (tabBtns.length === 0) return;

            tabBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    const targetTab = btn.getAttribute('data-tab');

                    // 移除所有活动状态
                    tabBtns.forEach(b => b.classList.remove('active'));

                    // 移除 tab-content 和 scene-content 的活动状态
                    document.querySelectorAll('.tab-content, .scene-content').forEach(c => c.classList.remove('active'));

                    // 添加活动状态
                    btn.classList.add('active');
                    // 优先查找 tab-content，如果没有则查找 scene-content
                    const targetContent = document.getElementById('tab-' + targetTab) || document.getElementById('scene-' + targetTab);
                    if (targetContent) {
                        targetContent.classList.add('active');
                    }
                });
            });
        }
    };

    // ========================================
    // 平滑滚动
    // ========================================
    
    const SmoothScroll = {
        init() {
            // 为所有锚点链接添加平滑滚动
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function(e) {
                    const href = this.getAttribute('href');
                    if (href === '#') return;

                    e.preventDefault();
                    const target = document.querySelector(href);
                    if (target) {
                        const headerHeight = document.getElementById('navbar').offsetHeight || 72;
                        const targetPosition = target.getBoundingClientRect().top + window.scrollY - headerHeight;

                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });
                    }
                });
            });
        }
    };

    // ========================================
    // 滚动显示动画
    // ========================================
    
    const ScrollReveal = {
        init() {
            const revealElements = document.querySelectorAll('.product-card, .solution-card, .section-header');
            
            if (revealElements.length === 0) return;

            // 添加初始类
            revealElements.forEach(el => {
                el.classList.add('scroll-reveal');
            });

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('revealed');
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            });

            revealElements.forEach(el => observer.observe(el));
        }
    };

    // ========================================
    // 按钮点击效果
    // ========================================
    
    const ButtonEffects = {
        init() {
            document.querySelectorAll('.btn').forEach(btn => {
                btn.addEventListener('click', function(e) {
                    // 创建涟漪效果
                    const ripple = document.createElement('span');
                    const rect = this.getBoundingClientRect();
                    const size = Math.max(rect.width, rect.height);
                    const x = e.clientX - rect.left - size / 2;
                    const y = e.clientY - rect.top - size / 2;

                    ripple.style.cssText = `
                        position: absolute;
                        width: ${size}px;
                        height: ${size}px;
                        left: ${x}px;
                        top: ${y}px;
                        background: rgba(255, 255, 255, 0.3);
                        border-radius: 50%;
                        transform: scale(0);
                        animation: ripple 0.6s ease-out;
                        pointer-events: none;
                    `;

                    this.style.position = 'relative';
                    this.style.overflow = 'hidden';
                    this.appendChild(ripple);

                    setTimeout(() => ripple.remove(), 600);
                });
            });

            // 添加涟漪动画样式
            const style = document.createElement('style');
            style.textContent = `
                @keyframes ripple {
                    to {
                        transform: scale(2);
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    };

    // ========================================
    // 侧边工具栏交互
    // ========================================
    
    const SidebarTools = {
        init() {
            const toolItems = document.querySelectorAll('.tool-item');
            
            toolItems.forEach(item => {
                item.addEventListener('click', () => {
                    const text = item.querySelector('.tool-text').textContent;
                    
                    // 显示提示
                    this.showToast(`您点击了：${text}`);
                });
            });
        },

        showToast(message) {
            // 移除已有的 toast
            const existingToast = document.querySelector('.toast-message');
            if (existingToast) {
                existingToast.remove();
            }

            // 创建新的 toast
            const toast = document.createElement('div');
            toast.className = 'toast-message';
            toast.textContent = message;
            toast.style.cssText = `
                position: fixed;
                bottom: 100px;
                left: 50%;
                transform: translateX(-50%);
                background: rgba(0, 0, 0, 0.8);
                color: white;
                padding: 12px 24px;
                border-radius: 8px;
                font-size: 14px;
                z-index: 9999;
                animation: fadeInUp 0.3s ease;
            `;

            document.body.appendChild(toast);

            setTimeout(() => {
                toast.style.animation = 'fadeOutDown 0.3s ease';
                setTimeout(() => toast.remove(), 300);
            }, 2000);
        },

        showSuccessModal(message) {
            // 移除已有的弹窗
            const existingOverlay = document.querySelector('.success-modal-overlay');
            if (existingOverlay) existingOverlay.remove();

            // 创建遮罩（弹窗放内部，彻底解决层叠问题）
            const overlay = document.createElement('div');
            overlay.className = 'success-modal-overlay';
            overlay.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.6);
                z-index: 9999;
                display: flex;
                align-items: center;
                justify-content: center;
            `;

            // 弹窗HTML直接写在overlay内部
            overlay.innerHTML = `
                <div style="
                    background: white;
                    border-radius: 16px;
                    padding: 40px;
                    max-width: 420px;
                    width: 90%;
                    text-align: center;
                    box-shadow: 0 25px 80px rgba(0, 0, 0, 0.4);
                    animation: modalIn 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
                    position: relative;
                    z-index: 10000;
                ">
                    <div style="width: 72px; height: 72px; background: linear-gradient(135deg, #4F46E5, #7C3AED); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px; box-shadow: 0 8px 24px rgba(79, 70, 229, 0.4);">
                        <svg width="36" height="36" fill="white" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                    </div>
                    <h3 style="font-size: 22px; font-weight: 700; color: #1a1a2e; margin: 0 0 12px;">提交成功</h3>
                    <p style="font-size: 15px; color: #555; line-height: 1.6; margin: 0 0 28px;">${message}</p>
                    <button class="modal-close-btn" style="
                        background: linear-gradient(135deg, #4F46E5, #7C3AED);
                        color: white;
                        border: none;
                        padding: 14px 40px;
                        border-radius: 10px;
                        font-size: 15px;
                        font-weight: 600;
                        cursor: pointer;
                        transition: all 0.2s;
                        box-shadow: 0 4px 16px rgba(79, 70, 229, 0.35);
                    ">知道了</button>
                </div>
            `;

            document.body.appendChild(overlay);

            // 关闭按钮
            overlay.querySelector('.modal-close-btn').addEventListener('click', () => {
                overlay.remove();
            });
            overlay.addEventListener('click', (e) => {
                if (e.target === overlay) overlay.remove();
            });
        }
    };

    // 添加 toast 动画样式
    const toastStyle = document.createElement('style');
    toastStyle.textContent = `
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateX(-50%) translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateX(-50%) translateY(0);
            }
        }
        @keyframes fadeOutDown {
            from {
                opacity: 1;
                transform: translateX(-50%) translateY(0);
            }
            to {
                opacity: 0;
                transform: translateX(-50%) translateY(20px);
            }
        }
        @keyframes modalIn {
            from {
                opacity: 0;
                transform: scale(0.9);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
    `;
    document.head.appendChild(toastStyle);

    // ========================================
    // 视频播放按钮
    // ========================================
    
    const VideoPlayer = {
        init() {
            const playBtn = document.querySelector('.play-btn');
            if (!playBtn) return;

            playBtn.addEventListener('click', () => {
                this.showToast('视频播放功能演示');
            });
        },

        showToast(message) {
            SidebarTools.showToast(message);
        }
    };

    // ========================================
    // 产品卡片链接
    // ========================================
    
    const ProductLinks = {
        init() {
            document.querySelectorAll('.product-link').forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    SidebarTools.showToast('即将跳转到详情页面');
                });
            });
        }
    };

    // ========================================
    // ========================================
    // 表单提交处理（联系表单）
    // ========================================

    const FormContact = {
        init() {
            const form = document.getElementById('contactForm');
            if (!form) return;

            form.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.handleSubmit(form);
            });
        },

        async handleSubmit(form) {
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            const formData = new FormData(form);

            // 收集表单数据（字段名与 Worker 保持一致）
            const data = {
                name: formData.get('name'),
                phone: formData.get('phone'),
                company: formData.get('company') || '',
                scenario: formData.get('scene') || '未选择',
                message: formData.get('message'),
                // 额外字段也保留
                industry: formData.get('industry') || '未选择',
                budget: formData.get('budget') || '未选择',
                timestamp: new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' })
            };

            // 验证
            if (!data.name || !data.phone || !data.message) {
                SidebarTools.showToast('请填写必填项');
                return;
            }

            // 禁用按钮，显示loading
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span>提交中...</span>';

            try {
                // 通过 Worker 转发到 Resend（绕过 CORS）
                const resendRes = await fetch('https://form.videotvai.com', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: data.name,
                        phone: data.phone,
                        company: data.company,
                        scenario: data.scenario,
                        message: `行业：${data.industry}\n预算：${data.budget}\n\n${data.message}`
                    })
                });

                if (!resendRes.ok) {
                    const errText = await resendRes.text();
                    console.error('Resend API error:', errText);
                    throw new Error('邮件发送失败');
                }

                SidebarTools.showSuccessModal('感谢您的咨询提交，VideoTV团队将会尽快与您联系，请保持手机畅通');
                form.reset();
            } catch (error) {
                console.error('表单提交错误:', error);
                // 备用 mailto 方案
                const subject = encodeURIComponent(`【VideoTV咨询】${data.name} - ${data.company}`);
                const body = encodeURIComponent(
                    `姓名：${data.name}\n公司：${data.company}\n电话：${data.phone}\n行业：${data.industry}\n场景：${data.scenario}\n预算：${data.budget}\n需求：${data.message}\n时间：${data.timestamp}`
                );
                SidebarTools.showSuccessModal('感谢您的咨询提交，VideoTV团队将会尽快与您联系，请保持手机畅通');
                setTimeout(() => { window.location.href = `mailto:business@videotvai.com?subject=${subject}&body=${body}`; }, 800);
            } finally {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
            }
        }
    };

    // ========================================
    // FAQ 折叠功能
    // ========================================

    const FaqAccordion = {
        init() {
            const faqItems = document.querySelectorAll('.faq-item');
            if (faqItems.length === 0) return;

            faqItems.forEach(item => {
                item.addEventListener('click', () => {
                    const isOpen = item.classList.contains('open');

                    // 关闭所有
                    faqItems.forEach(i => i.classList.remove('open'));

                    // 如果之前没有打开，则打开当前
                    if (!isOpen) {
                        item.classList.add('open');
                    }
                });
            });

            // 默认展开第一个
            if (faqItems.length > 0) {
                faqItems[0].classList.add('open');
            }
        }
    };

    // ========================================
    // 页面加载完成后初始化
    // ========================================

    function init() {
        MobileMenu.init();
        HeaderScroll.init();
        CountUpAnimation.init();
        TabSwitcher.init();
        SmoothScroll.init();
        ScrollReveal.init();
        ButtonEffects.init();
        SidebarTools.init();
        VideoPlayer.init();
        ProductLinks.init();
        FormContact.init();
        FaqAccordion.init();

        console.log('🎉 VideoTV 官网脚本加载完成！');
    }

    // DOM 加载完成后初始化
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // ========================================
    // 移动端底部留资浮条
    // ========================================
    (function initMobileCTA() {
        function createMobileCTA() {
            // 不显示在 contact 页面和 admin 页面
            var path = window.location.pathname;
            if (path.indexOf('/contact') !== -1 || path.indexOf('/admin') !== -1) return;

            // 确定 about#contact 链接路径
            var contactHref = path.indexOf('/blog/') !== -1 ? '../about.html#contact' : 'about.html#contact';

            var bar = document.createElement('div');
            bar.id = 'mobile-cta-bar';
            bar.innerHTML = '<a href="' + contactHref + '" class="mobile-cta-btn">' +
                '<span class="mobile-cta-icon">💬</span>' +
                '<span class="mobile-cta-text">免费获取方案</span>' +
                '<span class="mobile-cta-arrow">→</span>' +
                '</a>';

            document.body.appendChild(bar);

            // CSS 注入
            var style = document.createElement('style');
            style.textContent = [
                '#mobile-cta-bar {',
                '  display:none;',
                '  position:fixed; bottom:0; left:0; right:0; z-index:9999;',
                '  padding:8px 16px; padding-bottom:max(8px, env(safe-area-inset-bottom));',
                '  background:#534AB7;',
                '  box-shadow:0 -2px 12px rgba(83,74,183,0.3);',
                '}',
                '.mobile-cta-btn {',
                '  display:flex; align-items:center; justify-content:center; gap:8px;',
                '  background:#fff; color:#534AB7;',
                '  padding:12px 20px; border-radius:10px;',
                '  text-decoration:none; font-weight:600; font-size:15px;',
                '  transition:transform 0.15s, box-shadow 0.15s;',
                '  box-shadow:0 2px 8px rgba(0,0,0,0.1);',
                '}',
                '.mobile-cta-btn:active { transform:scale(0.97); }',
                '.mobile-cta-arrow { font-size:18px; }',
                '@media (max-width: 768px) {',
                '  #mobile-cta-bar { display:block; }',
                '  body { padding-bottom:80px !important; }',
                '}',
            ].join('\n');
            document.head.appendChild(style);
        }

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', createMobileCTA);
        } else {
            createMobileCTA();
        }
    })();

})();
