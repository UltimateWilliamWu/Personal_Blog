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

### TVM 的地基

时间价值的作用是**在不同日期发生的现金流之间建立等价关系**。「今天的钱」和「一年后的钱」是两种不同的东西，需要一个换算率才能比较 —— 那个换算率就是利率。

### 🔢 教材的锚点例子（务必看清分母）

```
今天 9,500  ≡  一年后 10,000
补偿 = 10,000 − 9,500 = 500
利率 = 500 ÷ 9,500 = 5.26%
```

> ⚠️ **分母是 9,500，不是 10,000。** `500 ÷ 10,000 = 5%` 是典型粗心错。
> 利率永远相对于**你投入的本金**，即 HPR 的 $\frac{P_1-P_0}{P_0}$ —— **分母永远是起点**。

### 三种解读（同一个数的三个视角）

| 解读 | 视角 | 在上面例子里 |
|---|---|---|
| **Required rate of return** | 投资者 | 「至少给我 5.26%，我才肯今天掏 9,500」 |
| **Discount rate** | 估值 | 「用 5.26% 折现，一年后 10,000 = 今天 9,500」 |
| **Opportunity cost** | 消费者 | 「今天花掉这 9,500，就放弃了赚 5.26% 的机会」 |

> 教材原文承认这几个词 "almost interchangeably" —— 题目里混着用是正常的，都是同一个 r。

### ⭐ 利率由供需决定

> 利率由**供给和需求**决定：**投资者供给资金，借款人需求资金**。

这解释了为什么 premium 不是主观的 —— 每一项都是市场博弈的均衡结果。
另注意教材的视角声明：整个 build-up 公式是**站在投资者角度**构建的（出借方要求什么补偿），不是借款方的成本视角。

### 分解式（必背）

```
r = Real risk-free rate
  + Inflation premium
  + Default risk premium
  + Liquidity premium
  + Maturity premium
```

| 溢价 | 补偿什么 | ⭐ 教材细节考点 |
|---|---|---|
| **Real risk-free rate** | 纯粹的时间价值 | 定义有三个限定词：**single-period · completely risk-free · no inflation expected**。反映人们对当前 vs. 未来消费的 **time preferences（时间偏好）** |
| **Inflation premium** | 预期通胀侵蚀购买力 | 是 **expected**（预期）通胀，且是**整个期限内的平均**预期通胀率 |
| **Default risk premium** | 借款人可能违约 | 原文是 "fail to make a promised payment **at the contracted time and in the contracted amount**" —— 迟付、少付都算 |
| **Liquidity premium** | 急着变现时相对 fair value 的损失 | ⭐⭐ **US T-bills 不含 liquidity premium**（可大额买卖而不影响价格）；**小发行人债券含**（发行后交投稀少，卖出成本高） |
| **Maturity premium** | 期限越长，市值对利率变动越敏感 | ⭐ 长短期国债利差 **不全是** maturity premium —— 教材明说 "and possibly **different inflation premiums** as well" |

$$\text{Nominal risk-free} \approx \text{Real risk-free} + \text{Inflation premium}$$

> ⚠️ **Liquidity vs. Maturity premium 易混**：一个关于「卖不掉」，一个关于「期限长」。

### 💡 直觉：这不是数学公式，是一张报价单

把它读成「**时间本身的价钱 + 我让你承担的每一种风险的价钱**」：

先想象最纯净的借贷 —— 我百分百会还、无通胀、借条随时能转手、只借三个月。这时你仍要收利息，因为你放弃了现在用钱的机会。这个纯粹的「时间的价钱」就是 **real risk-free rate**，它跟风险无关。

然后每加一层风险，加一层补偿：

| 放松哪个假设 | 加什么 premium |
|---|---|
| 会有通胀，还你的钱购买力下降 | Inflation premium |
| 我有可能还不上 | Default risk premium |
| 借条不好转手，急用钱只能折价卖 | Liquidity premium |
| 借 30 年而不是 3 个月 | Maturity premium |

### 💡 这些 premium 在现实中怎么量化？—— 做减法

不是谁拍脑袋定的，是**从市场价格里倒推**，每一项都是两个可观测收益率之差：

| Premium | 现实中怎么估 |
|---|---|
| Inflation premium | 普通国债收益率 − 同期限 **TIPS** 收益率 |
| Default risk premium | 公司债收益率 − 同期限国债收益率（**信用利差**） |
| Maturity premium | 长期国债收益率 − 短期国债收益率（**期限利差**） |

> **诚实的局限**：总量客观（市场交易定价），但拆分到每一项是估算的 —— 信用利差里 default 和 liquidity 混在一起，学界仍在争论各占多少；inflation premium 用的是**预期**通胀，不可直接观测。
>
> **但 L1 不考这个**。L1 绝不会让你去估计 premium 的数值，那是 L2/L3 和实务的事。

### 🎯 L1 的三种考法（只有这三种）

| 形式 | 长什么样 |
|---|---|
| **A. 纯概念**（最常见） | 「30 年期国债收益率高于 3 个月期，最能解释的是？」→ maturity premium |
| **B. 直接加减**（送分） | 给全五项让你求和；或给总数和其中四项，倒推第五项 |
| **C. Real ↔ Nominal 转换** | 唯一涉及「精确 vs 近似」的地方 ↓ |

### ⚠️ 精确还是近似？—— 两个公式场景不同，不是二选一

| 场景 | 用哪个 |
|---|---|
| **利率分解**（build-up） | **永远用加法**。教材原文就是 "approximated as the sum of"，在 CFA 体系里定义上就是加法 |
| **Real return 换算**（nominal → real） | **用除法（精确）**：$1 + r_{real} = \dfrac{1+r_{nominal}}{1+\pi}$ |

**考场实操法**（三选一的选项结构会告诉你答案）：

> 先按**近似**算 → 选项里有完全吻合的 → 选它（考的是加减）
> 近似值卡在两个选项**中间** → 出题人在考精确式 → 换乘除法重算

**例**：nominal 8%，通胀 3%
- 近似 `8 − 3 = 5.00%` ／ 精确 `1.08 ÷ 1.03 − 1 = 4.85%`
- 选项 `4.85 / 5.00 / 5.15` → 考精确式
- 选项 `3.00 / 5.00 / 11.00` → 只考你会不会减

两种算法都在 20 秒内，拿不准就都算。

### ⚠️⚠️ 报价利率是年化的（最容易忽略的陷阱）

教材原文藏了一句杀伤力很大的话：

> 90 天期国债**报价 3%**，指的是**年化利率**，**不是**这 90 天里实际赚到的收益。

90 天实际赚的约为 `3% × 90/360 ≈ 0.75%`。

> **看到任何利率报价，先问一句：这是年化的还是期间的？** 这个坑在 [[Fixed Income]] 里会反复出现。

各国短期政府债都可视为该国的 nominal risk-free rate：美国 90 天 T-bill、法国 BTF、日本 6/12 个月国库券。（国家名不太可能考，但「**短期政府债利率 ≈ 该国 nominal risk-free rate**」是考点。）

### 为什么利率天天在变

所有 premium 和 real risk-free rate 都**随时间持续变化** → 所有利率都在波动。
`r` 里的每一项都是**时变的** —— 这是后面学 term structure 和 duration 的铺垫。

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

0. **利率算式的分母是起点值**：`500 ÷ 9,500`，不是 `500 ÷ 10,000`
1. **报价利率是年化的**，≠ 期间实际收益（90 天报价 3% ≠ 90 天赚 3%）
2. **US T-bills 不含 liquidity premium**；小发行人债券含
3. **长短期国债利差不全是 maturity premium**，还含不同的 inflation premium
4. **Inflation premium 是预期的、整个期限的平均**
5. `Nominal ≈ Real + Inflation` 是**近似**；build-up 公式考试用加法，real return 换算用除法
6. **Liquidity premium**（急售折价）vs. **Maturity premium**（期限敏感度）
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
