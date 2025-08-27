import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"
// 新增：引入类型
import type { QuartzTransformerPlugin } from "./quartz/plugins/types"

// ========= 你的仓库信息 =========
const GH_USER = "UltimateWilliamWu"
const REPO = "Personal_Blog"
const VER  = "v20250831" // ← 改这个值可强制刷新缓存

// ✅ 内联一个极小的 transformer，用 externalResources 注入脚本
const InjectI18n: QuartzTransformerPlugin<{ version?: string }> = (opts) => {
  return {
    name: "InjectI18n",
    externalResources(ctx) {
      // 从 baseUrl 里解析出仓库前缀（/Personal_Blog）
      const cfg = ctx.cfg.configuration
      const prefix = (() => {
        try { return new URL("https://" + (cfg.baseUrl ?? "")).pathname || "" }
        catch { return "" }
      })()

      const v = opts?.version ? `?${opts.version}` : ""
      return {
        js: [
          {
            // 一定要带仓库前缀，否则在 GitHub Pages 项目页会 404
            src: `${prefix}/static/i18n.js${v}`,
            loadTime: "afterDOMReady",   // 页面加载完成后执行
            contentType: "external",     // 外链脚本
            module: false,
          },
        ],
      }
    },
  }
}

const config: QuartzConfig = {
  configuration: {
    pageTitle: "William's Blog",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: { provider: "plausible" },
    locale: "en-US",

    // ✅ 官方建议：不带协议，且包含仓库子路径
    // https://ultimatewilliamwu.github.io/Personal_Blog  ->  ultimatewilliamwu.github.io/Personal_Blog
    baseUrl: `${GH_USER}.github.io/${REPO}`,

    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",

    // ⚠️ 删掉原来的 head.scripts，这里本就不会生效
    // head: { scripts: [...] },

    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: { /* ……保持你的原配置不变…… */ },
    },
  },

  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "git", "filesystem"] }),
      Plugin.SyntaxHighlighting({ theme: { light: "github-light", dark: "github-dark" }, keepBackground: false }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),

      // ✅ 在末尾加上我们注入脚本的插件
      InjectI18n({ version: VER }),
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
      Plugin.Static(),     // 会把根目录 static/ 拷到 public/static/
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
