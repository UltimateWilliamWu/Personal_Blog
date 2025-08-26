import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "William's Blog",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "quartz.jzhao.xyz",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },

    // 自定义 head 注入：多语言切换（支持 SPA）
    head: {
      scripts: [
        {
          inline: true,
          content: `
(function () {
  const KEY = 'blog.lang';
  const SUPPORTED = ['en', 'zh'];

  function getLang() {
    const saved = localStorage.getItem(KEY);
    if (saved && SUPPORTED.includes(saved)) return saved;
    const nav = (navigator.language || 'en').toLowerCase();
    return nav.startsWith('zh') ? 'zh' : 'en';
  }

  function setLang(lang) {
    if (!SUPPORTED.includes(lang)) lang = 'en';
    localStorage.setItem(KEY, lang);

    // 按钮高亮
    document.querySelectorAll('.i18n-toggle button').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // 内容切换（同一个 .i18n-block 中只显示当前语言）
    document.querySelectorAll('.i18n-block').forEach(block => {
      block.querySelectorAll('.i18n').forEach(node => {
        const show = node.classList.contains(lang);
        node.classList.toggle('i18n-hide', !show);
      });
    });
  }

  // 初始应用
  let current = getLang();
  function applyIfNeeded() {
    setLang(localStorage.getItem(KEY) || current);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyIfNeeded);
  } else {
    applyIfNeeded();
  }

  // 事件委托：一次绑定，适配 SPA
  document.addEventListener('click', (e) => {
    const target = e.target;
    if (target instanceof Element && target.matches('.i18n-toggle button')) {
      const lang = target.getAttribute('data-lang');
      if (lang) {
        current = lang;
        setLang(lang);
      }
    }
  });

  // 监听 DOM 变化（路由切换/重渲染）
  const obs = new MutationObserver((muts) => {
    for (const m of muts) {
      if (m.type === 'childList' && (m.addedNodes.length || m.removedNodes.length)) {
        applyIfNeeded();
        break;
      }
    }
  });
  obs.observe(document.documentElement, { childList: true, subtree: true });

  // 兜底：前端路由事件
  window.addEventListener('popstate', applyIfNeeded);
  window.addEventListener('hashchange', applyIfNeeded);
})();
          `,
        },
      ],
    },
  },

  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
