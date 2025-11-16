## 1. Image Processing Basics（图像处理基础）

**EN:**  
Image processing modifies or enhances an image to make it suitable for further analysis.

**CN:**  
图像处理的目的，是让图像更适合分割、检测、识别等进一步分析。

---

## 2. Point Operations（点操作）

**EN:**  
Point operations transform each pixel independently:  
g(x,y) = T(f(x,y))

**CN:**  
点操作对每个像素独立执行转换，不考虑邻域。  
公式：g(x,y) = T(f(x,y))

---

## 3. Types of Point Operations（点操作类型）

### 3.1 Contrast Stretching（对比度拉伸）

**EN:**  
Linearly expands a narrow intensity range into the full range.

**CN:**  
把窄灰度区间线性拉伸到整个范围，提高对比度。

---

### 3.2 Thresholding（二值化）

**EN:**  
Below threshold → 0; above → 255.

**CN:**  
阈值以下变黑，以上变白。

**Otsu:**  
EN: maximizes inter-class variance.  
CN: 最大化类间方差。

**IsoData:**  
EN: iteratively updates threshold.  
CN: 迭代更新均值直到收敛。

---

### 3.3 Intensity Inversion（灰度反转）

**EN:**  
g = L_max - f

**CN:**  
亮变暗、暗变亮。

---

### 3.4 Log Transform（对数变换）

**EN:**  
Enhances low intensities, compresses high intensities.

**CN:**  
增强暗部、压缩亮部。

---

### 3.5 Power (Gamma) Transform（幂次/伽马变换）

**EN:**  
g = c r^γ  
γ<1 → brightens; γ>1 → darkens

**CN:**  
γ<1 变亮，γ>1 变暗；用于曝光校正。

---

### 3.6 Piecewise Linear Transform（分段线性变换）

**EN:**  
Custom mapping using multiple linear segments.

**CN:**  
可设计多个线性段的灵活变换。

---

### 3.7 Gray-Level Slicing（灰度切片）

**EN:**  
Highlights a specific intensity range.

**CN:**  
突出特定灰度段。

---

### 3.8 Bit-Plane Slicing（位平面分解）

**EN:**  
Decomposes image into bit-planes.

**CN:**  
将图像分成 8 个二进制平面，高位表示结构，低位表示细节/噪声。

---

## 4. Intensity Histogram（强度直方图）

**EN:**  
Histogram = frequency distribution of pixel intensities.

**CN:**  
直方图表示每个灰度值出现多少次。

---

### 4.1 Histogram Equalization（直方图均衡化）

**EN:**  
Uses the CDF to obtain a more uniform histogram.

**CN:**  
利用累积分布函数使直方图更均匀，提高对比度。

---

### 4.2 Histogram Matching（直方图规定化）

**EN:**  
Matches an image histogram to a target distribution.

**CN:**  
将图像直方图变成目标直方图。

---

### 4.3 Histogram-Based Thresholding（基于直方图的阈值）

**EN:**  
Methods like Otsu, Triangle rely on histogram shape.

**CN:**  
如 Otsu、Triangle 等方法依赖直方图形状确定阈值。

---

## 5. Arithmetic & Logical Operations（算术与逻辑操作）

**EN:**  
Pixel-wise operations between two images.

**CN:**  
对两幅图逐像素运算。

---

### 5.1 Arithmetic Operations（算术）

**EN:**  
Addition, subtraction, multiplication, averaging.

**CN:**  
加法调亮，减法调暗，乘法增强对比度，平均降噪（噪声方差 σ²/N）。

---

### 5.2 Logical Operations（逻辑）

**EN:**  
AND / OR / XOR / NOT — commonly for masking.

**CN:**  
与/或/异或/非，多用于掩膜与区域提取。

---

## 6. Relationships（关系总结）

**EN:**  
- Histogram = indicator  
- Point ops = pixel-wise transformation  
- Arithmetic/logical = multi-image pixel ops  
- All modify histogram

**CN:**  
- 直方图 = 亮度和对比度的指标  
- 点操作 = 修改单像素  
- 算术逻辑 = 多图像像素操作  
- 都会改变直方图

---

## 7. Why Use Point Operations?（为何使用点操作）

**EN:**  
To adjust brightness/contrast and prepare images for segmentation, detection, recognition.

**CN:**  
为了调亮、调暗、增强对比度，让图像更适合分割、检测、识别。

---

## 8. Week1 Key Exam Points（考试高频点）

**EN:**  
- Contrast stretching is linear  
- Log expands low intensities  
- γ<1 brightens  
- HE uses CDF  
- Matching = CDF + inverse CDF  
- Otsu = maximize inter-class variance  
- Bit-plane high bits store structure  
- Averaging reduces noise variance  
- Arithmetic/logic are pixel-wise

**CN:**  
- 对比度拉伸是线性的  
- Log 增强暗部  
- γ<1 变亮  
- 均衡化用 CDF  
- 规定化 = CDF + 逆 CDF  
- Otsu 最大类间方差  
- 位平面高位是主要结构  
- 平均降噪 σ²→σ²/N  
- 算术/逻辑是逐像素操作

---

## 9. One-Sentence Final Summary（一句话总结）

**EN:**  
Week1 teaches intensity manipulation using point operations and histograms.

**CN:**  
Week1 核心是用点操作与直方图控制像素值，使图像更适合后续处理。

---

>[!note] Concept
>image formation occurs when a sensor registers radiation that has interacted with physical objects

>[!note] Projection Mathematics
>![[Pasted image 20251114132826.png]]

![[Pasted image 20251114133716.png]]
D

>[!important] Types of Image Processing
>- Spatial domain operations (in image space)
>	- Point operations (intensity transformations on individual pixels)
>	- Neighbourhood operations (spatial filtering on groups of pixels)
>- Transform domain operations (mainly in Fourier space)

![[Pasted image 20251116130020.png]]
B

