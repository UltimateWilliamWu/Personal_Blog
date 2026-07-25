---
title: Quantitative Methods
tags:
  - CFA
  - CFA/L1
  - CFA/L1/Quant
---

# 01 · Quantitative Methods

← [[CFA Program]] · **权重 6–9%**（约 11–16 题） · **一轮配时 11h** · **W1**

> 🎯 **你的定位**：这科对你是**复习不是学习**。概率、分布、假设检验、回归你在 ML 里天天用。
> 唯一要重新适应的是 **CFA 的表述习惯和计算器操作** —— 很多失分不是不会，是 `Sx` 按成 `σx`、P/Y 没设成 1。
> 所以 W1 的重点是：**快速过概念 + 大量刷题练手感**，不要在数学上恋战。

---

## 📋 Module 清单

> 按 2024+ curriculum 结构整理，**请对照 LES 实际章节勾选核对**。

- [ ] Rates and Returns
- [ ] Time Value of Money in Finance
- [ ] Statistical Measures of Asset Returns
- [ ] Probability Trees and Conditional Expectations
- [ ] Portfolio Mathematics
- [ ] Simulation Methods
- [ ] Estimation and Inference
- [ ] Hypothesis Testing
- [ ] Parametric and Non-Parametric Tests of Independence
- [ ] Simple Linear Regression
- [ ] Introduction to Big Data Techniques

---

## 🔥 高频考点

*（学到哪填到哪 —— 每个 module 学完提炼 3 条回填这里）*

**先埋几个我确定的高频点：**

1. **各种 return 的区分与计算**：holding period return / arithmetic mean / geometric mean / harmonic mean / money-weighted (IRR) / time-weighted。**必考，且必考「哪个更适合评价基金经理」→ time-weighted**（因为它剔除了申赎时点的影响，那不是经理能控制的）。
2. **年化与复利频率转换**：EAR = (1 + 定期利率)^m − 1；连续复利 EAR = e^r − 1。
3. **Hypothesis testing 的完整流程**：H₀/Hₐ 设定 → 选检验统计量 → 临界值 vs. p-value → 结论表述。**表述陷阱**：永远是 "reject / fail to reject H₀"，**绝不能说 "accept H₀"**。
4. **Type I vs. Type II error**：Type I = 弃真（α，显著性水平）；Type II = 存伪（β）。Power = 1 − β。
5. **Simple linear regression**：SST = SSR + SSE、R² 的含义、standard error of estimate、系数的 t 检验、置信区间与预测区间。

---

## ⚠️ 易错点 / 陷阱

1. **`Sx` vs. `σx`** —— 计算器上样本标准差（÷ n−1）和总体标准差（÷ n）。CFA 题几乎都问**样本**，用 `Sx`。→ [[计算器 BA II Plus 速查]]
2. **几何平均 ≤ 算术平均**，且波动越大差距越大。问「过去 5 年的平均年化收益」→ **几何**；问「下一年的期望收益」→ **算术**。
3. **Money-weighted vs. Time-weighted**：前者受现金流时点影响（评价**投资者**），后者不受（评价**经理**）。题干出现 "manager performance" 基本就是 time-weighted。
4. **Covariance vs. Correlation**：相关系数是标准化的协方差，∈[−1, 1]，无量纲。组合方差公式里用的是**协方差**，别直接代相关系数。
5. **单尾 vs. 双尾**：题干出现 "differs from"（双尾）、"greater than / exceeds"（单尾右）、"less than"（单尾左）。看错就选错临界值。
6. **`least likely` / `not`**：Quant 里大量出现。圈出来再做。

---

## 📐 核心公式

| 概念 | 公式 |
|---|---|
| Holding Period Return | $R = \dfrac{P_1 - P_0 + D_1}{P_0}$ |
| Geometric Mean Return | $R_G = \sqrt[n]{\prod(1+R_i)} - 1$ |
| Effective Annual Rate | $EAR = \left(1 + \dfrac{r}{m}\right)^m - 1$ |
| 连续复利 EAR | $EAR = e^{r} - 1$ |
| 两资产组合方差 | $\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\rho_{12}\sigma_1\sigma_2$ |
| 相关系数 | $\rho_{12} = \dfrac{Cov_{12}}{\sigma_1\sigma_2}$ |
| 检验统计量（均值，σ 未知） | $t = \dfrac{\bar{X} - \mu_0}{s/\sqrt{n}}$，df = n − 1 |
| 决定系数 | $R^2 = \dfrac{SSR}{SST} = 1 - \dfrac{SSE}{SST}$ |

---

## 🔗 关联

- 组合数学部分 → [[Portfolio Management]]（组合方差、相关性是同一套东西）
- TVM → [[Fixed Income]]（债券定价就是 TVM）、[[Corporate Issuers]]（NPV/IRR）
- 错题 → [[错题本]]
