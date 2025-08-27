---
tags:
  - LectureNotes
---
## 1. Machine Learning Pipeline（学习路线）
![[Pasted image 20250224135530.png|1050]]
### 1）Data Preparation
clear all trash data and filter the useful data
### 2) Data Cleaning & Pre-processing

## 2. Supervised Learning vs Unsupervised Learning（监督学习与非监督学习）
The most widely used categories of machine learning algorithms are: 
- Supervised learning – output class (or label) is given o Unsupervised learning – no output class is given（给出结果集）
- Unsupervised learning – no output class is given（无结果集）
## 3. Regression（回归）
>[!important] Introduction
>- Regression predicts numeric values (e.g., house prices, temperatures). （回归监督学习用于预测数值）
>- while Classification predicts discrete values (e.g., spam vs. nonspam).（分类监督学习用于预测类别）
>- The “most typical” ML problem is supervised learning for classification; however, there are also tasks where we need to predict numeric values, so we use regression.
### 3.1 Linear Regression（线性回归）
如何找到一条函数曲线使得所有数据点都靠近这条函数，误差最小。
本质就是找到损失函数并对其求导得出最优解

>[!note] Loss Function 损失函数
>$$y_j​=θ_1​x_j​+θ_0$$​
>$\qquad$![[Pasted image 20250224145605.png|500]]
>$\qquad$损失函数值越小 说明曲线越拟合
>### Residual Sum of Square RSS 残差平方和
>简单理解就是误差平方总和
>$\qquad$![[Pasted image 20250218163950.png|525]]
>### Mean Squared error MSE 均方误差
>简单理解就是误差平方和的均值
>$\qquad$![[Pasted image 20250218165414.png|525]]

>[!note] “Ordinary Least Squares” (OLS) regression 最小二乘法
>$\qquad$令 $\frac{\partial J(\theta)}{\partial \theta}=0$ 可得：
>$$\theta=(X^TX)^{-1}X^Ty$$
>这个是最小二乘法闭式解
>本质是对损失函数求导使得导数等于0得到极值点的解

>[!note] Gradient Descent 梯度下降
>- Why using Gradient Descent?
>	- Because sometimes finding the minimum cost function cost too much
>- 为什么使用梯度下降？
>	- 因为有时候求线性回归的闭式解耗费太多，因此需要找到一种节省资源的优化算法
>- 什么是梯度？
>	- 对损失函数求导
>- 已知损失函数MSE, 对其泰勒展开可得:
>$$L(w+\Delta w)\approx L(w)+\nabla L(w)^T\Delta w$$
>$\Delta w=−\alpha \nabla L(w)$ 因为最佳移动方向是负梯度方向
>$\nabla L(w)$ 代表在w处的梯度
>- 梯度下降更新公式：
>![[Pasted image 20250412150332.png]]
>![[Pasted image 20250220091330.png|600]]
>1. Batch Gradient Descent:
>![[Pasted image 20250224164409.png|750]]
>2. Stochastic Gradient Descent:
>![[Pasted image 20250224164431.png|750]]
>