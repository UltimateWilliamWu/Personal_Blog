---
title: Financial Statement Analysis
tags:
  - CFA
  - CFA/L1
  - CFA/L1/FSA
---

# 03 · Financial Statement Analysis

← [[CFA Program]] · **权重 11–14%**（约 20–25 题） · **一轮配时 33h** · **W4–W6**

> 🚨 **这是整个计划的重心。你会计零基础，而 FSA 是三个科目的地基。**
> FSA 学扎实 → Corporate Issuers 和 Equity 的估值部分会顺很多。
> FSA 学崩 → 连带丢掉三个科目，总权重接近 30%。
>
> **W4 的目标不是刷进度，是把「三张表怎么勾稽」彻底搞懂。** 这一周慢一点没关系，后面会加倍还回来。

---

## 🧱 W4 地基：零基础必须先建立的四个直觉

在碰任何 module 之前，先把这四件事搞清楚。这不是考点，是**理解所有考点的前提**。

1. **会计恒等式**：`Assets = Liabilities + Equity`。任何一笔交易都必须让等式两边同时变，这是复式记账的全部秘密。
2. **三张表的勾稽**：
   - Income Statement 的 **Net Income** → 流入 Balance Sheet 的 **Retained Earnings**
   - Cash Flow Statement 的 **期末现金** = Balance Sheet 的 **Cash**
   - CFO 的间接法起点就是 **Net Income**
   → 三张表不是三份独立报告，是同一件事的三个切面。
3. **权责发生制 vs. 收付实现制（accrual vs. cash）**：利润表按**权责发生制**（赚到就确认，不管收没收到钱），现金流量表按**收付实现制**。**两者的差额全部体现在资产负债表的应收/应付/存货等科目变动上** —— 这句话是 FSA 一半考点的来源。
4. **利润可以操纵，现金难以操纵**：所以有 Financial Reporting Quality 这个 module，所以分析师看 CFO 和 Net Income 的背离。

> 💬 这四条如果有任何一条读完还是模糊的，**直接问我**，我从零讲。W4 卡住不要硬扛。

---

## 📋 Module 清单

> 按 2024+ curriculum 结构整理，**请对照 LES 实际章节勾选核对**。

**W4 · 地基 + 两张表**
- [ ] Introduction to Financial Statement Analysis
- [ ] Analyzing Income Statements
- [ ] Analyzing Balance Sheets

**W5 · 现金流 + 资产**
- [ ] Analyzing Statements of Cash Flows I
- [ ] Analyzing Statements of Cash Flows II
- [ ] Analysis of Inventories
- [ ] Analysis of Long-Term Assets

**W6 · 负债 + 质量 + 分析**
- [ ] Analysis of Income Taxes
- [ ] Topics in Long-Term Liabilities and Equity
- [ ] Financial Reporting Quality
- [ ] Financial Analysis Techniques
- [ ] Introduction to Financial Statement Modeling

---

## 🔥 高频考点

*（学到哪填到哪）*

**先埋几个确定的高频点：**

1. **存货 FIFO vs. LIFO** —— 必考。通胀环境下：LIFO → COGS 高、净利低、税低、期末存货低；FIFO 相反。以及 **LIFO reserve 换算成 FIFO** 的调整。（⚠️ **IFRS 禁止 LIFO**，只有 US GAAP 允许）
2. **CFO 间接法调整**：Net Income → 加回非现金费用（折旧摊销）→ 剔除投资/筹资性损益 → 调整营运资本变动。**方向记法**：经营性资产增加 → 减；经营性负债增加 → 加。
3. **递延所得税 DTA / DTL** 的产生原因：会计利润与应税利润的**暂时性差异**。加速折旧（税法）→ 前期税低 → 产生 **DTL**。
4. **折旧方法的影响**：直线 vs. 加速（DDB）对早期净利、ROA、资产周转率的影响方向。
5. **资本化 vs. 费用化**：资本化 → 当期利润高、资产高、CFO 高（因为支出计入 CFI）、后期利润低。这是最典型的「操纵」手段。
6. **比率分析**：DuPont 三步/五步分解、流动性/偿债/盈利/营运效率四大类比率的定义和方向。

---

## ⚠️ 易错点 / 陷阱

1. **IFRS vs. US GAAP 差异**是 FSA 的送命题库。做一张专门的对比表（LIFO、开发支出资本化、资产减值转回、存货计量、利息分类）。
2. **利息/股息在现金流量表的分类**：**IFRS 有选择权**（利息支付可 CFO 或 CFF；利息收到可 CFO 或 CFI），**US GAAP 是死的**（利息收付都在 CFO，股息支付在 CFF）。这题几乎每年考。
3. **「增加」到底加还是减**：应收账款增加 = 卖了货没收到钱 = **减** CFO。想不清就回到「现金到底动了没有」。
4. **资产减值**：IFRS 允许**转回**（除商誉），US GAAP **不允许转回**。
5. **稀释每股收益（diluted EPS）**：只有**摊薄性**（antidilutive 的要排除）证券才计入。转换后 EPS 反而变高的，直接不算。
6. **单位陷阱**：题干给 thousands 还是 millions，比率题里差一个数量级答案就全对不上。

---

## 📐 核心公式（先放框架，学到哪补到哪）

| 概念 | 公式 |
|---|---|
| 会计恒等式 | Assets = Liabilities + Equity |
| DuPont（三步） | $ROE = \dfrac{NI}{Sales} \times \dfrac{Sales}{Assets} \times \dfrac{Assets}{Equity}$ |
| DuPont（五步） | 税负担 × 息负担 × EBIT margin × 资产周转 × 权益乘数 |
| 存货恒等式 | 期初存货 + 购入 = COGS + 期末存货 |
| LIFO → FIFO 存货 | $Inv_{FIFO} = Inv_{LIFO} + \text{LIFO reserve}$ |
| 现金转换周期 | DSO + DOH − DPO |

---

## 🔗 关联

- 比率与资本结构 → [[Corporate Issuers]]
- 盈利质量与估值输入 → [[Equity Investments]]
- 信用分析用的比率 → [[Fixed Income]]
- 错题 → [[错题本]]
