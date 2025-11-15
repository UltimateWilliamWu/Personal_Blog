---
title: Home
---

# 🌐 Welcome 欢迎光临
---

✨ This is my personal blog, where I share notes on AI/ML, quant finance projects, and personal reflections.  
这是我的个人博客，在这里我会分享人工智能、量化金融项目和个人感悟。
<!-- ✅ 直接把这一整段粘到你的首页简介位置（如 index.md 里用原生 HTML 块）
     作用：一个切换按钮 + 简介内容的中英文切换
     特点：
       - 无需建立 en/zh 子目录
       - 纯前端切换，不改路由
       - 记忆上次选择（localStorage）
       - 自动按浏览器语言第一次加载时选择
-->

<style>
  .i18n-toggle {
    display: inline-flex; align-items: center; gap: .5rem;
    border: 1px solid var(--lightgray, #ddd); border-radius: 999px;
    padding: .25rem .6rem; font-size: .92rem; cursor: pointer;
    user-select: none; backdrop-filter: blur(6px);
  }
  .i18n-toggle button {
    border: none; background: transparent; padding: .25rem .5rem; cursor: pointer;
    opacity: .7;
  }
  .i18n-toggle button.active { opacity: 1; font-weight: 700; text-decoration: underline; }
  .i18n-hide { display:none !important; }
  .intro-card { 
    border: 1px solid var(--lightgray, #e6e6e6); border-radius: 12px; padding: 16px; 
    box-shadow: 0 4px 16px rgba(0,0,0,.04);
  }
</style>

<div id="intro-i18n" class="intro-card">
  <!-- 切换按钮（你也可以把这段放到导航栏） -->
  <div class="i18n-toggle" role="group" aria-label="Language Switch">
    <span style="font-size:.9rem;opacity:.7">Language</span>
    <button type="button" data-lang="en" class="active">EN</button>
    <span>｜</span>
    <button type="button" data-lang="zh">中文</button>
  </div>

  <!-- 内容块：在同一位置放两份文本，用类名区分语言 -->
  <div class="i18n-block" data-key="intro">
    <div class="i18n en">
      <h2>Hi, I’m William Wu 👋</h2>
      <p>
        Welcome to my personal blog. I’m a CS/AI student working on machine learning, 
        reinforcement learning and applied systems. Here I share course notes, project write-ups, and occasional market/quant thoughts.
      </p>
      <ul>
        <li>Current focus: <strong>FinMem</strong> (LLM + memory for time series)</li>
        <li>Course notes: <strong>UNSW Master IT (AI direction)</strong></li>
        <li>Hobbies: 🏃‍♂️ gaming, 📷 notes design</li>
      </ul>
    </div>
    <div class="i18n zh i18n-hide">
      <h2>你好，我是William Wu 👋</h2>
      <p>
        欢迎来到我的个人博客。我主要研究机器学习、强化学习与应用系统。
        在这里，你可以看到：
      </p>
      <ul>
        <li>学习与笔记：<strong>UNSW</strong>学校课程、机器学习、人工智能、数据结构等</li>
        <li>项目记录：医疗信息系统<strong>HIS</strong>、基于<strong>Qlib</strong>的量化策略研究</li>
        <li>经验分享：学习技巧、编程心得、工具配置等</li>
	    <li>成长与随想：一些生活感悟与灵感记录</li>
      </ul>
    </div>
  </div>

  <!-- 你可以复制更多块，只要加 data-key 不同即可（例如 about, contact 等） -->
  <div class="i18n-block" data-key="contact" style="margin-top:12px">
    <div class="i18n en">
      <h3>Contact</h3>
      <p>Email: <a href="mailto:you@example.com">william-wu2001@outlook.com</a> · GitHub: <a href="https://github.com/UltimateWilliamWu">@WilliamWu</a></p>
    </div>
    <div class="i18n zh i18n-hide">
      <h3>联系我</h3>
      <p>邮箱：<a href="mailto:you@example.com">william-wu2001@outlook.com</a> · GitHub：<a href="https://github.com/UltimateWilliamWu">@WilliamWu</a></p>
    </div>
  </div>
</div>



