---
title: Derivatives
tags:
  - CFA
  - CFA/L1
  - CFA/L1/Deriv
---

# 07 · Derivatives

← [[CFA Program]] · **权重 5–8%**（约 9–14 题） · **一轮配时 11h** · **W12**

> 🎯 **定位**：权重最小的科目，但**别当成可以放弃的科目** —— L1 的衍生品几乎全部建立在**一条主线**上：
> **无套利定价（no-arbitrage）**。理解了这一条，forward / futures / swap / option 的定价逻辑是同一个东西的四种皮肤。
> 时间紧张时，**优先保 put-call parity 和 cost of carry，砍 binomial model 的手算细节**。

---

## 📋 Module 清单

> 按 2024+ curriculum 结构整理，**请对照 LES 实际章节勾选核对**。

- [ ] Derivative Instrument and Derivative Market Features
- [ ] Forward Commitment and Contingent Claim Features and Instruments
- [ ] Derivative Benefits, Risks, and Issuer and Investor Uses
- [ ] Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives
- [ ] Pricing and Valuation of Forward Contracts
- [ ] Pricing and Valuation of Futures Contracts
- [ ] Pricing and Valuation of Interest Rate and Other Swaps
- [ ] Pricing and Valuation of Options
- [ ] Option Replication Using Put–Call Parity
- [ ] Valuing a Derivative Using a One-Period Binomial Model

---

## 🔥 高频考点

*（学到哪填到哪）*

1. **Forward commitment vs. Contingent claim**：远期/期货/互换是**义务**（双向对称收益），期权是**权利**（单向不对称收益）。这个二分法是整科的框架。
2. **Cost of carry**：$F_0 = S_0 \times (1+r)^T$，再减去持有收益（股息/票息/便利收益），加上持有成本（仓储）。**一个公式串起所有远期定价**。
3. **Put-call parity**：$c + \dfrac{X}{(1+r)^T} = p + S_0$。考法：给三个求第四个，或者问「怎么用合成方式复制某个头寸」。
4. **Forward vs. Futures 的区别**：场外/场内、定制/标准化、对手方风险/清算所担保、**每日盯市（mark to market）**。
5. **期权价值的上下限、影响因素**（标的价、执行价、到期时间、波动率、无风险利率、股息）对 call/put 的方向。
6. **One-period binomial model**：风险中性概率 $\pi = \dfrac{(1+r) - d}{u - d}$。

---

## ⚠️ 易错点 / 陷阱

1. **Price vs. Value 是两个东西**。Forward **price** 是合约里约定的交割价（签订时确定，之后不变）；Forward **value** 是合约本身值多少钱（签订时为 0，之后随标的波动）。混淆这两个是 Derivatives 第一大失分点。
2. **签约时远期合约价值 = 0**，不是价值 = 远期价格。
3. **Put-call parity 里的执行价要折现**：$\dfrac{X}{(1+r)^T}$，不是 X。
4. **风险中性概率不是真实概率**，也不能用真实概率折现。这是概念题常考的陷阱。
5. **期权到期时间对美式 put 的影响**是唯一可能反直觉的一项（深度实值美式 put 提前行权可能更优）—— 一般规律「时间越长价值越高」对**欧式 put** 不总成立。
6. **多头/空头方向**：题干说 "sold a forward"（空头），到期时 $S_T > F_0$ 是**亏**。做题先画一条收益线。

---

## 📐 核心公式

| 概念 | 公式 |
|---|---|
| 远期价格（无收益标的） | $F_0 = S_0 (1+r)^T$ |
| 远期价格（含持有收益 I） | $F_0 = (S_0 - PV(I))(1+r)^T$ |
| 远期合约到期价值（多头） | $V_T = S_T - F_0$ |
| Put-Call Parity | $c + \dfrac{X}{(1+r)^T} = p + S_0$ |
| Call 到期收益 | $\max(0,\ S_T - X)$ |
| Put 到期收益 | $\max(0,\ X - S_T)$ |
| 风险中性概率 | $\pi = \dfrac{(1+r) - d}{u - d}$ |
| 二叉树期权价值 | $c = \dfrac{\pi c^+ + (1-\pi)c^-}{1+r}$ |

---

## 🔗 关联

- 无套利逻辑与远期汇率同源 → [[Economics]]
- 利率互换 → [[Fixed Income]]
- 对冲与风险管理 → [[Portfolio Management]]
- 错题 → [[错题本]]
