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

# ## ⭐ Final Exam Summary (Super Short)
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
