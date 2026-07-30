---
title: Fixed Income
tags:
  - CFA
  - CFA/L1
  - CFA/L1/FI
---

# 06 · Fixed Income

← [[CFA Program]] · **权重 11–14%**（约 20–25 题） · **一轮配时 22h** · **W10–W11**

> 🎯 **定位**：和 FSA 并列的第一梯队权重，但**比 FSA 好拿分** —— 计算高度模式化，本质就是 TVM 的反复应用。
> **Duration & Convexity 是绝对核心**，这一块必须刷到闭着眼睛能做。

---

## 📋 Module 清单

> 按 2024+ curriculum 结构整理，**请对照 LES 实际章节勾选核对**。

**W10 · 特征与定价**
- [ ] Fixed-Income Instrument Features
- [ ] Fixed-Income Cash Flow Structures
- [ ] Fixed-Income Issuance and Trading
- [ ] Fixed-Income Markets for Corporate Issuers
- [ ] Fixed-Income Markets for Government Issuers
- [ ] Fixed-Income Bond Valuation: Prices and Yields（Part I / II / III）

**W11 · 风险与信用**
- [ ] The Term Structure of Interest Rates: Spot, Par, and Forward Curves
- [ ] Interest Rate Risk and Return
- [ ] Yield-Based Bond Duration Measures and Properties
- [ ] Yield-Based Bond Convexity and Portfolio Properties
- [ ] Curve-Based and Empirical Fixed-Income Risk Measures
- [ ] Credit Risk / Credit Analysis for Government & Corporate Issuers
- [ ] Fixed-Income Securitization + ABS / MBS Features

---

## 🔥 高频考点

*（学到哪填到哪）*

1. **价格与收益率的反向关系 + 凸性**：价格-收益率曲线是**向原点凸出**的。→ 收益率下降带来的涨幅 **>** 同等幅度收益率上升带来的跌幅。
2. **溢价债 / 折价债 / 平价债** 的判定与价格随时间的 **pull to par** 路径。
3. **Macaulay / Modified / Effective / Money duration** 的定义、单位、适用场景。**含权债券必须用 effective duration**。
4. **久期的影响因素**：期限越长久期越大；票息越高久期越小；YTM 越高久期越小。
5. **Spot / Par / Forward rate 的相互推导** —— 计算题，套路固定，必须练熟。
6. **信用利差与信用分析的 4C**（Capacity, Collateral, Covenants, Character）。

---

## ⚠️ 易错点 / 陷阱

1. **Modified duration = Macaulay duration / (1 + y/m)** —— 分母别忘，而且 y 要用**每期**收益率。
2. **久期估计的价格变动是「近似」**，加上凸性修正才更准。凸性修正项**永远为正**（对普通债券），所以只用久期会**低估**涨幅、**高估**跌幅。
3. **含权债券**：可赎回债（callable）→ **负凸性**（收益率下行时价格涨幅受限）；可回售债（putable）→ 价格下行受保护。必须用 effective duration，不能用 modified。
4. **单位陷阱**：题干给 **basis points** 还是 **percentage points**。25 bp = 0.25%。这个坑在 duration 题里出现率极高。
5. **半年付息**：`N` = 年数 × 2，`I/Y` = 年 YTM ÷ 2，`PMT` = 年息 ÷ 2。算出来的价格是对的，但**报出来的 YTM 要 ×2**（bond-equivalent yield）。
6. **Current yield ≠ YTM**：current yield 只考虑票息 / 价格，忽略资本利得。折价债 YTM > current yield > coupon rate；溢价债反过来。

---

## 📐 核心公式

| 概念 | 公式 |
|---|---|
| 债券价格 | $P = \sum \dfrac{C}{(1+y)^t} + \dfrac{FV}{(1+y)^n}$ |
| Modified Duration | $ModDur = \dfrac{MacDur}{1 + y/m}$ |
| Effective Duration | $\dfrac{P_{-} - P_{+}}{2 \times P_0 \times \Delta \text{curve}}$ |
| 价格变动（久期） | $\%\Delta P \approx -ModDur \times \Delta y$ |
| 价格变动（久期+凸性） | $\%\Delta P \approx -ModDur \times \Delta y + \tfrac{1}{2} \times Convexity \times (\Delta y)^2$ |
| Money Duration | $ModDur \times$ 全价 |
| PVBP | $\dfrac{P_{-} - P_{+}}{2}$（1 bp 变动的价格变化） |
| 远期利率 | $(1+S_2)^2 = (1+S_1)(1+{}_1f_1)$ |

> 💡 **凸性修正项符号记法**：$(\Delta y)^2$ 恒为正，凸性对普通债券为正 → 这一项**永远是加分项**。所以久期单独用总是「不够乐观」。

---

## 🔗 关联

- 定价本质是 TVM → [[Quantitative Methods]]、[[计算器 BA II Plus 速查]]
- 信用分析的比率 → [[Financial Statement Analysis]]
- 利率与货币政策 → [[Economics]]
- 利率互换 → [[Derivatives]]
- 错题 → [[错题本]]
