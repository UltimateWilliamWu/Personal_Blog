---
title: Equity Investments
tags:
  - CFA
  - CFA/L1
  - CFA/L1/Equity
---

# 05 · Equity Investments

← [[CFA Program]] · **权重 11–14%**（约 20–25 题） · **一轮配时 22h** · **W8–W9**

> 🎯 **定位**：前半段（市场机制、指数、有效市场）是**概念送分题**，背熟即得分；
> 后半段（估值）是**计算题**，DDM / FCFE / 乘数三块必须练到自动化。
> 你有交易系统的实操背景，市场机制那块会比一般考生轻松。

---

## 📋 Module 清单

> 按 2024+ curriculum 结构整理，**请对照 LES 实际章节勾选核对**。

**W8 · 市场与效率**
- [ ] Market Organization and Structure
- [ ] Security Market Indexes
- [ ] Market Efficiency
- [ ] Overview of Equity Securities

**W9 · 分析与估值**
- [ ] Industry and Competitive Analysis
- [ ] Company Analysis: Past and Present
- [ ] Company Analysis: Forecasting
- [ ] Equity Valuation: Concepts and Basic Tools（DDM / FCFE / 乘数）

---

## 🔥 高频考点

*（学到哪填到哪）*

1. **三种指数加权方式对比**：price-weighted（如 DJIA，高价股主导，拆股需调除数）、market-cap weighted（如 S&P 500，大市值主导，天然「追涨」）、equal-weighted（需定期再平衡，小盘股偏向）。**必考对比表**。
2. **市场有效性三种形式**：weak（历史价格已反映 → 技术分析无效）、semi-strong（公开信息已反映 → 基本面分析无效）、strong（含内幕信息 → 内幕交易也无效）。**考法**：给一个情景问「这与哪种形式一致/矛盾」。
3. **Gordon Growth Model (GGM)** 及其变形（求 P、求 r、求 g、求 terminal value）。
4. **Porter 五力** + 行业生命周期阶段特征。
5. **P/E 的 trailing vs. leading**、justified P/E 的推导（由 GGM 两边同除 E₁ 得到）。
6. **优先股 / 可转换优先股 / 库存股** 等权益证券类型的特征区分。

---

## ⚠️ 易错点 / 陷阱

1. **GGM 里的 D₁ 不是 D₀**。题干给「刚刚支付的股息 D₀」时必须先 `D₀ × (1+g)`。这是 Equity 第一大失分点。
2. **GGM 要求 r > g**，否则公式无意义。题目会用 `g > r` 的数据考你「为什么不能用 GGM」。
3. **Price-weighted 指数遇到拆股**：除数要调整，指数值本身不变。
4. **Justified P/E 用 leading**：$\dfrac{P_0}{E_1} = \dfrac{1-b}{r-g}$，分母是 E₁ 不是 E₀。
5. **Market-cap weighted 的偏向**：会自动超配「被高估」的股票（因为涨了权重就大），这是它的**理论缺陷**，常作为考点。
6. **EMH 与行为金融**：题干描述 momentum / overreaction 等异象时，问的往往是「这挑战了哪种形式的有效性」。

---

## 📐 核心公式

| 概念 | 公式 |
|---|---|
| Gordon Growth Model | $P_0 = \dfrac{D_1}{r - g} = \dfrac{D_0(1+g)}{r - g}$ |
| 可持续增长率 | $g = b \times ROE$（b = retention ratio = 1 − 派息率） |
| Justified leading P/E | $\dfrac{P_0}{E_1} = \dfrac{1 - b}{r - g}$ |
| Justified trailing P/E | $\dfrac{P_0}{E_0} = \dfrac{(1-b)(1+g)}{r - g}$ |
| FCFE 估值 | $P_0 = \dfrac{FCFE_1}{r - g}$ |
| 两阶段 DDM | 分段折现高增长期股息 + 折现 terminal value |

---

## 🔗 关联

- 估值输入（盈利、现金流质量）→ [[Financial Statement Analysis]]
- 折现率 / CAPM → [[Portfolio Management]]、[[Corporate Issuers]]
- 行业周期 → [[Economics]]
- 错题 → [[错题本]]
