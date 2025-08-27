import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"
// 用于声明自定义 transformer 的类型
import type { QuartzTransformerPlugin } from "./quartz/plugins/types"

/** ====== 常量（按需改） ====== */
// 你的仓库是 GitHub Pages “项目页”，前缀必须带仓库名
const REPO_PREFIX = "/Personal_Blog"
// 每次改 static/i18n.js 时，改这里的版本号防缓存
const I18N_VER = "v20250831"

/** 极简注入插件：把外链 JS 注入到页面（DOM Ready 后执行） */
const InjectI18n: QuartzTransformerPlugin<{ src: string }> = (opts) => ({
  name: "InjectI18n",
  externalResources() {
    return {
      js: [
        {
          src: opts!.src,          // 形如 "/Personal_Blog/static/i18n.js?v=xxxx"
          loadTime: "afterDOMReady",
          contentType: "external",
          module: false,
        },
      ],
    }
  },
})

/** ====== 你的站点配置 ====== */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "William's Blog",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: { provider: "plausible" },
    locale: "en-US",

    // 官方建议 baseUrl 用 “域名/子路径” 不带协议
    // 对应实际站点 https://ultimatewilliamwu.github.io/Personal_Blog
    baseUrl: "ultimatewilliamwu.github.io/Personal_Blog",

    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",

    // ⚠️ 不要放 head.scripts；Quartz v4 不识别该字段
    // head: { scripts: [...] },

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
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "git", "filesystem"] }),
      Plugin.SyntaxHighlighting({
        theme: { light: "github-light", dark: "github-dark" },
        keepBackground: false,
      }),
      // 保持禁用 Markdown 内联脚本，避免解析报错
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),

      // ✅ 把 i18n.js 注入到每个页面（仓库前缀 + 版本号）
      InjectI18n({ src: `${REPO_PREFIX}/static/i18n.js?${I18N_VER}` }),
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
      Plugin.Static(),     // 会把 根目录 static/ 拷到 public/static/
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
