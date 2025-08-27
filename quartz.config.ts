import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 * See https://quartz.jzhao.xyz/configuration for more information.
 */

// ==== 固定站点信息（不依赖 NODE_ENV）====
const GH_USER = "UltimateWilliamWu"       // 你的 GitHub 用户名
const REPO = "Personal_Blog"              // 你的仓库名（项目页）
const PROD_BASE = `https://${GH_USER}.github.io/${REPO}`

// 本地开发地址（Quartz 预览）
const DEV_BASE = "http://localhost:8080"

// 写死线上前缀，保证 Pages 一定能加载；本地用无前缀
const PROD_PREFIX = `/${REPO}`
const DEV_PREFIX = ""                     // 本地 dev 不带仓库前缀

// 给外链脚本加个版本参数，避免缓存
const VER = "v20250829"

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

    // ✅ baseUrl 必须是完整可访问地址（线上/本地二选一，Quartz 只用来生成链接）
    // 你如果经常本地预览，就先用 DEV_BASE；要发布前改成 PROD_BASE。
    // 也可以一直留成 PROD_BASE，不影响本地 dev。
    baseUrl: "https://ultimatewilliamwu.github.io/Personal_Blog",

    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",

    // ✅ 这里同时加“线上用的带仓库前缀脚本”和“本地开发的无前缀脚本”
    // 任意一个加载成功即可；为避免重复执行，建议在 i18n.js 开头加：
    //   if (window.__I18N_LOADED__) { console.debug("i18n already loaded"); } else { window.__I18N_LOADED__ = true; /* 原逻辑 */ }
    head: {
      scripts: [
        // 线上（GitHub Pages 项目页）
        //{ src: `${PROD_PREFIX}/static/i18n.js?${VER}`, defer: true },
	{ src: "/Personal_Blog/static/i18n.js?v=20250831", defer: true },
       ],
    },

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
  },

  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: { light: "github-light", dark: "github-dark" },
        keepBackground: false,
      }),
      // 禁用 Markdown 内联 <script>（外链不受影响）
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
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: true }),
      Plugin.Assets(),
      Plugin.Static(),     // ✅ 会把 根目录 static/ 拷到 public/static/
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
