import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 * See https://quartz.jzhao.xyz/configuration for more information.
 */

// === 环境&前缀（本地无前缀，GitHub 项目页自动加 /<repo>） ===
const isProd = process.env.NODE_ENV === "production"
const GH_USER = "UltimateWilliamWu"          // ← 改成你的 GitHub 用户名
const REPO = "Personal_Blog"                 // ← 若是用户主页，改成 ""（空串）

// 线上完整站点地址（非常重要）
const PROD_BASE =
  REPO && REPO.length > 0
    ? `https://${GH_USER}.github.io/${REPO}`
    : `https://${GH_USER}.github.io`

// 本地 / 线上 baseUrl
const baseUrl = isProd ? PROD_BASE : "http://localhost:8080"

// 静态资源与路由前缀
const prefix = isProd && REPO ? `/${REPO}` : ""

// 给外链脚本做个防缓存版本号
const VER = "v20250827"

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

    // ✅ 这里必须是完整的、可公开访问的站点地址
    baseUrl,

    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",

    // ⬇️ 在 <head> 里注入你的 i18n.js（自动带仓库前缀）
    head: {
      scripts: [
        { src: `${prefix}/static/i18n.js?${VER}`, defer: true },
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
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      // 禁用 Markdown 中的内联 <script>，外链 <script src="..."> 不受影响
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
      Plugin.ComponentResources(),  // quartz 内部静态资源
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),              // 处理 assets
      Plugin.Static(),              // ✅ 拷贝根目录 static/ → public/static/
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
