---
title: Portfolio Management
tags:
  - CFA
  - CFA/L1
  - CFA/L1/PM
---

# 09 · Portfolio Management

← [[CFA Program]] · **权重 8–12%**（约 14–22 题） · **一轮配时 5h** · **W13**

> 🎯 **定位**：又一个**高性价比科目**。数学部分（组合方差、CAPM、有效前沿）你在 [[Quantitative Methods]] 已经学过，
> 剩下的 IPS、行为偏差、风险管理都是概念题。5 小时足够，因为你的量化背景在这里可以直接迁移。

---

## 📋 Module 清单

> 按 2024+ curriculum 结构整理，**请对照 LES 实际章节勾选核对**。

- [ ] Portfolio Management: An Overview
- [ ] Portfolio Risk and Return: Part I
- [ ] Portfolio Risk and Return: Part II
- [ ] Basics of Portfolio Planning and Construction（IPS）
- [ ] The Behavioral Biases of Individuals
- [ ] Introduction to Risk Management

---

## 🔥 高频考点

*（学到哪填到哪）*

1. **CML vs. SML** —— 必考对比。
   - **CML**：横轴是**总风险 σ**，只对**有效组合**成立，斜率 = Sharpe ratio
   - **SML**：横轴是**系统性风险 β**，对**所有资产**成立（包括单个证券），这就是 CAPM
   → 混淆这两条线是 PM 第一大失分点。
2. **系统性风险 vs. 非系统性风险**：分散化只能消除非系统性风险；**市场只为系统性风险付酬**，所以 CAPM 里只有 β。
3. **有效前沿 / 最优组合**：加入无风险资产后，所有投资者持有同一个**市场组合**，只是杠杆比例不同（**两基金分离定理**）。
4. **IPS 的构成**：Return objective / Risk tolerance（willingness vs. ability，**取较低者**）/ 五大约束 **TTLLU**（Time horizon、Taxes、Liquidity、Legal、Unique circumstances）。
5. **行为偏差**：认知错误（cognitive errors，可通过教育纠正）vs. 情绪偏差（emotional biases，只能适应）—— 这个二分法必考。
6. **绩效评价指标**：Sharpe / Treynor / Jensen's alpha / M² 的分母分别是什么。

---

## ⚠️ 易错点 / 陷阱

1. **Sharpe 用 σ（总风险），Treynor 用 β（系统性风险）**。分母记反是高频错。评价**充分分散**的组合用 Treynor，评价**不完全分散**的组合用 Sharpe。
2. **风险承受力：willingness vs. ability 冲突时取较低者**，然后教育客户。题干经常设计成「他说自己很激进（willingness 高），但他 60 岁且是唯一收入来源（ability 低）」→ 答案是保守。
3. **组合标准差不是加权平均**。只有 ρ = +1 时才等于加权平均，其余情况都更小（这就是分散化的来源）。
4. **β = 1 不代表无风险**，代表与市场同步。β = 0 才是无系统性风险。
5. **Cognitive vs. Emotional 的归类**：confirmation bias、anchoring、availability → 认知；loss aversion、overconfidence、regret aversion、endowment → 情绪。列一张表背。

---

## 📐 核心公式

| 概念 | 公式 |
|---|---|
| 组合期望收益 | $E(R_p) = \sum w_i E(R_i)$ |
| 两资产组合标准差 | $\sigma_p = \sqrt{w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\rho_{12}\sigma_1\sigma_2}$ |
| CAPM / SML | $E(R_i) = R_f + \beta_i[E(R_m) - R_f]$ |
| Beta | $\beta_i = \dfrac{Cov(R_i, R_m)}{\sigma_m^2} = \rho_{i,m}\dfrac{\sigma_i}{\sigma_m}$ |
| Sharpe Ratio | $\dfrac{R_p - R_f}{\sigma_p}$ |
| Treynor Ratio | $\dfrac{R_p - R_f}{\beta_p}$ |
| Jensen's Alpha | $\alpha_p = R_p - [R_f + \beta_p(R_m - R_f)]$ |
| CML | $E(R_p) = R_f + \dfrac{E(R_m) - R_f}{\sigma_m}\sigma_p$ |

---

## 🔗 关联

- 组合数学 / 相关性 → [[Quantitative Methods]]
- CAPM 用于折现率 → [[Corporate Issuers]]、[[Equity Investments]]
- 分散化与另类资产 → [[Alternative Investments]]
- 错题 → [[错题本]]
