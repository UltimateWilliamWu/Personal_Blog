---
tags:
  - LectureNotes
---
## 1. Classification 分类
Find a line that separates the two classes.
![[Pasted image 20250316163131.png|500]]
### Basic Linear Classifier
![[Pasted image 20250412175125.png|500]]
Using a Linear Classifier to classify:
$$ax_1+bx_2+c=0$$

>[!note] Logic Regression 逻辑回归
>- 
>Sigmod Function: 将线性回归的值映射到[0,1]中 表示预测为某个类别的概率
>$\qquad$![[Pasted image 20250316164255.png]]
>决策边界就是$x^T\beta$ 是一条线用于分割类别
>$\beta$就是回归系数 也就是损失函数的理论最小值 但是不同于线性回归 
>它无法用牛顿的最小二乘法获得闭式解 因此只能使用极大似然估计来表示
>Loss Function(MLE): 不能用最小二乘法因为是非线性
>$\qquad$![[Pasted image 20250316170135.png]]
>- ### Discriminative Models (判别模型)
>	- 只是计算函数值并判断是否大于零来进行判别 不考虑数据分布
>	- 关注的是值的差异
>- ### Generative Models (生成模型)
>	- 联合概率分布 考虑数据分布
>	- loss function 是两个数据分布
## 2. Generalization 泛化
泛化是指一个模型对未见过数据的适应能力 即模型能否正确预测训练集之外的数据
过拟合：训练集上表现好 测试集上表现差
### 2.1 泛化的基本假设 Assumptions for Generalization
- 独立同分布 Independent and Identically Distributed
	- 训练集数据和测试集数据是在相同概率分布中独立抽取的
- 分布稳定性 Stationary Distribution
	- 数据分布不会随着时间变化 即训练集和测试集来自相同分布
- 数据一致性 Consistent Datasource
	- 训练集测试集验证集来自相同数据分布
### 2.2 过拟合和欠拟合
#### 过拟合 Overfitting
模型对训练数据学习的过于细致，甚至学习了噪声，导致对新数据的泛化能力变差
#### 欠拟合 Underfitting
模型对训练数据学习不够，通常因为模型太简单
### 解决方案
- 使用交叉验证 将训练数据划分成多个子集，轮流“训练”和“验证”，从而更加稳定、准确地评估模型性能。
- 采用正则化限制模型复杂度 在损失函数中加上一项“惩罚项”，让模型不再一味追求拟合训练数据，而是学一个更**简洁、泛化能力更强**的模型
- 适当增加训练集 减少模型对于噪声的依赖 （噪声是指数据中那些无法被模型解释的随机因素或扰动。）

>[!note] 常见交叉验证的方法
>### 1. 保留法
>- 数据集分为测试集和训练集
>- 仅在训练集上训练 测试集上评估 定死测试集和数据集的比例
>### 2. 留一交叉验证
>- 每次仅留出一个样本作为测试 其余样本用于训练 直到所有样本都被作为测试使用过一次
>### 3. K折交叉验证
>- 将数据分为k份使用k-1份作为训练集 1份作为测试集
## 3. 评估指标
### 1. 混淆矩阵
### 2. 分类准确率
### 3. 精确率
### 4. 召回率
### 5. F1分数
### 6. AUC-ROC曲线
## 4. 最近邻分类法
## 5. K近邻分类法
