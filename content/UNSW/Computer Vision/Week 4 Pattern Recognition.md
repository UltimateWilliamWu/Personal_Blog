## ⭐ 1. What is Pattern Recognition?

**Pattern recognition is the scientific discipline of recognizing patterns and regularities in data.**  
模式识别是一门识别数据中模式与规律的科学。

**In computer vision, this means deciding what is in an image.**  
在计算机视觉中，它表示对图像内容进行分类与识别。

---

## ⭐ 2. Pattern Recognition Applications

**Applications include image classification, text classification, speech recognition, activity detection, and recommendation systems.**  
应用包括图像分类、文本分类、语音识别、行为检测与推荐系统。

---

## ⭐ 3. Categories of Pattern Recognition

**Supervised learning uses labelled data to learn class boundaries.**  
监督学习使用带标签的数据学习类别边界。

**Unsupervised learning finds hidden patterns without labels.**  
无监督学习在无标签数据中挖掘结构。

**Semi-supervised learning combines labelled and unlabelled data.**  
半监督学习结合有标签和无标签数据。

**Weakly supervised learning uses weak or noisy labels.**  
弱监督学习使用噪声或不精确的标签。

---

## ⭐ 4. Key Concepts

**Objects are physical entities; regions represent segmented objects.**  
对象是图像拍摄的物体；区域是分割后对应物体的部分。

**Classes are groups of objects with common features.**  
类别是一组具有共同特征的对象。

**Labels indicate the class of an object.**  
标签用于指示对象所属类别。

**Classification assigns labels based on features.**  
分类根据特征给对象分配标签。

---

## ⭐ 5. Pattern Recognition Pipeline

**The typical pipeline is: acquisition → preprocessing → feature extraction → feature selection → learning → evaluation.**  
典型流程：采集 → 预处理 → 特征提取 → 特征选择 → 学习 → 测试。

---

## ⭐ 6. Feature Vectors

**A feature vector is $x = [x_1, x_2, …, x_d]$ describing an object's measurable properties.**  
特征向量是 $x = [x_1, x_2, …, x_d]$，描述对象可测量的属性。

**Features should be invariant to translation, rotation, lighting, and deformation.**  
特征应对平移、旋转、光照和形变具有不变性。

---

## ⭐ 7. Supervised Learning Overview

**Supervised learning learns a function $f : X \rightarrow Y$ mapping features to labels.**  
监督学习学习一个函数 $f : X \rightarrow Y$，将特征映射到标签。

---

## ⭐ 8. Generative vs Discriminative Models

**Generative models learn $p(x|y)$ and $p(y)$ to model how data is generated.**  
生成模型学习 $p(x|y)$ 和 $p(y)$ 来建模数据产生过程。

**Discriminative models directly learn the decision boundary between classes.**  
判别模型直接学习类别间的决策边界。

---

## ⭐ 9. Nearest Class Mean Classifier

**This classifier assigns a test sample to the class whose centroid is closest.**  
该分类器把样本分配给距离最近的类别中心。

**Centroid for class $k$ is $\mu_k = \frac{1}{|C_k|}\sum_{x \in C_k} x$.**  
类别 $k$ 的中心为 $\mu_k = \frac{1}{|C_k|}\sum_{x \in C_k} x$。

**Works well when classes are compact and separated.**  
适用于类内紧凑、类间分离的情况。

---

## ⭐ 10. K-Nearest Neighbours (KNN)

**KNN classifies a sample based on the majority class among its $K$ nearest neighbours.**  
KNN 根据最近的 $K$ 个邻居中占多数的类别进行分类。

**Uses Euclidean or Hamming distance.**  
使用欧氏距离或汉明距离。

**Non-parametric and no training phase.**  
非参数模型，无需训练。

---

## ⭐ 11. Bayesian Decision Theory

**Bayesian classification chooses the class with the highest posterior $p(c|x)$.**  
贝叶斯分类选择具有最大后验概率 $p(c|x)$ 的类别。

**Posterior is computed using Bayes Rule: $p(c|x) \propto p(x|c)p(c)$.**  
后验概率由贝叶斯公式计算：$p(c|x) \propto p(x|c)p(c)$。

---

## ⭐ 12. Bayesian Decision with Costs

**When different errors have different costs, choose class minimizing expected risk.**  
当不同错误代价不同，应选择期望风险最小的类别。

**Risk: $R(\alpha_i|x)=\sum_j \lambda(\alpha_i,c_j)p(c_j|x)$.**  
风险：$R(\alpha_i|x)=\sum_j \lambda(\alpha_i,c_j)p(c_j|x)$。

---

## ⭐ 13. Decision Trees

**Decision trees classify by asking a sequence of feature-based questions.**  
决策树通过一系列基于特征的问题进行分类。

**Nodes represent features; leaves represent class labels.**  
节点表示特征，叶子节点表示类别。

---

## ⭐ 14. Tree Construction

**At each node choose the feature with highest information gain.**  
每个节点选择信息增益最高的特征。

**Entropy: $H(y)=-\sum_i p(y_i)\log p(y_i)$.**  
熵：$H(y)=-\sum_i p(y_i)\log p(y_i)$。

**Information gain: $IG(S,f)=H(S)-H(S|f)$.**  
信息增益：$IG(S,f)=H(S)-H(S|f)$。

---

## ⭐ 15. Decision Tree Pros & Cons

**Pros: interpretable, supports categorical data, robust to missing values.**  
优点：可解释，支持分类数据，对缺失值鲁棒。

**Cons: overfits, only axis-aligned splits, greedy.**  
缺点：容易过拟合，分裂方向受限，贪婪算法。

---

## ⭐ 16. Ensemble Learning

**Ensemble learning combines multiple models to improve accuracy.**  
集成学习通过组合多个模型提高准确率。

---

## ⭐ 17. Random Forests

**Random forests build many decision trees and take the majority vote.**  
随机森林构建多棵决策树并对结果投票。

**Each tree is trained on bootstrapped samples and random features.**  
每棵树基于自助采样和随机选择特征训练。

**Reduces overfitting and improves generalization.**  
减少过拟合，提高泛化能力。

---

## ⭐ 18. Random Forest Theory

**Forest error decreases when tree correlation decreases and tree strength increases.**  
当树之间相关性降低、单棵树的分类能力增强时，森林误差会降低。

---

## ⭐ 19. Random Forest Pros & Cons

**Pros: accurate, robust, handles high-dimensional data and missing values well.**  
优点：准确、鲁棒、能处理高维和缺失数据。

**Cons: less interpretable and slower to train than a single tree.**  
缺点：不如单棵树可解释，训练较慢。

---

## ⭐ 20. Exam Question Key

**Correct statement: Increasing tree strength decreases the forest error rate.**  
正确陈述：增加单树的强度会降低随机森林的错误率。
![[Pasted image 20251117221211.png]]
对应选项为：
### ✔ **D**

