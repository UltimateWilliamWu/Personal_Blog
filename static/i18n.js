// static/i18n.js
(() => {
  if (window.__I18N_LOADED__) return;
  window.__I18N_LOADED__ = true;

  const KEY = "blog.lang";
  const SUPPORTED = ["en", "zh"];

  // 注入必要样式（确保 .i18n-hide 生效）
  function ensureStyle() {
    if (document.getElementById("i18n-style")) return;
    const style = document.createElement("style");
    style.id = "i18n-style";
    style.textContent = `
      .i18n-hide { display: none !important; }
    `;
    document.head.appendChild(style);
  }

  function getLang() {
    const saved = localStorage.getItem(KEY);
    if (saved && SUPPORTED.includes(saved)) return saved;
    const nav = (navigator.language || "en").toLowerCase();
    return nav.startsWith("zh") ? "zh" : "en";
  }

  function updateButtons(lang) {
    document.querySelectorAll(".i18n-toggle button").forEach((btn) => {
      btn.classList.toggle("active", btn.getAttribute("data-lang") === lang);
    });
  }

  function setLang(lang) {
    if (!SUPPORTED.includes(lang)) lang = "en";
    localStorage.setItem(KEY, lang);

    // 内容切换：每个 .i18n-block 内仅显示当前语言 .i18n.en / .i18n.zh
    document.querySelectorAll(".i18n-block").forEach((block) => {
      block.querySelectorAll(".i18n").forEach((node) => {
        const show = node.classList.contains(lang);
        node.classList.toggle("i18n-hide", !show);
      });
    });

    // 页面级标记（可用于全局样式/无障碍）
    document.documentElement.setAttribute("data-lang", lang);
    document.documentElement.lang = lang === "zh" ? "zh-CN" : "en";

    updateButtons(lang);
    console.log("[i18n] active ->", lang);
  }

  function applyCurrent() {
    setLang(localStorage.getItem(KEY) || getLang());
  }

  // 初始化
  function init() {
    ensureStyle();
    applyCurrent();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }

  // 点击切换（事件委托，兼容 SPA）
  document.addEventListener("click", (e) => {
    const btn = e.target.closest && e.target.closest(".i18n-toggle button");
    if (!btn) return;
    const lang = btn.getAttribute("data-lang");
    if (lang) setLang(lang);
  });

  // 监听 DOM 变化（路由切换/重新渲染）
  const obs = new MutationObserver(() => applyCurrent());
  obs.observe(document.documentElement, { childList: true, subtree: true });

  window.addEventListener("popstate", applyCurrent);
  window.addEventListener("hashchange", applyCurrent);
})();
