# 本库写作规范（Claude 必读）

这个目录是 **Quartz 博客的 `content/`**，不只是 Obsidian 库。
所有笔记会经 **remark-math** 渲染发布 —— **remark-math 比 Obsidian 严格得多**。

> ⚠️ **核心原则：按 remark-math 的规矩写。** Obsidian 能渲染 ≠ 发布出来能渲染。

---

## 🔢 数学公式写法（最容易踩）

### ① 块级 `$$` 必须独占一行

**尤其是带 `\tag{}` 的 —— 单行写法在 remark-math 下会挂。**

✅ **正确**

```markdown
$$
E = mc^2 \tag{1}
$$
```

❌ **错误**

```markdown
$$E = mc^2 \tag{1}$$
```

> 前者在 Obsidian 里同样是推荐写法，**两边都正常**。所以**一律用多行写法**，不要图省事。

### ② 引用块 / 列表内同理 —— 前缀要带上

引用块里也要让 `$$` 独占一行，**每行都带 `> `**：

```markdown
> 说明文字：
>
> $$
> R = \frac{P_1 - P_0}{P_0}
> $$
```

列表项内的公式，**三行保持相同缩进**（list continuation）：

```markdown
- **First moment (Mean):**
    $$
    \mu_i = \frac{1}{N}\sum f_{ij}
    $$
```

### ③ 行内公式用单 `$`，块级一律用 `$$`

不要用 `\[ \]` 或 `\( \)`。

### ✅ 全库检查命令

```bash
cd content && grep -rn '\$\$.*\$\$' --include="*.md" . | grep -v '^\./\.'
```

**任何命中都是待修的**（`CLAUDE.md` 里的反例、`Excalidraw/` 数据文件除外）。

> 📌 **2026-07-31 已做过一次全库清理**：修复 **135 处 / 20 个文件**（CFA 笔记 79 处，UNSW 笔记 56 处）。
> 修复脚本在 `content/.claudian/fix_math_apply.py`（`--apply` 写入，默认 dry-run）。
> ⚠️ `.claudian/` 是 gitignored 的，`git clean -xdf` 会删掉脚本。

---

## 📁 CFA 笔记结构约定

### 目录

官方教材是 **lesson 粒度**（`1.02`、`1.03`…），所以**每个 module 是一个文件夹**：

```
M1 Rates and Returns/          ← 文件夹
├── M1 Rates and Returns.md    ← folder note（同名）：导航 + 考点优先级 + 易错点总清单
├── 1.01 Introduction.md       ← 一篇一个 lesson
├── 1.02 ....md
└── ...
```

**folder note 用与文件夹同名的写法**，与 `01 Quantitative Methods/Quantitative Methods.md` 惯例一致（make-md 可识别）。

### 单篇 lesson 笔记的标准结构

```
# 1.0X | 官方标题
← 导航行
> 一句话概括 + 考法定位

## 📖 LOS（官方学习目标）

# Part 1 · 原文翻译      ← 忠实翻译，保留官方措辞的精确限定词
# Part 2 · 概念详解      ← 直觉、动手算、考法、陷阱

## ⚠️ 易错点清单
## 🔗 关联
```

**模板参照** `1.02 Interest Rates and Time Value of Money.md` 和 `1.03 Rates of Return.md`。

### 内容准则

- **中文讲解，术语 / 公式 / 选项关键词一律保留英文原文**
- Part 1 **只翻译**，不掺解释；官方的**限定词**（*expected*、*at the contracted time*、*nearest observations*）是考点，必须保留
- Part 2 才展开：直觉、为什么、动手算、考法、易错
- **官方给的例题（Example N）默认只译题目，不给答案** —— 留作练习，除非用户明确要答案
- 标题拿不准是否与官方一致时，**标 ⚠️ 注明是推测**，不要假装确定

---

## 🧭 IT/ 知识体系目录（方案 D · tag 驱动）

`IT/` 是**体系导航层**，**不放具体内容**。每页只写三样东西：

1. **依赖关系图** —— 谁是谁的前置（tag 页给不了的价值）
2. **`#Topic/X` 内联标签** —— Obsidian 可点、Quartz `TagPage()` 自动聚合
3. **状态与缺口标注**

> ⚠️ **新笔记只要打 `Topic/*` 标签就会自动出现在标签页，不需要回来改 IT/ 索引。**
> IT/ 只在「新增主题」或「学习路径变化」时才动。

### ⬜ 占位页 ≠ 断链（**重要，别再误判**）

库里有大量**内容为空但有意保留的占位页**，它们是**规划提纲**，不是缺陷：

| 例子 | 性质 |
|---|---|
| `IT/Java/` 下的 JavaEE / JavaWeb / SSM / SpringBoot / SpringCloud / JVM | Java **自建学习路线**的 7 个模块，按序填充中（1/7） |
| `IT/Operating Systems/`、`IT/Blockchain.md` | 体系里有、UNSW 没修课，保留作后续提纲 |

**不要**把它们描述成「残缺」「无内容」「应该删掉」。用状态标记：

| 标记 | 含义 |
|---|---|
| ✅ | 已写 |
| 🔄 | 进行中 |
| 🟡 | 少量 / 零散 |
| ⬜ | **已建页占位，内容待写** |

### 两个维度

```
IT/                ← 学科视角，跨课程聚合
      ↕  靠 Topic/* 标签打通
UNSW/index         ← 课程视角，按学期原样
```

同一篇笔记同时出现在两边，**不复制内容，不手工同步**。

---

## 🗺 路径

- 顶层是 `Work/`（**不是** `Interview/`，已改名）
- CFA 主索引：`Work/CFA Program/CFA Program.md`
- 学科索引：`Work/CFA Program/01 Quantitative Methods/Quantitative Methods.md`

---

## ⚠️ 操作注意

- **不要在 Bash 里 `cd`** —— 工作目录会持续影响后续工具调用的相对路径，之前因此在错误位置建过嵌套目录树。用绝对路径。
- `content/.claudian/` 已在 `.gitignore` 里，**对话记录不进 git、无备份**
- 用户会用 Obsidian 直接改名/移动文件，**动手前先确认当前路径**
