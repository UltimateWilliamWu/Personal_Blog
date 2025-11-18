---
tags:
  - LectureNotes
---
# Part 1
## ⭐ What is Image Segmentation?

Image segmentation partitions an image into meaningful regions.  
图像分割将图像划分成有意义的区域以便进一步分析。

It is one of the oldest and most important tasks in computer vision.  
分割是计算机视觉历史最悠久、应用范围最广的核心问题之一。

---

## ⭐ Criteria for Good Segmentation

Regions should be homogeneous in some property (intensity, color, texture).  
分割区域内部应尽量均匀（亮度/颜色/纹理等）。

Adjacent regions should differ significantly in those properties.  
相邻区域应在这些特征上显著不同。

Boundaries should be smooth and spatially accurate.  
边界应光滑且位置准确。

Real images rarely satisfy all these perfectly.  
但实际图像往往达不到这些理想条件。

---

## ⭐ Segmentation vs Other Tasks

Image classification → one label for the whole image.  
分类给整张图一个标签。

Object localization → predict bounding boxes.  
定位预测物体框。

Semantic segmentation → label each pixel with a class.  
语义分割为每个像素标类别。

Instance segmentation → separate different object instances.  
实例分割区分同类中不同个体。

---

## ⭐ Segmentation Challenges

No single method works for all applications.  
没有一种万能的分割方法。

Images in the same domain can still vary widely.  
同一应用领域的图像差异也可能很大。

Domain knowledge is often necessary.  
通常需要结合领域知识。

---

# ⭐ **Basic Segmentation Methods**

---

## ⭐ Thresholding

Thresholding separates pixels by intensity.  
阈值法根据灰度分割前景和背景。

Works if classes have distinct intensity distributions.  
适用于目标与背景亮度差异明显的情况。

Fails when distributions overlap.  
若直方图重叠则难以分割。

---

## ⭐ K-means Clustering

K-means groups pixels into K clusters based on similarity.  
K-means 根据像素特征相似性聚类成 K 类。

Works only when K is known and clusters are distinct.  
适合已知类别数且类分布分明的情况。

Fails when K is unknown or clusters are irregular.  
当 K 未知或类形状复杂时效果差。

---

## ⭐ Feature-based Pixel Classification

Extract a patch around each pixel and compute features; train a classifier.  
为每个像素取邻域 patch 提取特征并用分类器预测类别。

Requires many training examples.  
需要大量标注数据。

Works well with powerful classifiers.  
适合深度学习前的传统方法框架。

---

# ⭐ **Advanced Segmentation Methods**

---

## ⭐ 1. Region Splitting and Merging

Split image recursively based on local statistics.  
根据局部统计不断拆分图像。

Merge similar regions recursively.  
合并相似区域。

Combines both for hierarchical segmentation.  
结合两者实现层级式分割。

---

## ⭐ Connectivity & Connected Components

Connectivity defines neighborhood relations (4/8 for 2D; 6/18/26 for 3D).  
连通性定义像素邻域（2D 中 4/8 连通；3D 中 6/18/26）。

Connected component labeling assigns each region a unique ID.  
连通域标记为每个连通区域分配标签。

Number of objects depends on connectivity definition.  
物体数量受连通性定义影响。

---

## ⭐ Region Growing

Choose a seed point and add neighboring pixels if they are similar.  
选取种子像素，加入与其相似的邻域像素。

Grows until no more similar pixels exist.  
直到没有更多相似像素为止。

Produces smooth, connected regions.  
常得到连贯且较平滑的区域。

---

## ⭐ 2. Watershed Segmentation

Treat image as a topographic surface; fill basins with water.  
将图像视为地形，用“注水”方式分割盆地。

Watershed lines are segmentation boundaries.  
水坝的位置即为分割边界。

Sensitive to noise; many local minima cause oversegmentation.  
对噪声敏感，局部极小点多会导致过分割。

Requires smoothing (preprocessing) or basin merging (postprocessing).  
通常需通过平滑或后处理减少错误分割。

---

## ⭐ 3. Maximally Stable Extremal Regions (MSER)

Apply many thresholds and find regions whose shapes remain stable.  
尝试多个阈值，找出形状稳定的区域。

Good for blob detection and text detection.  
常用于 blob 提取、文字区域检测。

---

## ⭐ 4. Mean Shift Segmentation

Mean shift finds modes (peaks) in feature density.  
Mean shift 在特征密度中寻找峰值（模态）。

Does not require knowing number of clusters.  
无需预先设定 K。

Robust to outliers but computationally expensive.  
抗噪强，但计算开销大。

Used for color/texture segmentation.  
常用于颜色/纹理分割。

---

## ⭐ 5. Superpixel Segmentation (SLIC)

Superpixels group similar pixels → faster subsequent processing.  
Superpixel 把相似像素合成小块，加速后续操作。

SLIC uses color + spatial distance.  
SLIC 使用颜色 + 空间距离生成超像素。

Produces compact, boundary-preserving superpixels.  
生成紧致且贴合边界的超像素。

---

## ⭐ 6. Conditional Random Field (CRF)

Build a graph of superpixels: nodes = superpixels, edges = adjacency.  
CRF 构建超像素图：节点为超像素，边表示邻接关系。

Unary potential → likelihood of each pixel’s label.  
单势能：该像素属于某类别的置信度。

Pairwise potential → encourages smooth, consistent labels.  
对势能：鼓励邻域标签一致。

Segmentation = minimizing total energy via graph cut.  
最终通过图割最小化能量实现分割。

---

## ⭐ 7. Active Contour (Snakes)

Fit a curve to object boundaries using energy minimization.  
通过能量最小化将曲线贴合到物体边缘。

Uses internal smoothness + external image forces.  
结合内部光滑项与图像梯度等外部力。

Sensitive to initialization and cannot handle topology changes.  
对初始位置敏感，难处理拓扑变化。

---

## ⭐ 8. Level-Set Segmentation

Represent contour implicitly as zero level of a 3D function.  
将轮廓表示为三维函数的零水平集。

Can naturally split/merge shapes; handles topology changes well.  
可自然处理形状分裂、合并等拓扑变化。

More computationally demanding.  
计算量较大。

---

# ⭐ **Evaluating Segmentation**

---

## ⭐ Pixel-level classification

TP = correctly predicted object pixels  
TP：正确预测为物体的像素  
FN = object missed  
FN：漏检  
FP = background wrongly predicted as object  
FP：误检  
TN = correctly predicted background  
TN：正确预测背景

---

## ⭐ Sensitivity & Specificity

Sensitivity (TPR):  
$$TPR = \frac{TP}{TP+FN}$$  
敏感度，表示正确检测的比例。

Specificity (TNR):  
$$TNR = \frac{TN}{TN+FP}$$  
特异度，表示背景准确率。

---

## ⭐ ROC Curve & AUC

Plot TPR vs FPR (1 – specificity).  
ROC 曲线绘制 TPR 对 FPR。

Higher AUC → better segmentation method.  
AUC 越大，分割越好。

---

## ⭐ Precision, Recall, F1

Precision:  
$$P = \frac{TP}{TP+FP}$$  
查准率：预测为物体中有多少是真的。

Recall:  
$$R = \frac{TP}{TP+FN}$$  
查全率：真实物体有多少被找到。

F1:  
$$F1=\frac{2PR}{P+R}$$  
PR 的调和平均。

---

## ⭐ Jaccard (IoU) & Dice

Jaccard (IoU):  
$$J = \frac{TP}{TP+FP+FN}$$  
交并比，表示正确像素占联合区域比例。

Dice:  
$$D = \frac{2TP}{2TP+FP+FN}$$  
Dice 系数，IoU 的对称版本。

---

# ⭐ Example Exam Question (Understanding Connectivity)

“How many objects are there with 4-connectivity?”  
考点：连通性影响物体数量。
![[Pasted image 20251118134207.png]]
