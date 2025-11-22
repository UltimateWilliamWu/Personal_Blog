---
tags:
  - LectureNotes
---

# ⭐ 1. Why do we need feature representation?

**Image features are compact vectors representing important visual information.**  
图像特征是压缩后的向量，用来表达图像中的重要视觉信息。

**Raw pixel values are unstable (lighting, rotation, viewpoint) and extremely redundant.**  
原始像素不稳定（光照、角度、视角变化）且冗余量巨大。

**Features provide robustness, descriptiveness, and efficiency.**  
特征向量提供鲁棒性、描述性和高效性。

---

## ⭐ Desirable properties of features

**Robustness: should appear in the same location under illumination/viewpoint changes.**  
鲁棒性：在不同光照与视角下应仍可被识别。

**Descriptiveness: similar structures should produce similar features.**  
描述性：相似结构应产生相似的特征。

**Efficiency: fewer and smaller features are better.**  
高效性：特征越少、越小越好。

---

## ⭐ Applications requiring feature representation

**Object detection, segmentation, classification, retrieval, stitching, tracking.**  
对象检测、图像分割、分类、检索、拼接、跟踪都需要特征。

---
# ⭐ 2. Major Categories of Image Features
图像特征分三类：

1. **Colour features（颜色）**
    
2. **Texture features（纹理）**
    
3. **Shape features（形状）**（Part 2）
    

下面总结本周的两大重点：颜色与纹理。

---
# ⭐ 3. Colour Features
## ⭐ Why use colour features?

**Colour is easy to compute and invariant to scaling, translation, and rotation.**  
颜色计算简单，对缩放、平移、旋转具有不变性。

---

## ⭐ Colour Histogram

**A colour histogram represents the global distribution of colours in each channel (R, G, B).**  
颜色直方图表示每个通道（R、G、B）的全局颜色分布。

**Final feature vector = concatenation of all channel histograms.**  
最终特征 = 各通道直方图拼接。

**High representation capability but high dimension.**  
表达能力强但维度高。

---
## ⭐ Colour Moments

**Colour distributions can also be represented using statistical moments (per channel).**  
颜色分布也可通过统计矩来表示。

### Moments:

- **First moment (Mean):**  
    $$\mu_i = \frac{1}{N}\sum_{j=1}^{N} f_{ij}$$  
    第一阶矩（均值）
    
- **Second moment (Std):**  
    $$\sigma_i = \sqrt{\frac{1}{N}\sum_{j=1}^{N}(f_{ij}-\mu_i)^2}$$  
    第二阶矩（标准差）
    
- **Third moment (Skewness):**  
    $$s_i = \sqrt[3]{\frac{1}{N}\sum_{j=1}^{N}(f_{ij}-\mu_i)^3}$$  
    第三阶矩（偏度）
    

**Only 9 features total (RGB × 3 moments) → very compact.**  
总共 9 个特征，非常紧凑。

---

# ⭐ 4. Texture Features
**Texture describes patterns created by local variations in intensity.**  
纹理描述由局部亮度变化形成的图案特征。

---

### ⭐ 4.1 Haralick Texture Features (基于共生矩阵的经典纹理特征)
#### ⭐ Concept
**Haralick features quantify spatial relationships between pixel intensities.**  
Haralick 特征量化像素灰度之间的空间关系。

---

#### ⭐ Step 1: Build the Gray-Level Co-occurrence Matrix (GLCM)

**GLCM counts how often a pixel of gray level $i$ co-occurs with gray level $j$ at offset $(d, \theta)$.**  
共生矩阵统计灰度值 $i$ 与灰度值 $j$ 在偏移 $(d, \theta)$ 下共同出现的频率。

**Matrix size = $L \times L$ where $L$ is number of gray levels.**  
矩阵大小为 $L\times L$（图像的灰度等级数）。

---

#### ⭐ Step 2: Compute Haralick descriptors

**For each GLCM, compute statistical descriptors such as contrast, correlation, energy, homogeneity, etc.**  
对每个 GLCM 计算统计特征，如对比度、相关性、能量、同质性等。

**Used widely in medical imaging due to interpretability.**  
因可解释性高，在医学影像中广泛使用。

---

### ⭐ 4.2 Local Binary Patterns (LBP)
#### ⭐ Concept

**LBP describes local texture by thresholding neighbors against the center pixel.**  
LBP 通过将邻居像素与中心像素比较来描述局部纹理。

---

#### ⭐ Basic LBP procedure

1. **Divide image into cells (e.g., $16\times16$).**  
    将图像分成小块。
    
2. **For each pixel, compare its 8 neighbors to center pixel:**  
    若邻居 $<=$ 中心 → 写 1，否则写 0。
    
3. **Form an 8-bit binary number (0–255).**  
    得到一个 8 位二进制数。
    
4. **Build a 256-bin histogram per cell.**  
    每块生成一个 256 维直方图。
    
5. **Concatenate histograms → final LBP descriptor.**  
    拼接所有细胞直方图形成最终特征。
    

---

#### ⭐ LBP advantages

**LBP is fast, compact, and robust to monotonic illumination changes.**  
LBP 快速、紧凑，对光照单调变化有鲁棒性。

---

#### ⭐ Multiresolution LBP

**Vary radius and number of neighbors to capture texture at multiple scales.**  
通过改变半径和邻居数来提取多尺度纹理。

---

#### ⭐ Rotation-invariant LBP

**Rotate the 8-bit number bitwise and choose its minimum value.**  
将 LBP 的 8 位二进制模式循环位移，选最小数字 → 获得旋转不变性。

**Feature size reduces from 256 to 36.**  
特征维度从 256 大幅降到 36。

---
# ⭐ 5. Scale-Invariant Feature Transform (SIFT)
## ⭐ Concept

**SIFT captures distinctive keypoints that are invariant to scale, rotation, illumination, and viewpoint.**  
SIFT 提取对尺度、旋转、光照、视角变化具有不变性的关键点。

---

## ⭐ SIFT pipeline (4 stages)

### **1. Scale-space extrema detection**

**Find keypoints by detecting maxima/minima in Difference-of-Gaussian (DoG) images across scales.**  
在多尺度 DoG 图像中寻找极值点。

---

### **2. Keypoint localization**

**Reject low-contrast or poorly defined points by fitting a 3D quadratic model.**  
通过三维二次曲线拟合剔除低对比度与不稳定点。

---

### **3. Orientation assignment**

**Assign dominant orientation using gradient histograms → rotation invariance.**  
通过局部梯度直方图确定主方向，使特征旋转不变。

---

### **4. Keypoint descriptor (128D)**

**For each keypoint, build a $4\times4$ array of 8-bin gradient histograms.**  
对每个关键点，构建 $4\times 4$ 的 8-bin 梯度直方图。

**Final descriptor length = $4\times4\times8 = 128$.**  
最终特征长度 = 128 维。

---

## ⭐ SIFT applications

**Image matching, stitching, object recognition, localization.**  
图像匹配、拼接、目标识别、定位等。

---

#  ⭐ 6. Descriptor Matching
## ⭐ Nearest Neighbour Distance Ratio (NNDR)

**Use distances $d_1$ (closest) and $d_2$ (second closest) in feature space.**  
在特征空间中使用最近距离 $d_1$ 与次近距离 $d_2$。

**Reject match if $d_1/d_2 > 0.8$.**  
若 $d_1/d_2 > 0.8$ 则拒绝此匹配。

**Improves matching robustness significantly.**  
显著提升匹配鲁棒性。

---
# ⭐ 7. Spatial Transformations & Alignment
## ⭐ Types of transformations

Translation, rotation, scaling, affine, perspective.  
平移、旋转、缩放、仿射、透视。

---

## ⭐ Least-squares fitting

**Solve linear system $Ap=b$ to find transformation parameters.**  
通过解线性系统 $Ap=b$ 求空间变换参数。

---

## ⭐ RANSAC

**Used to estimate transformations when many outliers exist.**  
当数据中存在大量离群点时，用 RANSAC 求解空间变换。

**Randomly sample, solve, score inliers, repeat.**  
随机采样 → 求解 → 打分 → 重复。

---

# ⭐ Final Exam Summary (Super Short)
### **Colour**

Histogram = strong but large  
Moments = compact but weaker

### **Texture**

Haralick = GLCM statistics  
LBP = binary local pattern  
SIFT = scale/rotation invariant keypoints

### **Matching**

NNDR < 0.8

### **Alignment**

Least squares + RANSAC

B
![[Pasted image 20251117204730.png]]

---

# ⭐ 1. Shape Features（形状特征）

**Shape features describe an object’s geometry, outline, and boundary structure.**  
形状特征用于描述物体的几何结构、轮廓和边界信息。

**They are typically extracted after segmentation.**  
通常在图像分割之后提取。

---

# ⭐ 2. Basic Geometric Shape Features（基础几何形状特征）

### ✔ Convexity / Concavity（凸性 / 凹性）

**Convex shapes contain all line segments between interior points; concave shapes do not.**  
凸形物体包含内部任意两点间的直线；凹形物体则不满足。

### ✔ Convex Hull（凸包）

**The convex hull is the smallest convex region enclosing the object.**  
凸包是包围物体的最小凸区域。

### ✔ Convex Deficiency（凸缺陷）

**Convex deficiency = convex hull area − actual object area.**  
凸缺陷 = 凸包面积 − 物体面积。

### ✔ Circularity（圆度）

**Circularity = $4\pi A / P^2$ (equals 1 for a perfect circle).**  
圆度 = $4\pi A / P^2$（完美圆的值为 1）。

### ✔ Eccentricity（偏心率）

**Eccentricity = minor axis / major axis of the fitted ellipse.**  
偏心率 = 拟合椭圆的短轴 / 长轴。

### ✔ Elongation（细长度）

**Elongation = length / width of the bounding rectangle.**  
细长度 = 外接矩形的长宽比。

---

# ⭐ 3. Boundary Descriptors（边界描述子）

### ✔ Chain Code

**Represents boundary as a sequence of directional codes.**  
链码用方向序列表示物体边界。

### ✔ Curvature（曲率）

**Curvature measures how sharply the boundary bends.**  
曲率描述边界在某点的弯曲程度。

- 凸曲率为正
    
- 凹曲率为负
    

### ✔ Bending Energy / Absolute Curvature

**Bending energy = $\int \kappa(s)^2 ds$, smallest for circles.**  
弯曲能量 = $\int \kappa(s)^2 ds$，圆形最小。

**Absolute curvature = $\int |\kappa(s)| ds$, convex shapes have minimum $2\pi$.**  
绝对曲率 = $\int |\kappa(s)| ds$，凸形物体最小值 $2\pi$。

### ✔ Radial Distance Descriptor

**Record distance from each boundary point to the centroid.**  
记录边界每个点与重心的距离。

**Normalize by maximum distance for scale invariance.**  
通过最大距离归一化实现尺度不变性。

---

# ⭐ 4. Shape Context（形状上下文）

**Shape Context is a powerful descriptor for comparing two shapes point-by-point.**  
Shape Context 是一种强大的逐点形状比较方法。

### ✔ How it works

1. 在边界上采样 $n$ 个点
    
2. 每个点对其他点做 log-polar 直方图
    
3. 每个直方图就是该点的 shape context 特征
    

### ✔ Matching

**Use histogram distances + Hungarian algorithm to match points.**  
通过直方图距离 + 匈牙利算法匹配形状点。

**Then estimate transformation with least squares or RANSAC.**  
再用最小二乘或 RANSAC 求变换。

---

# ⭐ 5. Bag-of-Words (BoW)

**BoW converts many local features (e.g., SIFT) into one global histogram.**  
BoW 将大量局部特征（如 SIFT）转换为一个全局直方图。

### ✔ Step 1: Build Visual Vocabulary

- 从训练图提取 SIFT
    
- 用 k-means 聚类得到 $k$ 个簇 → 视觉词汇
    

### ✔ Step 2: Encode Image

- 将每个 SIFT 匹配到最近的“视觉词”
    
- 统计词频 → 得到 $k$ 维直方图（即图像特征）
    

---

# ⭐ 6. Histogram of Oriented Gradients (HOG)

**HOG describes shape by accumulating gradient orientation histograms.**  
HOG 通过累积梯度方向直方图来描述形状。

### ✔ How HOG works

1. 计算梯度方向与幅度
    
2. 按 cell 累积方向直方图
    
3. 按 block 归一化以获得光照不变性
    
4. 拼接所有 block histogram → HOG 特征
    

**Widely used for pedestrian detection.**  
广泛用于行人检测。

---

# ⭐ 7. Final Exam Summary（超级精简版）

- **几何特征**：圆度、偏心率、细长度、凸包、凸缺陷
    
- **边界特征**：链码、曲率、径向距离
    
- **Shape Context**：点到点的 log-polar 分布直方图
    
- **BoW**：k-means 视觉词 + 直方图
    
- **HOG**：局部梯度方向直方图（行人检测经典）
    

---
![[Pasted image 20251117210154.png]]
选B
