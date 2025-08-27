// /public/i18n.js
console.log("[i18n] file loaded");

(function () {
  const KEY = "blog.lang";
  const SUPPORTED = ["en", "zh"];

  function getLang() {
    const saved = localStorage.getItem(KEY);
    if (saved && SUPPORTED.includes(saved)) return saved;
    const nav = (navigator.language || "en").toLowerCase();
    return nav.startsWith("zh") ? "zh" : "en";
  }

  function setLang(lang) {
    if (!SUPPORTED.includes(lang)) lang = "en";
    localStorage.setItem(KEY, lang);

    // 按钮高亮
    document.querySelectorAll(".i18n-toggle button").forEach((btn) => {
      btn.classList.toggle("active", btn.getAttribute("data-lang") === lang);
    });

    // 内容切换：每个 .i18n-block 内只显示当前语言
    document.querySelectorAll(".i18n-block").forEach((block) => {
      block.querySelectorAll(".i18n").forEach((node) => {
        const show = node.classList.contains(lang);
        node.classList.toggle("i18n-hide", !show);
      });
    });

    console.log(
      "[i18n] setLang ->",
      lang,
      "blocks:",
      document.querySelectorAll(".i18n-block").length
    );
  }

  // 初始应用
  let current = getLang();
  function applyIfNeeded() {
    setLang(localStorage.getItem(KEY) || current);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyIfNeeded);
  } else {
    applyIfNeeded();
  }

  // 事件委托（适配 SPA）
  document.addEventListener("click", (e) => {
    const t = e.target;
    if (t instanceof Element && t.matches(".i18n-toggle button")) {
      const lang = t.getAttribute("data-lang");
      console.log("[i18n] click ->", lang);
      if (lang) {
        current = lang;
        setLang(lang);
      }
    }
  });

  // 监听 DOM 变化（路由切换/页面重渲染）
  const obs = new MutationObserver((muts) => {
    for (const m of muts) {
      if (
        m.type === "childList" &&
        (m.addedNodes.length || m.removedNodes.length)
      ) {
        console.log("[i18n] mutation -> reapply");
        applyIfNeeded();
        break;
      }
    }
  });
  obs.observe(document.documentElement, { childList: true, subtree: true });

  // 兜底：前端路由事件
  window.addEventListener("popstate", applyIfNeeded);
  window.addEventListener("hashchange", applyIfNeeded);
})();
