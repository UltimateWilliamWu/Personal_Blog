---
tags:
  - UNSW
  - UNSW/COMP9517
  - Topic/ComputerVision
  - Type/Lecture
---
# Part 1
## ⭐ Challenges in Computer Vision

Computer vision is hard due to variation in viewpoint, illumination, occlusion, and background clutter.  
计算机视觉困难因为视角变化、光照变化、遮挡、背景杂乱。

---

## ⭐ Traditional CV Pipeline

Early pipelines used hand-crafted features + manual classifiers.  
传统方法依赖手工特征和独立分类器。

Deep learning replaces all these steps with a single model.  
深度学习将整条管线合并到一个模型中学习。

---

# ⭐ Part 1 — From Linear Classifier → Neural Network

---

## ⭐ Linear Classifier

A linear classifier computes a weighted sum of the input.  
线性分类器使用输入特征的加权和进行分类。

It cannot handle non-linear patterns in images.  
它无法处理图像中的非线性模式。

---

## ⭐ Motivation for Non-linear Networks

Adding non-linear transformations allows more complex decision boundaries.  
加入非线性变换后，模型可学习复杂边界。

This leads to multi-layer neural networks.  
因此发展出多层神经网络。

---

## ⭐ Multi-layer Perceptron (MLP)

An MLP stacks layers of linear transforms followed by activation functions.  
多层感知机由线性层和激活函数堆叠而成。

More layers → more expressive power.  
层数增加 → 表达能力更强。

---

## ⭐ Importance of Activation Functions

Without activation functions, the entire network collapses to a linear model.  
没有激活函数，多层网络仍等价于单层线性模型。

ReLU is the most common activation due to simplicity and stable gradients.  
ReLU 是最常用激活函数，因为简单且梯度稳定。

---

## ⭐ Common Activation Functions

Sigmoid, tanh, ReLU, Leaky ReLU, Maxout, ELU.  
常见激活：Sigmoid、tanh、ReLU、Leaky ReLU、Maxout、ELU。

ReLU is a good default choice.  
ReLU 是默认首选。

---

# ⭐ Part 2 — What is Deep Learning?

---

## ⭐ What is Deep Learning?

Deep learning uses deep neural networks to learn hierarchical features from data.  
深度学习使用深层神经网络从数据中自动学习特征层次。

It usually requires large datasets and deeper architectures.  
深度学习通常依赖大数据集和更深层结构。

---

## ⭐ Deep Learning Paradigms

CNNs for images,  
RNNs for sequences,  
GANs for generation,  
Transformers for broad tasks.  
CNN 用于图像，RNN 用于序列，GAN 用于生成，Transformer 应用于多种任务。

---

## ⭐ Deep Nets Learn Hierarchical Features

Early layers learn edges; mid layers learn parts; deeper layers learn full objects.  
浅层学习边缘，中层学习部件，深层学习整体语义。

This is the core benefit of deep networks.  
这是深度网络的核心优势。

---

# ⭐ Part 3 — Convolutional Neural Networks (CNN)

---

## ⭐ What is a CNN?

CNNs are deep networks specialized for processing 2D/3D image data.  
CNN 是专门为图像/视频设计的深度神经网络。

They learn features automatically using convolutional filters.  
它们通过卷积滤波器自动学习特征。

---

## ⭐ Why CNN Works Well?

CNN learns spatial hierarchies: edges → shapes → objects.  
CNN 学习空间层次结构：边缘→形状→物体。

It is spatially invariant and efficient due to parameter sharing.  
因为共享参数，CNN 具有空间不变性且高效。

---

## ⭐ Traditional vs Deep Learning Pipeline

Traditional CV uses manual features;  
Deep learning directly learns features & classifier together.  
传统 CV 用人工特征；深度学习直接学习特征+分类器。

---

# ⭐ CNN Components（核心结构）

---

## ⭐ 1. Convolution Layer

A convolution layer applies multiple learnable filters to extract features.  
卷积层通过可学习的滤波器提取特征。

Each filter produces one feature map.  
每个滤波器生成一张特征图。

---

## ⭐ 2. ReLU Activation

ReLU keeps positive values and sets negatives to zero.  
ReLU 保留正值，负值置零。

It introduces non-linearity for deeper models.  
它提供非线性，使深层模型可训练。

---

## ⭐ 3. Pooling Layer

Pooling downsamples feature maps (max/avg).  
池化层对特征图下采样。

It makes the network more invariant and reduces computation.  
它增强位置不变性并降低计算量。

---

## ⭐ 4. Flattening

Flattening converts feature maps into a vector before FC layers.  
Flatten 将特征图转成一维向量，便于连接全连接层。

---

## ⭐ 5. Fully Connected Layers

FC layers combine high-level features to form final decisions.  
全连接层将高级特征组合用于最终分类。

Usually ends with a softmax classifier.  
最终使用 softmax 进行分类。

---

# ⭐ Convolution Parameters（卷积层参数）

---

## ⭐ Channels

Filters operate over depth (RGB channels).  
卷积核会对图像的通道维度进行处理。

Multiple filters → multi-channel outputs.  
多个卷积核→多通道输出。

---

## ⭐ Filter Size

Common sizes: 3×3, 5×5.  
常见卷积核：3×3 与 5×5。

Smaller filters preferred for efficiency and performance.  
小卷积核通常效果更好且计算更小。

---

## ⭐ Stride

Stride controls how far the filter moves.  
步幅控制卷积核移动距离。

Larger stride = smaller output feature map.  
步幅越大，输出越小。

---

## ⭐ Padding

Padding preserves spatial size by adding border pixels.  
填充通过加边界像素保持空间大小。

Useful when boundary information matters.  
边界信息重要时非常必要。

---

## ⭐ Dilation

Dilation increases receptive field without increasing kernel size.  
膨胀卷积可增大感受野而不增加参数量。

---

## ⭐ Activation in CNN

ReLU is standard for conv outputs.  
卷积层之后通常使用 ReLU。

---

# ⭐ Convolution Layer Interpretation

Each filter learns to detect a specific pattern (edge, texture, part).  
每个卷积核学习检测一种特定模式（边缘、纹理、形状）。

Activation maps indicate where the pattern appears in the image.  
特征图表示该模式在图像哪里出现。

Stacking filters forms rich hierarchical representation.  
堆叠卷积核能形成丰富的层级表示。

---

# ⭐ Receptive Field

Receptive field is the region of input that influences one neuron.  
感受野是影响一个神经元输出的输入区域。

Deeper layers have larger receptive fields.  
越深的层感受野越大。

---

# ⭐ Feature Map Size Formula（考试常考）

Output height × width：  
$$
(1 + (J + 2P - M)/s) \times (1 + (K + 2P - N)/s)
$$
J,K = input size; M,N = kernel size; P = padding; s = stride.

计算卷积输出大小的重要公式。

---

# ⭐ Key Takeaways

CNN learns features automatically and hierarchically.  
CNN 自动、分层地学习图像特征。

Convolution + ReLU + Pooling is the fundamental block.  
卷积 + ReLU + Pooling 是基本结构。

Deeper architectures → better performance.  
网络更深 → 表现更强。
