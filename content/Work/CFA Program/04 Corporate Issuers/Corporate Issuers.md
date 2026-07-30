---
title: Corporate Issuers
tags:
  - CFA
  - CFA/L1
  - CFA/L1/CI
---

# 04 · Corporate Issuers

← [[CFA Program]] · **权重 6–9%**（约 11–16 题） · **一轮配时 11h** · **W7**

> 🎯 **定位**：小科目但**性价比高** —— 内容不多，考法固定，且大量依赖 [[Financial Statement Analysis]] 和 [[Quantitative Methods]]（NPV/IRR）的基础。
> 如果 W4–W6 的 FSA 学扎实了，这一周会很轻松。

---

## 📋 Module 清单

> 按 2024+ curriculum 结构整理，**请对照 LES 实际章节勾选核对**。

- [ ] Organizational Forms, Corporate Issuer Features, and Ownership
- [ ] Investors and Other Stakeholders
- [ ] Corporate Governance: Conflicts, Mechanisms, Risks, and Benefits
- [ ] Working Capital and Liquidity
- [ ] Capital Investments and Capital Allocation
- [ ] Capital Structure
- [ ] Business Models

---

## 🔥 高频考点

*（学到哪填到哪）*

1. **NPV vs. IRR 的冲突**：项目规模或现金流时间分布不同时两者排序会矛盾，**冲突时以 NPV 为准**（NPV 直接对应股东财富增加）。必考。
2. **相关现金流的判定**：**sunk cost 不计入**、**opportunity cost 要计入**、**externalities（含 cannibalization）要计入**。这是「看起来在算 NPV，实际在考概念」的经典题。
3. **WACC 的计算与权重口径**：用**市值权重**不是账面权重；债务成本要用**税后**（× (1 − t)）。
4. **MM 理论**：无税时资本结构无关（Prop I），有税时负债有税盾故越多越好，加入财务困境成本后出现**最优资本结构**。
5. **委托代理冲突（agency problems）**：股东 vs. 管理层、股东 vs. 债权人、控股股东 vs. 中小股东 —— 三类冲突的表现和治理机制。
6. **营运资本管理**：现金转换周期、各类短期融资来源的成本比较。

---

## ⚠️ 易错点 / 陷阱

1. **Sunk cost** —— 题干会很自然地放一句「公司已花费 $50,000 做可行性研究」，这个数**不进现金流**。看到「已经花了」就警觉。
2. **税后债务成本**：`rd × (1 − t)`。忘了乘 (1 − t) 是 WACC 题第一大错因。
3. **Cost of equity 用 CAPM**：`re = rf + β(E(Rm) − rf)`。注意括号里是**风险溢价**，不要把 `E(Rm)` 整个代进去。
4. **IRR 的多解问题**：现金流符号变号多次时 IRR 可能有多个解或无解 → 又一个用 NPV 的理由。
5. **权重用市值**：题干会同时给账面价值和市值，给账面价值就是干扰项。

---

## 📐 核心公式

| 概念 | 公式 |
|---|---|
| WACC | $WACC = w_d r_d (1-t) + w_p r_p + w_e r_e$ |
| CAPM | $r_e = r_f + \beta[E(R_m) - r_f]$ |
| NPV | $NPV = \sum \dfrac{CF_t}{(1+r)^t} - \text{初始投资}$ |
| 现金转换周期 | DSO + DOH − DPO |
| 经营杠杆 DOL | $\dfrac{\%\Delta EBIT}{\%\Delta \text{Sales}}$ |
| 财务杠杆 DFL | $\dfrac{\%\Delta EPS}{\%\Delta EBIT}$ |
| 总杠杆 DTL | $DOL \times DFL$ |

---

## 🔗 关联

- 比率与报表 → [[Financial Statement Analysis]]
- NPV/IRR 计算器操作 → [[计算器 BA II Plus 速查]]
- CAPM / beta → [[Portfolio Management]]
- 错题 → [[错题本]]
