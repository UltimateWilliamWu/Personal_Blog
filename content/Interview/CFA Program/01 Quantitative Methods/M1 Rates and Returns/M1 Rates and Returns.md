---
title: M1 Rates and Returns
tags:
  - CFA
  - CFA/L1
  - CFA/L1/Quant
  - Type/Index
---

# Module 1 · Rates and Returns

← [[Quantitative Methods]] · [[CFA Program]] · **W1**

> **一句话概括**：本 module 回答两件事 —— ① 利率由什么构成 ② 同一段投资历史该用哪种「平均收益」来描述。
> **考点 80% 集中在 ②**，而且考法几乎全是「这个场景该用哪一个」，不是「算出这个数」。

---

## 📚 Lesson 清单

> 官方教材把本 module 拆成 lesson 粒度（1.0x）。每篇一个 lesson，独立精读。

| Lesson | 笔记 | 对应 LOS | 状态 |
|---|---|---|---|
| **1.01** | [[1.01 Introduction]] | Module 总览 + 自测清单 | ✅ **已精写** |
| **1.02** | [[1.02 Interest Rates and Time Value of Money]] | 利率的三种解读 + 五项分解 | ✅ **已精写** |
| 1.03 | [[1.03 Rates of Return]] ⚠️ | 收益度量方式与适用场景 | 🚧 待精写 |
| 1.04 | [[1.04 Money-Weighted and Time-Weighted Return]] ⚠️ | MWR vs. TWR、业绩评价 | 🚧 待精写 |
| 1.05 | [[1.05 Annualized Return]] ⚠️ | 年化 + 连续复利 | 🚧 待精写 |
| 1.06 | [[1.06 Other Major Return Measures]] ⚠️ | 各种收益口径 | 🚧 待精写 |

> ⚠️ **1.03–1.06 的标题和编号是从 LOS 反推的推测，不是官方标题** —— 贴原文时按实际标题重命名。
>
> 🚧 = 内容已从旧整篇笔记迁入、结构完整，但**尚未按官方原文做「翻译 + 逐概念详解」**。
> 精写标准参照 [[1.02 Interest Rates and Time Value of Money]]。

---

## 📖 LOS（官方学习目标）

1. interpret interest rates as required rates of return, discount rates, or opportunity costs; explain an interest rate as the sum of a real risk-free rate and premiums → **1.02**
2. calculate and interpret different approaches to return measurement over time and describe their appropriate uses → **1.03**
3. compare the **money-weighted** and **time-weighted** rates of return and evaluate portfolio performance based on these measures → **1.04**
4. calculate and interpret **annualized** return measures and **continuously compounded** returns → **1.05**
5. calculate and interpret **major return measures** and describe their appropriate uses → **1.06**

---

## 🎯 本 Module 考点优先级

| 优先级 | 考点 | 在哪 | 理由 |
|---|---|---|---|
| ⭐⭐⭐ | **MWR vs. TWR**（尤其「评价经理用哪个」） | [[1.04 Money-Weighted and Time-Weighted Return]] | 几乎必考，且是概念题送分 |
| ⭐⭐⭐ | **五种 mean 的选择 + 大小关系** | [[1.03 Rates of Return]] | 必考，Trimmed/Winsorized 易混 |
| ⭐⭐ | **利率分解**（五个组成部分） | [[1.02 Interest Rates and Time Value of Money]] | 送分题 |
| ⭐⭐ | **EAR / 连续复利 / 年化** | [[1.05 Annualized Return]] | 计算题，套路固定 |
| ⭐ | **Gross vs. Net / Real vs. Nominal** | [[1.06 Other Major Return Measures]] | 定义辨析 |

---

## ⚠️ 全 Module 易错点总清单

> 跨 lesson 汇总。**考前只看这一页。**

### 利率与分解（1.02）

1. **利率算式的分母是起点值** —— `500 ÷ 9,500 = 5.26%`，不是 `500 ÷ 10,000`
2. **报价利率是年化的** —— 90 天报价 3% ≠ 90 天赚 3%（≈0.75%）
3. **US T-bills 不含 liquidity premium**；小发行人债券**含**
4. **长短期国债利差 ≠ 纯 maturity premium** —— 还含**不同的 inflation premium**
5. **Inflation premium 是「预期的」+「整个期限的平均」**
6. **Liquidity（卖不掉）vs. Maturity（期限长）** —— 用「市场活跃能否消除它」区分
7. **Build-up 用加法，real return 换算用除法** —— 场景不同，不是二选一

### 收益度量（1.03）

8. **Trimmed = 删，Winsorized = 换**（样本量变 / 不变）
9. **Geometric 看过去，Arithmetic 预测未来**
10. **Harmonic 用于定额定投的平均成本**

### 业绩评价（1.04）

11. **评价经理用 TWR**（现金流时点非经理可控）
12. **上涨前加仓 → MWR > TWR**

### 年化与口径（1.05 / 1.06）

13. 年化短期收益会得到荒谬数字 → 考「是否合理」（答：不合理，隐含可持续再投资假设）
14. **Gross return 已扣交易成本**，只是没扣管理费

### 计算器

15. 样本标准差用 `Sx`（不是 `σx`）；MWR 用 `CF` → `IRR`；**每题前 `2ND CLR WORK`**

---

## 🔗 关联

- 计算器操作 → [[计算器 BA II Plus 速查]]
- TVM / 折现 → 下一个 module: Time Value of Money in Finance
- 组合收益与风险 → [[Portfolio Management]]
- 通胀与实际利率 → [[Economics]]
- 错题 → [[错题本]]
