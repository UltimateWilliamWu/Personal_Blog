---
title: M1 Rates and Returns
tags:
  - CFA
  - CFA/L1
  - CFA/L1/Quant
---

# Module 1 · Rates and Returns

← [[Quantitative Methods]] · [[CFA Program]] · **W1**

> **一句话概括**：本 module 回答两件事 —— ① 利率由什么构成 ② 同一段投资历史该用哪种「平均收益」来描述。
> **考点 80% 集中在 ②**，而且考法几乎全是「这个场景该用哪一个」，不是「算出这个数」。

---

## 📖 LOS（官方学习目标）

1. interpret interest rates as required rates of return, discount rates, or opportunity costs; explain an interest rate as the sum of a real risk-free rate and premiums
2. calculate and interpret different approaches to return measurement over time and describe their appropriate uses
3. compare the **money-weighted** and **time-weighted** rates of return and evaluate portfolio performance based on these measures
4. calculate and interpret **annualized** return measures and **continuously compounded** returns
5. calculate and interpret **major return measures** and describe their appropriate uses

---

## 1️⃣ 利率的本质与分解

### 三种解读（同一个数的三个视角）

| 解读 | 视角 | 场景 |
|---|---|---|
| **Required rate of return** | 投资者 | 我要求的最低回报，否则不投 |
| **Discount rate** | 估值 | 把未来现金流折回今天 |
| **Opportunity cost** | 消费者 | 今天不消费、把钱借出去的代价 |

> 利率的本质：**反映不同时点现金流之间的关系**（the relationship between differently dated cash flows）。

### 分解式（必背）

```
r = Real risk-free rate
  + Inflation premium
  + Default risk premium
  + Liquidity premium
  + Maturity premium
```

| 溢价 | 补偿什么 |
|---|---|
| **Inflation premium** | 预期通胀侵蚀购买力 |
| **Default risk premium** | 借款人可能违约 |
| **Liquidity premium** | 想卖时卖不掉 / 要折价卖 → 关于**变现** |
| **Maturity premium** | 期限越长，对利率变动越敏感 → 关于**久期** |

$$\text{Nominal risk-free} \approx \text{Real risk-free} + \text{Inflation premium}$$

> ⚠️ **这是近似**。精确关系是乘法：$(1+r_{nom}) = (1+r_{real})(1+\pi)$。
> 数字小时两者接近，数字大时（高通胀情景）差异显著 —— 题目会用这个设陷阱。

> ⚠️ **Liquidity vs. Maturity premium 易混**：一个关于「卖不掉」，一个关于「期限长」。

---

## 2️⃣ 单期收益：Holding Period Return

$$R = \frac{P_1 - P_0 + I_1}{P_0} = \underbrace{\frac{I_1}{P_0}}_{\text{income yield}} + \underbrace{\frac{P_1 - P_0}{P_0}}_{\text{capital gain yield}}$$

**总回报 = 收益率部分（股息/利息）+ 资本利得部分**。这个拆分本身就是考点。

多期链接：

$$1 + R_{total} = (1+R_1)(1+R_2)\cdots(1+R_n)$$

---

## 3️⃣ 🌳 决策树一：多期收益用哪个平均？

> **本 module 第一大考点。** 考法：给一组数据 + 一个场景，问该用哪个 / 算哪个。

| 题干在问 | 用 | 公式 |
|---|---|---|
| 过去 n 年的**平均年化收益** / 实际复合增长率 | **Geometric mean** | $\left[\prod(1+R_i)\right]^{1/n} - 1$ |
| **下一期**的期望收益 / 单期最佳估计 | **Arithmetic mean** | $\dfrac{\sum R_i}{n}$ |
| **定额定投**的平均买入成本 | **Harmonic mean** | $\dfrac{n}{\sum (1/X_i)}$ |
| 有极端值，想**删掉** | **Trimmed mean** | 去掉最高最低各 x% 后取算术平均 |
| 有极端值，想**削弱但保留样本量** | **Winsorized mean** | 把极端值**替换**成某百分位值后取算术平均 |

### 必背不等式

$$\text{Harmonic} \le \text{Geometric} \le \text{Arithmetic}$$

- 仅当所有数值**完全相同**时取等号
- **波动越大，三者差距越大** —— 这是几何平均「惩罚波动」的体现

### ⚠️ 易错点

1. **Trimmed = 删，Winsorized = 换**。Trimmed 后样本量变小，Winsorized 后样本量不变。这是本节送命题第一名。
2. **Geometric 用于回顾过去，Arithmetic 用于预测未来**。看到 "average annual return over the past 5 years" → 几何；看到 "expected return next year" → 算术。
3. **Harmonic mean 的应用场景是「固定金额买浮动价格」**（dollar cost averaging）。每月投 $1000 买股票，平均买入成本是价格的 harmonic mean，不是 arithmetic mean。
4. 两个观测值时有恒等式：$\text{Arithmetic} \times \text{Harmonic} = \text{Geometric}^2$。

---

## 4️⃣ 🌳 决策树二：Money-weighted vs. Time-weighted

> **本 module 第二大考点，也是整个 Quant 最高频的概念题之一。**

| | **Money-weighted (MWR)** | **Time-weighted (TWR)** |
|---|---|---|
| 本质 | 组合现金流的 **IRR** | 各子期 HPR 的**几何链接** |
| 受现金流金额/时点影响 | ✅ **受影响** | ❌ **不受影响** |
| 回答的问题 | 投资者**实际赚了多少** | 投在里面的**每一块钱长了多少** |
| 适用于评价 | **投资者** | **基金经理** ⭐ |
| 计算方式 | BA II Plus `CF` → `IRR` | 分段算 HPR 再连乘 |

### 为什么评价经理必须用 TWR

申购赎回的**时点是客户决定的，不在经理控制范围内**。客户在低点大额赎回，MWR 会把这笔损失算到经理头上 —— 但那不是经理的决策。TWR 剔除了这个干扰。

> GIPS 也要求业绩呈现使用 TWR（部分私募类资产除外，因为那些的现金流时点**确实**由管理人控制 —— capital call 是 GP 发起的）。

### TWR 的计算步骤

1. 在**每次外部现金流发生时**把期间切分成子期
2. 每个子期单独算 HPR
3. 几何链接：$(1+TWR) = (1+HPR_1)(1+HPR_2)\cdots$
4. 需要年化时再开 n 次方

### ⚠️ 方向判断题（高频）

| 投资者行为 | 结果 |
|---|---|
| 在**上涨期之前加仓** | 高收益作用于更大本金 → **MWR > TWR** |
| 在**上涨期之前减仓**（或下跌前加仓） | **MWR < TWR** |

> 记法：MWR 会「奖励好的择时、惩罚差的择时」，TWR 对择时完全免疫。

---

## 5️⃣ 复利频率、年化与连续复利

### 名义年利率 → EAR

$$EAR = \left(1 + \frac{r_s}{m}\right)^m - 1$$

- $r_s$ = stated / quoted annual rate，$m$ = 每年复利次数
- **Periodic rate** = $r_s / m$
- m 越大 EAR 越高，但增速递减，极限是连续复利

### 连续复利

$$EAR = e^{r_s} - 1 \qquad\qquad r_{cc} = \ln\frac{P_1}{P_0} = \ln(1 + HPR)$$

> 连续复利收益率**可加**（跨期直接相加），这是它在量化里常用的原因。

### 任意持有期年化

$$r_{annual} = (1 + R_{period})^{c} - 1$$

其中 $c$ = 一年内包含多少个这样的持有期。

**例**：19 天赚 3% → $(1.03)^{365/19} - 1 \approx 78\%$

> ⚠️ **年化陷阱题**：短期高收益年化后数字荒谬。题目会问「这个年化数字合理吗」→ 答案是**不合理**，因为它隐含假设「该收益率能在全年持续复利再投资」，短期波动不具备这种可持续性。

---

## 6️⃣ 🌳 决策树三：各种收益口径

| 口径 | 定义 | 什么时候用 |
|---|---|---|
| **Gross return** | 扣除**交易成本**后，**未扣**管理费和行政费 | 比较**资产管理人的能力** |
| **Net return** | Gross − 管理费 − 行政费 | 投资者**实际到手** |
| **Pre-tax nominal** | 未扣税、未调通胀（默认口径） | 一般报价 |
| **After-tax nominal** | 扣掉股息/利息/**已实现**资本利得的税 | 应税账户 |
| **Real return** | 剔除通胀 | **跨时期**比较、跨国比较 |
| **After-tax real** | 既扣税又剔通胀 | 跨**税收待遇不同**的资产类别 |
| **Leveraged return** | 借款或期货放大 | 放大盈亏 |

### ⚠️ Gross return 的定义细节（考过）

Gross return **已经扣掉了交易成本**（佣金、买卖价差），只是没扣管理费和行政费。

**逻辑**：交易成本是投资过程的一部分，体现管理人的执行能力 → 该扣；管理费是商业条款，跟投资能力无关 → 不该扣，否则无法横向比较不同费率的管理人。

### 公式

$$1 + r_{real} = \frac{1 + r_{nominal}}{1 + \pi} \qquad\Rightarrow\qquad r_{real} \approx r_{nominal} - \pi$$

$$R_{leveraged} = R_p + \frac{V_{borrowed}}{V_{equity}}(R_p - r_{debt})$$

> 杠杆公式的直觉：自有资金的收益 = 组合收益 + 杠杆倍数 ×（组合收益 − 借款成本）。**只有当 $R_p > r_{debt}$ 时杠杆才增厚收益**，反之放大亏损。

---

## 🎯 本 Module 考点优先级

| 优先级 | 考点 | 理由 |
|---|---|---|
| ⭐⭐⭐ | **MWR vs. TWR**（尤其「评价经理用哪个」） | 几乎必考，且是概念题送分 |
| ⭐⭐⭐ | **五种 mean 的选择 + 大小关系** | 必考，Trimmed/Winsorized 易混 |
| ⭐⭐ | **利率分解**（五个组成部分） | 送分题 |
| ⭐⭐ | **EAR / 连续复利 / 年化** | 计算题，套路固定 |
| ⭐ | **Gross vs. Net / Real vs. Nominal** | 定义辨析 |

---

## ⚠️ 易错点总清单

1. `Nominal ≈ Real + Inflation` 是**近似**，精确是乘法
2. **Liquidity premium**（卖不掉）vs. **Maturity premium**（期限长）
3. **Trimmed = 删，Winsorized = 换**
4. **Geometric 看过去，Arithmetic 预测未来**
5. **Harmonic 用于定额定投的平均成本**
6. **评价经理用 TWR**（现金流时点非经理可控）
7. **Gross return 已扣交易成本**，只是没扣管理费
8. 年化短期收益会得到荒谬数字 → 考「是否合理」
9. 计算器：样本标准差用 `Sx`；MWR 用 `CF` → `IRR`；每题前 `2ND CLR WORK`

---

## 🔗 关联

- 计算器操作 → [[计算器 BA II Plus 速查]]
- TVM / 折现 → 下一个 module: Time Value of Money in Finance
- 组合收益与风险 → [[Portfolio Management]]
- 通胀与实际利率 → [[Economics]]
- 错题 → [[错题本]]
