import fs from "fs"
import path from "path"

const CONTENT = "content"
const SKIP = new Set([".obsidian", ".trash", ".makemd", ".space", ".claudian",
  "node_modules", ".venv", "datasets", "target", ".pytest_cache", "__pycache__", ".ipynb_checkpoints"])

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (SKIP.has(e.name)) continue
    const p = path.join(dir, e.name)
    if (e.isDirectory()) walk(p, out)
    else if (e.name.endsWith(".md")) out.push(p)
  }
  return out
}

let totalB = 0, totalA = 0
for (const f of walk(CONTENT)) {
  const lines = fs.readFileSync(f, "utf8").split("\n")
  const hits = []

  // Class B: a '>$$' block whose body has a line without the '>' prefix
  let inQuoteMath = false, openLine = 0
  for (let i = 0; i < lines.length; i++) {
    const raw = lines[i]
    const isQuoted = /^\s*>/.test(raw)
    const stripped = raw.replace(/^\s*>\s?/, "").trim()
    if (!inQuoteMath && isQuoted && stripped === "$$") { inQuoteMath = true; openLine = i + 1; continue }
    if (inQuoteMath) {
      if (isQuoted && stripped === "$$") { inQuoteMath = false; continue }
      if (!isQuoted && raw.trim() !== "") {
        hits.push({ cls: "B", line: i + 1, openLine, text: raw })
        totalB++
      }
    }
  }

  // Class A: single-line $$...$$ containing \tag
  lines.forEach((l, i) => {
    const m = l.match(/\$\$(.+?)\$\$/)
    if (m && m[1].includes("\\tag")) { hits.push({ cls: "A", line: i + 1, text: m[1] }); totalA++ }
  })

  if (hits.length) {
    console.log("=".repeat(96))
    console.log(f.replace(/\\/g, "/"))
    hits.sort((a, b) => a.line - b.line).forEach((h) => {
      if (h.cls === "B") console.log(`  [B] L${h.line}  blockquote 公式块(开于 L${h.openLine})中缺 '>' 的行:\n        ${JSON.stringify(h.text).slice(0, 92)}`)
      else console.log(`  [A] L${h.line}  单行 $$..\\tag..$$:\n        ${JSON.stringify(h.text).slice(0, 92)}`)
    })
  }
}
console.log(`\n合计: A 类(单行 $$ + \\tag) ${totalA} 处 | B 类(blockquote 内缺 '>') ${totalB} 处`)
