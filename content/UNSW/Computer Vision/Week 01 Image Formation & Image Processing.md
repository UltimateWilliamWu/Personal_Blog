---
tags:
  - UNSW
  - UNSW/COMP9517
  - Topic/ComputerVision
  - Type/Lecture
---
# 1. **What is Image Processing?**

**Image processing transforms an input image into an improved or more useful output image.**  
图像处理将输入图像转换成质量更高或更易分析的输出图像。

**It aims to suppress distortions and enhance relevant information.**  
目标是抑制噪声与畸变，同时增强关键信息。

**It prepares images for further tasks such as analysis or interpretation.**  
图像处理为后续的图像分析或视觉理解做预处理准备。

---

# 2. **Types of Image Processing**

**Spatial domain operations work directly on pixels in image space.**  
空间域操作直接基于像素值进行处理。

**Transform domain operations work on frequency representations (e.g., Fourier space).**  
变换域操作在频域（如傅里叶域）进行处理。

---

# 3. **Spatial Domain Operations**

**General form: 𝑔(x, y) = T(f(x, y))**  
通式：输出像素由操作符 T 作用到输入像素上。

**Point operations apply T to individual pixels independently.**  
点操作是对每个像素独立执行变换。

**Neighbourhood operations apply T to a set of pixels around each location.**  
邻域操作基于周围一小块区域的像素共同作用。

---

# 4. **Point Operations**

## ⭐ 4.1 Contrast Stretching

**Contrast stretching maps input intensities to a wider output range, increasing contrast.**  
对比度拉伸将输入灰度线性映射到更宽的区间，从而提升对比度。

**Values below L become black; values above H become white; values in [L, H] are stretched linearly.**  
低于 L 的输出为黑，高于 H 的输出为白，介于 L–H 之间的线性放大。

**✔ Exam Point:** Know the definition and linear mapping formula.  
✔ 考点：必须掌握定义与区间线性变换。

---

## ⭐ 4.2 Intensity Thresholding

**Thresholding produces a binary image by comparing pixel values to a threshold.**  
阈值化通过与阈值比较生成二值图像。

**Pixels < T → 0 (black); ≥ T → 1 (white).**  
小于阈值为 0，大于等于阈值为 1。

**It is a limiting case of contrast stretching.**  
这是对比度拉伸的极端特例。

**Works best when object and background intensities are clearly separated.**  
适用于前景与背景灰度差距大的情况。

**✔ Exam Point:** Purpose + binary output characteristics.  
✔ 考点：用途 + 二值化特性。

---

## ⭐ 4.3 Automatic Thresholding

### **Otsu’s Method**

**Otsu finds the threshold that maximizes inter-class variance (or minimizes intra-class variance).**  
大津法寻找使类间方差最大（或类内方差最小）的阈值。

**Formula: σ_B² = p₀ p₁ (μ₀ − μ₁)²**  
公式：类间方差等于两类概率与均值差平方的乘积。

**✔ Exam Point:** Remember what Otsu optimizes.  
✔ 考点：熟记“大津法最大化类间方差”。

---

### **IsoData Method**

**IsoData iteratively updates the threshold as the average of two class means.**  
IsoData 反复更新阈值，使其等于两类均值的平均。

**Converges to a threshold midway between class means.**  
最终阈值为两类均值的中点。

---

## ⭐ 4.4 Intensity Inversion

**Intensity inversion maps bright pixels to dark and dark pixels to bright (s = L − 1 − r).**  
灰度反转将亮变暗、暗变亮（s = L − 1 − r）。

**Useful for highlighting structures such as microcalcifications.**  
用于强调某些结构，例如医学图像中的钙化点。

---

## ⭐ 4.5 Log Transformation

**Log transform enhances low-intensity values and compresses high-intensity values.**  
对数变换增强暗部细节，压缩亮部范围。

**Formula: s = c log(1 + r)**  
公式：s = c log(1 + r)

**Often used to compress high dynamic range images (e.g., Fourier spectra).**  
常用于压缩高动态范围图像，如频谱。

---

## ⭐ 4.6 Power (Gamma) Transformation

**Power transform applies s = c r^γ, adjusting contrast based on γ.**  
幂次（伽马）变换根据 γ 改变图像亮度与对比度。

**γ < 1 brightens the image; γ > 1 darkens it.**  
γ<1 变亮，γ>1 变暗。

**Widely used in display gamma correction.**  
广泛用于显示器的伽马校正。

---

## ⭐ 4.7 Piecewise Linear Transformations

**Allows designing custom mappings with multiple linear segments.**  
可通过多段线性的方式设计更灵活的映射。

**Includes contrast stretching, intensity slicing, and more complex mappings.**  
包括对比度拉伸、灰度切片等方法。

---

## ⭐ 4.8 Gray-Level Slicing

**Highlights a specific range of gray values while suppressing others.**  
突出某个灰度区间，同时抑制其他区域。

**Two versions: binary highlighting or selective enhancement.**  
可采用二值方式或增强方式。

---

## ⭐ 4.9 Bit-Plane Slicing

**Separates an image into bit planes to analyze contributions of each bit.**  
将图像拆分为不同比特平面，用于观察不同比特对图像的贡献。

**Useful for compression and highlighting structures.**  
用于压缩与结构增强。

---

# 5. **Intensity Histogram**

**Histogram counts the number of pixels at each intensity level.**  
直方图统计每个灰度值的像素数。

**Normalized histogram becomes a probability distribution p(r).**  
归一化直方图代表像素灰度的概率分布。

---

## ⭐ Histogram-Based Thresholding (Triangle Method)

**Draw a line from histogram peak to the highest gray level; threshold is where the distance to the line is maximal.**  
从直方图峰值连线到最大灰度点，距离最大的位置为阈值。

---

# 6. **Histogram Processing**

## ⭐ 6.1 Histogram Equalization

**Histogram equalization aims to make intensity values uniformly distributed.**  
直方图均衡化使灰度值趋于均匀分布。

**Transformation uses the CDF: s = (L − 1) · CDF(r).**  
使用灰度累计分布函数进行映射。

**Enhances contrast near peaks of the histogram.**  
增强直方图峰值附近的对比度。

**✔ Exam Point:** Know CDF mapping formula.  
✔ 考点：CDF 公式必须掌握。

---

## ⭐ 6.2 Histogram Matching (Specification)

**Histogram matching produces an image with a specified target distribution.**  
直方图规定/匹配使图像达到指定的目标分布。

**Uses inverse CDF of the target histogram.**  
使用目标直方图的逆 CDF。

---

# 7. **Arithmetic & Logical Operations**

**Pixelwise addition and subtraction can blend images or detect changes.**  
逐像素加减用于图像融合或变化检测。

**Logical operations (AND, OR) apply masks to images.**  
逻辑操作用于掩膜处理。

**Averaging multiple noisy images reduces variance by a factor of 1/N.**  
对多个噪声图取平均可降低噪声方差至原来的 1/N。

**✔ Exam Point:** Noise reduction by averaging → variance = σ² / N**  
✔ 考点：平均降噪方差公式常考。

---

# 8. **Typical Exam Concepts**

**You must distinguish: contrast stretching vs thresholding vs log vs gamma.**  
必须区分：拉伸 / 阈值 / 对数 / γ。

**Otsu maximizes inter-class variance, not intra-class.**  
大津法最大化类间方差。

**Histogram equalization uses the CDF.**  
直方图均衡化基于 CDF。

**Bit-plane slicing relates to binary representation.**  
比特平面切片与像素二进制结构有关。

**Gamma < 1 brightens; Gamma > 1 darkens.**  
γ 值对亮度影响是必考点。

---
![[Pasted image 20251116143432.png|625]]

>[!faq] What is point Operations? Purpose? 
>- **Point operations are intensity transformations applied independently to each pixel in the image.**  
>点操作是对图像中每个像素独立进行的灰度/亮度变换。
>- **They do not consider neighbouring pixels—each output pixel depends only on its corresponding input pixel.**  
>它不会考虑邻域像素，每个输出像素仅由对应的输入像素决定。
>- **Common examples include contrast stretching, thresholding, inversion, log transform, and gamma transform.**  
>常见的点操作包括对比度拉伸、阈值化、反转、对数变换和伽马变换。
>- **Point operations are typically used for brightness correction, contrast manipulation, and image enhancement.**  
>点操作常用于亮度校正、对比度调整和图像增强。
>- **In formula form: g(x, y) = T(f(x, y)), where T acts on a single value.**  
>公式形式：g(x, y) = T(f(x, y))，其中 T 仅作用于单个像素值。

>[!faq] What is intensity histogram? What use? 
>- **An intensity histogram is a plot showing how many pixels in an image have each possible gray-level value.**  
强度直方图是一种统计图，用来表示图像中每个灰度值各有多少像素。
>- **It visualizes the distribution of brightness levels across the whole image.**  
它直观展示了图像整体亮度的分布情况。
>- **The histogram helps us understand whether an image is dark, bright, low-contrast, or high-contrast.**  
通过直方图可以判断图像偏暗、偏亮、对比度低或对比度高。
>- **For example, a histogram concentrated in the middle indicates low contrast, while one spread across the full range indicates high contrast.**  
如：直方图集中在中间说明对比度低，而分布很宽说明图像对比度高。
>- **Intensity histograms are used for tasks such as thresholding, contrast enhancement, histogram equalization, and histogram matching.**  
强度直方图可用于阈值选择、对比度增强、直方图均衡化、直方图匹配等任务。
>- **They provide essential statistical information for automatic segmentation methods (e.g., Otsu).**  
它们为自动分割方法（如大津法）提供必要的统计信息。
>- **In summary: the histogram is a diagnostic tool and a foundation for many image enhancement and segmentation algorithms.**  
总结：直方图既是分析图像质量的工具，也是许多图像增强与分割算法的基础。

> [!faq] What is arithmetic and logical operations? What for? 
> 
> **Arithmetic and logical operations are pixel-wise operations performed between two images or between an image and a mask.**  
> 算术与逻辑操作是在两幅图像之间，或图像与掩膜之间逐像素进行的操作。
> 
> 
> ## 🔹 **What They Are（是什么）**
> 
> **Arithmetic operations include addition, subtraction, multiplication, and averaging applied pixel-by-pixel.**  
> 算术操作包括逐像素加法、减法、乘法、平均等。
> 
> **Logical operations include AND, OR, XOR, applied bitwise to pixel values or masks.**  
> 逻辑操作包括逐位的 AND、OR、XOR 等，通常用于与掩膜(mask)共同使用。
> 
> 
> ## 🔹 **What They Do（干嘛的）**
> 
> **They combine or compare images at the pixel level to extract information, highlight differences, or apply region masks.**  
> 它们用于在像素层面组合图像、比较图像、提取差异，或应用区域掩膜。
> 
> 
> ## 🔹 **Purpose（目的）**
> 
> **The purpose is to manipulate multiple images jointly, remove noise, detect changes, isolate regions, or enforce binary logic.**  
> 目的在于将多幅图像联合处理、去噪、检测变化、提取特定区域，或进行二值逻辑判断。
> 
> 
> ## 🔹 **Uses / Applications（用途）**
> 
> ### **1. Image Addition / Subtraction（图像加减）**
> 
> **Used to blend images, enhance brightness, or detect differences between frames.**  
> 用于图像融合、调整亮度或检测两帧之间的差异。
> 
> 
> ### **2. Logical AND / OR（逻辑与/或）**
> 
> **Used to apply masks to keep or remove certain regions of an image.**  
> 用于应用掩膜以保留或去除图像的特定区域。
> 
> 
> ### **3. Averaging（多图平均）**
> 
> **Averages multiple noisy images to reduce noise because variance decreases as 1/N.**  
> 通过对多张噪声图像求平均降低噪声（方差缩减为 1/N）。
> 
> 
> ### **4. Change Detection（变化检测）**
> 
> **Subtraction between two frames highlights moving or changed objects.**  
> 通过帧差法检测运动物体或变化区域。
> 
> 
> ### **5. Bitwise Logic for Masks（基于掩膜的位运算）**
> 
> **AND keeps selected pixels; OR merges region masks.**  
> AND 用于保留特定区域；OR 用于合并多个区域。
> 
> 
> ## 🔹 **Why They Matter in Computer Vision（为什么重要）**
> 
> **They are fundamental tools for segmentation, region selection, noise reduction, motion analysis, and combining information across images.**  
> 它们是分割、区域选取、降噪、运动分析、图像组合等任务的核心工具。

![[Pasted image 20251114133716.png]]
D

![[Pasted image 20251116130020.png]]
B

