---
tags:
  - LectureNotes
---
## ⭐ What is Object Detection?

Object detection predicts **what** is in the image and **where** it is (bounding box).  
目标检测同时预测图像中的 **类别** 和 **位置**（框）。

It is harder than image classification because objects may appear in different sizes and locations.  
它比分类更难，因为目标大小与位置不固定。

---

# ⭐ 1. Detection vs Classification vs Segmentation

Image classification → one label per image.  
分类只给整张图一个标签。

Object detection → classify + localize bounding boxes.  
检测给出类别 + 框。

Semantic segmentation → label every pixel.  
语义分割给每个像素标标签。

Instance segmentation → separate object instances.  
实例分割区分同类不同物体。

---

# ⭐ 2. Detection Pipeline (Basic Idea)

Use a CNN to extract features and then predict class probabilities + bounding box coordinates.  
CNN 提取特征 → 预测类别与框。

Use Softmax loss for class; regression loss for bounding box.  
类别用 Softmax 损失；框用回归损失（如 L2）。

---

# ⭐ 3. IoU — Intersection over Union

IoU measures overlap between predicted and ground-truth boxes.  
IoU 衡量预测框与真值框的重叠程度。

Higher IoU → better localization.  
IoU 越高，定位越准。

Often require IoU > 0.5 to consider correct.  
通常 IoU > 0.5 算预测正确。

---

# ⭐ 4. Why is object detection hard?

Images contain multiple objects, all with different sizes, shapes, ratios.  
图中可能有多个物体，大小比例位置都不同。

The number of outputs is not fixed.  
输出数量不固定，这困难了深度模型。

Need both classification + localization.  
要同时做分类和定位。

---

# ⭐ 5. Early Detection Method: Sliding Window

Apply CNN on many crops at different scales and positions.  
在不同位置/尺度上滑动窗口，用 CNN 分类每个裁剪块。

Works but extremely slow.  
效果可以但非常慢。

Motivation for proposal-based methods.  
因此出现了 region proposal 方法。

---

# ⭐ 6. Region Proposal: Selective Search

Selective Search generates ~2000 region proposals likely to contain objects.  
Selective Search 生成约 2000 个“可能含有物体”的候选区域。

It is bottom-up: merge similar segments to propose regions.  
它是自底向上，通过合并相似区域生成候选框。

Used in R-CNN.  
是 R-CNN 的关键步骤。

---

# ⭐ 7. R-CNN（Region-based CNN）

R-CNN = Region proposals + CNN features + SVM classification.  
R-CNN = 区域候选 + CNN 特征 + SVM 分类。

Pipeline:

1. Generate 2000 region proposals
    
2. Warp each proposal
    
3. Feed each into CNN
    
4. Use SVM for classification + box regressor
    

流程：2k 区域 → CNN特征 → SVM 分类 + 框回归。

### Drawbacks

Very slow training & very slow testing.  
训练与推理都非常慢。

Requires storing features to disk (hundreds of GB).  
需要写大量特征到硬盘。

---

# ⭐ 8. SPP-Net（Spatial Pyramid Pooling）

SPP-Net uses spatial pyramid pooling to avoid resizing each region.  
SPP-Net 使用 spatial pyramid pooling 避免逐区域重采样。

Faster at test time but still multi-stage, not end-to-end.  
测试变快，但训练依然复杂，不是端到端。

---

# ⭐ 9. Fast R-CNN（End-to-End Region-based Detector）

Fast R-CNN processes entire image only once through CNN.  
Fast R-CNN 整张图只过一次 CNN。

Region proposals are cropped from feature maps using RoI Pooling.  
区域从特征图中用 RoI Pooling 进行裁剪。

Multi-task loss jointly trains classification + box regression.  
用多任务损失同时训练分类和框回归。

Much faster and more accurate than R-CNN.  
比 R-CNN 快得多、准得多。

---

# ⭐ 10. Problem: RoI Pooling Misalignment

RoI Pooling snaps to grid → tiny misalignment causes box inaccuracies.  
RoI Pooling 会网格对齐，导致轻微错位。

Solution: RoI Align (bilinear interpolation).  
解决：RoI Align（双线性插值）。

---

# ⭐ 11. Bottleneck: Region Proposals

Fast R-CNN is still slow because Selective Search is slow.  
Fast R-CNN 最大瓶颈不是 CNN，而是 Selective Search。

Need to improve region proposal generation.  
因此需要更快的候选区域生成方法。

---

# ⭐ 12. Faster R-CNN（RPN + Fast R-CNN）

Faster R-CNN introduces **Region Proposal Network (RPN)**.  
Faster R-CNN 用 **RPN** 替换 Selective Search。

RPN slides over feature map → predicts:  
RPN 在特征图上滑动，预测：

- object / not object
    
- bounding box transform relative to anchor
    

输出是否是物体 + 框的偏移量。

### Anchor boxes

Predefined shapes at each location (scales × aspect ratios).  
Anchor 是预定义的多尺度、多长宽比框。

RPN + Fast R-CNN share convolutional features → end-to-end.  
RPN 与 Fast R-CNN 共享特征 → 真正端到端训练。

速度比 Fast R-CNN 快一个数量级。  
速度远超 Fast R-CNN。

---

# ⭐ 13. Non-Maximum Suppression (NMS)

Many predicted boxes overlap heavily.  
模型输出许多重叠框。

NMS keeps only the most confident one and removes others with IoU > threshold.  
NMS 保留最高置信度框，去掉 IoU > 阈值的重叠框。

Essential for all detectors.  
几乎所有检测器都依赖它。

---

# ⭐ 14. One-stage Detectors（Proposal-free）

One-stage detectors skip region proposal and directly predict boxes over dense locations.  
一阶段方法跳过候选区域，直接在密集位置预测框。

Much faster but historically less accurate.  
速度快，但传统上准确率稍低。

Examples:  
YOLO, SSD, RetinaNet.  
代表方法：YOLO、SSD、RetinaNet。

---

# ⭐ 15. SSD（Single Shot MultiBox Detector）

SSD uses small convolution filters on multiple feature maps.  
SSD 在多尺度特征图上用小卷积核预测类别和框。

Detects at multiple scales → good for different sized objects.  
通过多尺度检测处理不同大小的物体。

Data augmentation is crucial.  
数据增强非常重要。

More default boxes = better detection.  
更多默认框更好。

---

# ⭐ 16. YOLO（You Only Look Once）

YOLO reframes detection as a single regression problem.  
YOLO 将检测重定义为一次性回归任务。

One forward pass predicts all boxes + classes.  
一次前向就预测所有框+类别。

Extremely fast.  
速度非常快。

Grid predicts class and bounding box.  
网格单元预测类别与框。

YOLO is end-to-end and real-time.  
YOLO 完全端到端且实时。

---

# ⭐ 17. Why early one-stage detectors were less accurate?

They suffer from extreme class imbalance (too many background cells).  
一阶段模型背景样本过多 → 类别不平衡。

Two-stage detectors have built-in filtering through proposals.  
两阶段模型通过 proposals 过滤背景。

---

# ⭐ 18. RetinaNet（One-stage but accurate）

RetinaNet = FPN + Focal Loss.  
RetinaNet = FPN + Focal Loss。

### Focal Loss

Down-weights easy negatives → focuses on hard examples.  
减少简单负样本的影响 → 专注难样本。

Solves the class imbalance issue.  
解决一阶段检测的类别不平衡问题。

---

# ⭐ 19. Feature Pyramid Network (FPN)

FPN combines high-level semantic features with low-level spatial details.  
FPN 结合高语义低分辨率与高分辨率低语义特征。

Generates multi-scale feature maps with strong semantics.  
生成多尺度、语义强的特征图。

Used extensively in modern detectors.  
现代检测器几乎都在用。

---

# ⭐ Summary

Two-stage (R-CNN family)  
Region proposals → classify proposals  
代表：R-CNN → Fast R-CNN → Faster R-CNN

One-stage (YOLO, SSD, RetinaNet)  
No proposals → directly regress boxes

RPN generates anchors + objectness + box offsets.  
RPN 预测 anchor 的 objectness 和偏移量。

YOLO is the fastest; RetinaNet is best among one-stage.  
YOLO 最快；RetinaNet 是一阶段里最准确的。

FPN provides multi-scale features.  
FPN 用于多尺度特征。

Focal Loss solves class imbalance.  
Focal Loss 解决类别不平衡。

NMS removes redundant boxes.  
NMS 去除冗余框。

## ⭐ Semantic Segmentation

Semantic segmentation classifies every pixel in an image.  
语义分割为图像中每个像素分配类别标签。

Uses ground-truth masks for supervision.  
训练需要对应的像素级标注 mask。

---

## ⭐ Sliding Window (Patch-based Segmentation)

The sliding window approach classifies pixels using local patches.  
滑动窗口通过局部 patch 来分类像素。

It is inefficient because overlapping patches do not share computation.  
效率极低，因为重叠区域无法复用特征。

---

## ⭐ Why sliding window fails?

Sliding window sees only local context and misses global information.  
滑窗只能看到局部，缺乏整体语义信息。

Deep networks need the whole image to understand object shapes.  
深度网络需要全图语义才能分割形状。

---

# ⭐ Fully Convolutional Networks (FCN)

## ⭐ FCN Idea

FCNs replace fully-connected layers with convolution layers to output pixel-wise predictions.  
FCN 去掉全连接层，用卷积直接输出像素对应的预测图。

This gives output the same spatial size as the input.  
输出尺寸和输入图像一致。

---

## ⭐ FCN Problem

Convolving on full-resolution images is computationally expensive.  
在原图分辨率上全卷积计算非常昂贵。

---

## ⭐ FCN Solution: Downsampling + Upsampling

FCN downsamples using pooling/stride and upsamples using unpooling or transpose convolution.  
FCN 使用下采样（池化/步幅卷积）和上采样（反池化/反卷积）构建端到端网络。

This preserves semantic features while recovering full resolution.  
这样既能提取深层语义又能恢复空间分辨率。

---

# ⭐ Upsampling Methods

## ⭐ Nearest-neighbour Upsampling

Nearest-neighbour repeats pixels to enlarge the feature map.  
最近邻通过复制像素来放大特征图。

Simple but may cause blocky artifacts.  
简单但可能导致块状伪影。

---

## ⭐ Unpooling

Unpooling restores pooled locations using max-pooling indices.  
反池化使用池化记录的位置恢复特征图。

Helps recover spatial structure.  
能更好地恢复空间结构。

---

## ⭐ Transpose Convolution (Deconvolution)

Transpose convolution learns upsampling weights to reconstruct higher resolution features.  
反卷积通过学习的卷积核进行上采样。

It is the default learnable upsampling method in segmentation networks.  
是大部分分割网络的标准可学习上采样方式。

---

# ⭐ U-Net

## ⭐ U-Net Architecture

U-Net has a contracting path for context and an expanding path for precise localization.  
U-Net 包含下采样编码器（提取语义）和上采样解码器（定位边界）。

Skip-connections pass high-resolution details from encoder to decoder.  
跳跃连接传递高分辨率细节到解码端。

---

## ⭐ Why U-Net works so well?

Skip connections combine global semantics + local detail.  
跳跃连接结合全局语义与局部细节。

This makes U-Net ideal for medical and dense segmentation.  
U-Net 对医学图像和密集分割非常有效。

---

## ⭐ U-Net Variants

### **Attention U-Net**

Adds attention to select important encoder features.  
加入注意力机制以选择重要特征。

### **ResU-Net**

Adds residual blocks for deeper and more stable training.  
加入残差结构以稳定深层训练。

### **TransUNet**

Uses Transformers as encoders for stronger global context.  
用 Transformer 作为编码器增强全局理解。

---

# ⭐ Instance Segmentation

## ⭐ Instance Segmentation Definition

Instance segmentation separates different object instances in the same class.  
实例分割区分同类中的不同个体。

It predicts a class label + bounding box + pixel mask for each object.  
每个物体同时预测类别、框和像素级掩膜。

---

# ⭐ Mask R-CNN

## ⭐ What is Mask R-CNN?

Mask R-CNN extends Faster R-CNN by adding a mask prediction branch.  
Mask R-CNN 在 Faster R-CNN 基础上增加分割 mask 分支。

It outputs one binary mask per detected object.  
为每个检测到的物体输出一个独立的二值 mask。

---

## ⭐ RoIAlign (Very Important!)

RoIAlign uses bilinear interpolation to avoid misalignment from quantization.  
RoIAlign 使用双线性插值避免 RoIPool 的量化误差。

This preserves per-pixel accuracy needed for masks.  
保证掩膜预测所需的像素级对齐。

---

## ⭐ Mask R-CNN Loss

Mask R-CNN uses a multi-task loss combining class, box, and mask losses.  
Mask R-CNN 使用分类、框回归、掩膜三者联合的损失。

This enables joint end-to-end training.  
实现端到端联合训练。

---

# ⭐ Video Understanding

## ⭐ What makes video harder than images?

Videos require spatial + temporal understanding over many frames.  
视频需要结合空间与时间信息进行分析。

Full videos are huge so models train on short clips.  
视频量巨大，因此通常在短片段上训练。

---

# ⭐ Video Classification Baseline

## ⭐ Frame-based CNN

Apply 2D CNN on each frame and fuse results (early/mid/late fusion).  
对每帧用 CNN，然后多帧融合（早/中/晚融合）。

Strong baseline but ignores motion explicitly.  
强基线，但无法显式捕获运动信息。

---

# ⭐ 3D CNN

## ⭐ 3D Convolution Idea

3D CNN uses 3D kernels to learn spatiotemporal features jointly.  
3D CNN 使用三维卷积同时学习空间+时间特征。

Captures motion patterns directly.  
能直接捕获运动行为。

---

## ⭐ C3D Model

C3D applies several layers of 3×3×3 3D convolutions and pools over space-time.  
C3D 使用多层 3×3×3 三维卷积，并在时空上池化。

It learns both appearance and motion.  
同时学习外观和运动信息。

---

# ⭐ Optical Flow

## ⭐ Motion-only Information

Optical flow computes pixel movement between consecutive frames.  
光流计算相邻视频帧之间的像素移动。

Represents motion as a 2D displacement field.  
将运动表示为二维运动向量场。

---

## ⭐ Why optical flow helps?

It removes background noise and focuses the model on motion.  
光流过滤背景影响，使模型专注运动特征。

Used heavily in action recognition.  
在动作识别中极为常用。

---

# ⭐ Two-Stream Network

## ⭐ Spatial + Temporal Streams

Two-stream networks process RGB images and optical flow separately.  
双流网络分别处理 RGB（外观）与光流（运动）信息。

The model fuses both to classify actions.  
融合两者以识别动作类别。

---

# ⭐ Transformers for Video

## ⭐ TimeSformer

TimeSformer applies self-attention over space and time with no convolutions.  
TimeSformer 用纯 self-attention 学习时空特征，不用卷积。

Provides strong global reasoning for long videos.  
能对长序列视频建模全局结构。

---

## ⭐ ViViT

ViViT extends Vision Transformers to video by splitting videos into tubelets.  
ViViT 将视频切成小 tubelet，再用 Transformer 处理。

Uses factorized spatial/temporal attention to reduce cost.  
通过空间-时间分解注意力降低计算成本。

---

# ⭐ Summary（你考试需要背的）

Semantic segmentation = pixel classification.  
语义分割就是对每像素分类。

FCN uses downsample + upsample to produce full-resolution predictions.  
FCN 用下采样+上采样做像素级预测。

U-Net adds skip-connections for precise segmentation.  
U-Net 的跳跃连接提供细节+语义结合。

Instance segmentation = detection + per-object masks.  
实例分割 = 检测 + 每个物体独立 mask。

Mask R-CNN adds mask head + uses RoIAlign.  
Mask R-CNN 增加 mask 分支且使用 RoIAlign。

Video understanding needs spatial + temporal modeling.  
视频理解需要同时处理空间与时间特征。

Two-Stream = RGB + optical flow.  
双流网络 = 外观 + 运动。

C3D and 3D CNN capture spatiotemporal features jointly.  
3D CNN 同时捕获时空特征。

TimeSformer / ViViT use Transformers for long-term video reasoning.  
TimeSformer 与 ViViT 用 Transformer 做视频时空建模。
