---
title: Economics
tags:
  - CFA
  - CFA/L1
  - CFA/L1/Econ
---

# 02 · Economics

← [[CFA Program]] · **权重 6–9%**（约 11–16 题） · **一轮配时 22h** · **W2–W3**

> 🎯 **定位**：概念题为主，计算集中在**汇率**（远期升贴水、交叉汇率、套算）。
> 性价比策略：**汇率计算必须练熟**（几乎每次都考且是确定送分），宏观政策部分理解框架即可，不用背细节数据。

---

## 📋 Module 清单

> 按 2024+ curriculum 结构整理，**请对照 LES 实际章节勾选核对**。

**W2 · 微观 + 周期**
- [ ] The Firm and Market Structures
- [ ] Understanding Business Cycles

**W3 · 宏观政策 + 国际**
- [ ] Fiscal Policy
- [ ] Monetary Policy
- [ ] Introduction to Geopolitics
- [ ] International Trade
- [ ] Capital Flows and the FX Market
- [ ] Exchange Rate Calculations

---

## 🔥 高频考点

*（学到哪填到哪）*

**先埋几个确定的高频点：**

1. **四种市场结构对比**（perfect competition / monopolistic competition / oligopoly / monopoly）—— 必考对比表：企业数量、产品差异、进入壁垒、定价能力、需求曲线弹性、长期经济利润。
2. **利润最大化条件 MR = MC**，以及各市场结构下 P 与 MR 的关系（完全竞争 P = MR；其余 P > MR）。
3. **货币政策 vs. 财政政策**：工具、传导机制、时滞（财政的**行动时滞**长、货币的**效果时滞**长）、四种政策组合对利率和产出的影响。
4. **汇率报价方向** —— Econ 失分王。见下方陷阱区。
5. **Business cycle 各阶段的特征**：库存、失业、通胀的领先/同步/滞后关系。

---

## ⚠️ 易错点 / 陷阱

1. **汇率报价方向（最高频失分点）**：`USD/EUR` 在 CFA 里读作 **"price currency / base currency"**，即 **1 EUR 值多少 USD**。**base 在后**。这和很多外汇市场习惯相反，看反了整题全错。做题第一步：**先圈出谁是 base**。
2. **升值/贬值的百分比不对称**：A 相对 B 升值 25% ≠ B 相对 A 贬值 25%。必须用倒数重算。
3. **远期升水/贴水**：利率**高**的货币在远期**贴水**（forward discount）。直觉：不然就有无风险套利。
4. **Fiscal vs. Monetary 的时滞方向别记反**：财政政策 → 立法流程长（recognition + action lag 长），但一旦执行见效快；货币政策 → 央行决策快，但传导到实体经济慢。
5. **Elastic vs. Inelastic 与总收入的关系**：需求富有弹性时降价→总收入**升**；缺乏弹性时降价→总收入**降**。
6. **GDP deflator vs. CPI**：deflator 覆盖所有国内生产的商品（篮子随时变），CPI 是固定篮子且含进口品。

---

## 📐 核心公式

| 概念 | 公式 |
|---|---|
| 交叉汇率 | $\dfrac{A}{C} = \dfrac{A}{B} \times \dfrac{B}{C}$（单位像分数一样约掉） |
| 远期汇率（covered interest rate parity） | $F = S \times \dfrac{1 + i_{price}}{1 + i_{base}}$ |
| 远期升贴水 | $\dfrac{F - S}{S}$ |
| 货币乘数 | $\dfrac{1}{\text{准备金率}}$ |
| 财政乘数 | $\dfrac{1}{1 - MPC(1-t)}$ |
| 费雪方程 | $R_{nominal} \approx R_{real} + \pi^e$ |

> 💡 **记 forward 公式的方法**：把 $S$ 写成 price/base，那么分子放 **price currency 的利率**，分母放 **base currency 的利率**。方向就不会错。

---

## 🔗 关联

- 汇率 / 利率平价 → [[Fixed Income]]（收益率曲线）、[[Derivatives]]（远期定价同一套 no-arbitrage 逻辑）
- 商业周期 → [[Equity Investments]]（行业周期性分析）
- 错题 → [[错题本]]
