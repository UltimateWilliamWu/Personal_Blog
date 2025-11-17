# Part 1
## 1. **Neighbourhood Operations**

**Neighbourhood operations compute each output pixel using a small local region around the input pixel.**  
邻域操作通过输入像素周围的一个小区域来计算输出像素。

**This region is typically a 3×3, 5×5, or 7×7 square subimage.**  
该区域一般是 3×3、5×5 或 7×7 的邻域。

**The weights of this region form the kernel (or filter).**  
邻域中每个像素对应的权重组成“核（滤波器）”。

**Neighbourhood operations can smooth, sharpen, enhance, or detect features in an image.**  
邻域操作可以实现平滑、锐化、增强或特征检测等功能。

---

## 2. **Spatial Filtering by Convolution**

**Convolution computes the output o(x,y) = ΣΣ f(x−i, y−j) h(i, j).**  
卷积通过公式 o(x,y) = ΣΣ f(x−i, y−j) h(i,j) 来计算输出。

**The kernel is flipped before sliding over the image (definition of convolution).**  
根据卷积定义，核在滑动前需要“翻转”。

**Convolution is linear and shift-invariant.**  
卷积是线性且平移不变的操作。

**Because it is LSI, convolution behaves consistently across the entire image.**  
由于其 LSI 特性，卷积在整个图像范围内行为一致。

---

## 3. **The Border Problem and Fixes**

**Filtering near borders requires defining pixel values outside the image.**  
在边界进行滤波时需要定义图像外的像素如何处理。

**Common solutions include padding, clamping, wrapping, and mirroring.**  
常见方案包括零填充、边缘复制、循环复制和镜像扩展。

**Mirroring produces smooth boundaries and avoids artifacts.**  
镜像扩展可以避免伪影，是最佳边界处理方式之一。

---

## 4. **Properties of Convolution**

**Convolution satisfies commutativity, associativity, and distributivity.**  
卷积满足交换律、结合律和分配律。

**Convolution in spatial domain equals multiplication in frequency domain.**  
空间域卷积等价于频域中的乘法（下一周详细讲）。

---

## 5. **Uniform Smoothing (Mean Filter)**

**The mean filter replaces each pixel with the average of its neighborhood.**  
均值滤波将每个像素替换为邻域的平均值。

**It reduces noise but also blurs edges.**  
它可降噪但会导致边缘模糊。

**Uniform smoothing corresponds to a kernel filled with equal weights.**  
均值滤波对应的核是全 1 的均匀权重矩阵。

---

## 6. **Gaussian Filter**

**The Gaussian filter applies a weighted average with weights following a Gaussian distribution.**  
高斯滤波使用符合高斯分布的权重进行加权平均。

**It is separable and circularly symmetric, making it efficient and stable.**  
高斯滤波可分离且具有圆对称性，因此高效且稳定。

**It smooths images while preserving structure better than the mean filter.**  
它比均值滤波更能保留结构信息。

**Sigma (σ) controls the scale—the larger σ is, the stronger the blur.**  
σ 控制模糊强度，σ 越大模糊越明显。

---

## 7. **Median Filter**

**The median filter selects the median value within the neighborhood.**  
中值滤波选择邻域像素的中位数作为输出。

**It removes salt-and-pepper noise without smoothing edges.**  
它能移除椒盐噪声，同时保持边缘清晰。

**It is nonlinear (not a convolution operation).**  
它是非线性的，因此不是卷积。

---

## 8. **Gaussian vs Median Filtering**

**Gaussian filtering preserves small structures but blurs noise gradually.**  
高斯滤波能保留小结构，但对噪声的处理较柔和。

**Median filtering completely removes impulse noise but may erase small objects.**  
中值滤波对脉冲噪声非常有效，但可能删除小目标。

---

## 9. **Sharpening by Unsharp Masking**

**Unsharp masking enhances high-frequency components by adding back (Input − Blurred).**  
反锐化（Unsharp Masking）通过增强高频成分 (原图 − 平滑图) 来提高锐度。

**This boosts edges and fine details.**  
该方法主要强化边缘与细节。

---

## 10. **Pooling**

**Pooling downsamples an image by selecting a summary statistic over a local region.**  
池化通过对局部区域取统计值实现图像降采样。

**Common types include max, min, average, and median pooling.**  
常见方式包括最大池化、最小池化、平均池化和中值池化。

**Pooling reduces computation and removes small variations.**  
池化减少计算量并抑制小范围噪声变化。

**Widely used in CNNs.**  
广泛应用于卷积神经网络。

---

## 11. **Derivative Filters (for Edge Detection)**

**Spatial derivatives detect intensity changes—key for edge detection.**  
空间导数用于检测亮度变化，是边缘检测的核心。

**Approximated with finite differences: forward, backward, or central.**  
数字图像中通过前向差分、后向差分与中心差分近似。

**First derivatives detect edges; second derivatives detect zero crossings.**  
一阶导数检测边缘，二阶导数检测零交叉。

---

## 12. **Prewitt and Sobel Filters**

**Prewitt and Sobel compute derivatives with smoothing in the perpendicular direction.**  
Prewitt 与 Sobel 通过在垂直方向的平滑来计算导数。

**Sobel gives stronger smoothing, making it more stable to noise.**  
Sobel 有更强的平滑能力，对噪声更加稳定。

---

## 13. **Separable Filters**

**A 2D kernel is separable if it can be written as the product of two 1D kernels.**  
一个 2D 核可分离，当它能被写成两个一维核的乘积。

**Separable filters reduce computation from O(n²) to O(2n).**  
分离滤波能将计算从 O(n²) 降到 O(2n)。

**Gaussian, Sobel, and uniform filters are separable.**  
高斯、Sobel、均值核等都可以分离。

---

## 14. **Laplacian Filter**

**The Laplacian approximates the sum of second-order derivatives.**  
拉普拉斯算子近似计算二阶导数之和。

**It responds strongly to edges and zero-crossings.**  
它对边缘与零交叉反应明显。

**Kernel:  \[[0,1,0],[1,−4,1],[0,1,0]].**  
其典型核为 \[\[0,1,0],\[1,−4,1],\[0,1,0]]。

---

## 15. **Gradient Vector & Magnitude**

**The gradient vector points in the direction of strongest intensity increase.**  
梯度向量指向亮度上升最快的方向。

**Magnitude = sqrt(fx² + fy²).**  
梯度幅值 = sqrt(fx² + fy²)。

**Used for edge maps and edge strength.**  
用于生成边缘图和计算边缘强度。

---

## 16. **Edge Detection**

**Gradient magnitude detects edges via high-intensity changes.**  
梯度幅值通过检测亮度快速变化找到边缘。

**Laplacian detects edges via zero-crossings.**  
拉普拉斯通过零交叉点检测边缘。

**Correct scale (σ) is essential — too small detects noise, too large loses detail.**  
选择合适 σ（尺度）很重要——太小会检测到噪声，太大则会丢失细节。

---

## 17. **Differentiation in Fourier Domain**

**Differentiation becomes multiplication by (iω) in the frequency domain.**  
在频域中，求导对应乘以 (iω)。

**This boosts high frequencies, which also boosts noise.**  
求导会放大高频，从而也放大噪声。

---

## 18. **Sharpening Using Laplacian**

**A sharpened image can be computed as f − Laplacian(f).**  
锐化图像可以表示为 f − Laplacian(f)。

**This enhances edges by subtracting low-frequency content.**  
通过去除低频部分来强化边缘。

---

## 19. **Typical Exam Points**

**Know convolution definition and why kernels are flipped.**  
掌握卷积定义以及为什么需要翻转核。

**Mean vs Gaussian vs Median — effects and differences.**  
必须区分均值、高斯、中值滤波的效果与差异。

**Gradient vs Laplacian — first vs second derivative.**  
梯度与拉普拉斯：一阶导 vs 二阶导。

**Sobel vs Prewitt — smoothing strength differences.**  
Sobel 比 Prewitt 更平滑、更抗噪。

**Separable kernels reduce computation — know examples.**  
可分离核能降低运算量，需要记住哪些核可分离。

**Laplacian kernel approximates second-order derivatives.（考试原题）**  
拉普拉斯核近似二阶导数（考题中出现）。

---

> [!faq] Summary & Question
> 
> # ⭐ 1. **Neighborhood operations（邻域操作）**
> 
> **Neighborhood operations compute each output pixel using a small local region (kernel) around the input pixel.**  
> 邻域操作通过输入像素周围一个小局部区域（核）来计算输出像素。
> 
> **They involve convolution, kernel filtering, and LSI (linear shift-invariant) operations.**  
> 它们包含卷积、核滤波、线性平移不变系统等内容。
> 
> **The focus is on HOW the operation works mathematically and mechanically.**  
> 重点在于理解操作本身“如何工作”的数学原理与执行方式。
> 
> **Examples: convolution, padding methods, kernel flipping, border problem.**  
> 例子包括：卷积、边界处理、核翻转等技术细节。
> 
> 👉 **核心概念：它讲的是“原理与机制”。**  
> 👉 关注点是这些操作的**底层原理**、计算方法、性质。
> 
> 
> # ⭐ 2. **Filtering methods（滤波方法）**
> 
> **Filtering methods refer to specific types of filters and how they affect the image.**  
> 滤波方法指具体的滤波器类型及其对图像的影响。
> 
> **They explain the purpose and effect of different filters: smoothing, noise removal, sharpening, etc.**  
> 它们解释不同滤波器的目的与效果，如平滑、降噪、锐化等。
> 
> **Different filters behave differently depending on their kernels and designs.**  
> 不同滤波器因其核设计不同而具有不同的行为方式。
> 
> **Examples: uniform filter, Gaussian filter, median filter, differentiation, separable filters, pooling.**  
> 例子包括：均值滤波、高斯滤波、中值滤波、微分滤波、可分离核、池化等。
> 
> 👉 **核心概念：它讲的是“每种滤波器做什么 + 效果是什么”。**  
> 👉 关注点是不同滤波器的**用途、优缺点、影响**。
> 
> ---
> 
> # ⭐ 3. **Image enhancement（图像增强）**
> 
> **Image enhancement combines multiple filters/operations to improve the visual quality or highlight structures.**  
> 图像增强通过组合多个滤波/操作来提升图像视觉质量或突出结构。
> 
> **It uses filtering operations as building blocks to create stronger enhancement techniques.**  
> 它将滤波作为基础模块，用来实现更高级的增强技术。
> 
> **Typical enhancements include sharpening, unsharp masking, edge detection, gradient magnitude, etc.**  
> 常见增强方法有：锐化、反锐化、边缘检测、梯度幅值计算等。
> 
> 👉 **核心概念：它讲的是“应用与组合策略”。**  
> 👉 关注点是如何**用滤波器实现更高层的图像增强任务**。
> 
> ---
> 
> # 🔥 三者核心区别总结（最重要）
> 
> |Category|What it focuses on|中文解释|
> |---|---|---|
> |**Neighborhood operations**|How filtering works (mechanics & math)|关注原理和计算方式|
> |**Filtering methods**|The types of filters and their effects|关注滤波器种类与作用|
> |**Image enhancement**|Using filters to improve image quality|关注最终增强任务（应用）|
> 
> ---
> 
> # 🔥 三者的关系（一句话总结）
> 
> **Neighborhood operations are the fundamental mechanism → filtering methods are specific tools built on that mechanism → image enhancement uses those tools to achieve practical improvements.**  
> 邻域操作是底层机制 → 滤波方法是在该机制之上构建的具体工具 → 图像增强利用这些工具来实现实际的增强任务。

## ✅ **1. Laplacian kernel（拉普拉斯算子）— 必考**

**Kernel:  
$\begin{bmatrix}0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0\end{bmatrix}$  
Approximates the sum of second-order derivatives → detects zero-crossings (edges).**  
近似二阶导数之和，用于检测零交叉与边缘，是 PPT “例题”考题。

---

## ✅ **2. Sobel kernels — 必会的一阶导数滤波器**

### **Sobel X**

**Kernel:  
$\begin{bmatrix}1 & 0 & -1 \\ 2 & 0 & -2 \\ 1 & 0 & -1\end{bmatrix}$  
Computes ∂f/∂x with smoothing → detects vertical edges.**  
计算 x 方向一阶导（带平滑），用于检测垂直边缘。

### **Sobel Y**

**Kernel:  
$\begin{bmatrix}1 & 2 & 1 \\ 0 & 0 & 0 \\ -1 & -2 & -1\end{bmatrix}$  
Computes ∂f/∂y with smoothing → detects horizontal edges.**  
计算 y 方向一阶导，检测水平边缘。

---

## ✅ **3. Prewitt kernels — 考点：与 Sobel 对比**

### **Prewitt X**

**Kernel:  
$\begin{bmatrix}1 & 0 & -1 \\ 1 & 0 & -1 \\ 1 & 0 & -1\end{bmatrix}$  
First-order derivative in x with weaker smoothing than Sobel.**  
x方向一阶导，平滑较弱（考试爱问差异）。

### **Prewitt Y**

**Kernel:  
$\begin{bmatrix}1 & 1 & 1 \\ 0 & 0 & 0 \\ -1 & -1 & -1\end{bmatrix}$  
First-order derivative in y.**  
y方向一阶导。

---

## ✅ **4. Uniform averaging filter（均值滤波）— 必会**

### **3×3 Uniform**

**Kernel:  
$\frac{1}{9}\begin{bmatrix}1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1\end{bmatrix}$
Performs simple smoothing; reduces noise but blurs edges.**  
简单平滑，降噪但模糊边缘。

---

## ✅ **5. Gaussian filter kernels — 高频考点（可分离）**

### **Example 3×3 Gaussian kernel**

**Kernel (σ≈1):  
$\frac{1}{16}\begin{bmatrix}1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1\end{bmatrix}$
Performs smooth, natural blurring; separable; best for noise reduction.**  
自然平滑、最好的降噪滤波器，并且核可分离（重要考点）。

---

## ✅ **6. Gaussian derivative filters — PPT 明确强调**

### **First derivative of Gaussian (DoG)**

**Kernel example:  
X-derivative: $\begin{bmatrix}1 & 0 & -1 \\ 2 & 0 & -2 \\ 1 & 0 & -1\end{bmatrix}$  
Equivalent to smoothed derivative — used for edge detection.**  
平滑的一阶导数，最常用于边缘检测（比 Sobel 更理论标准）。

PPT 强调：  
**Gaussian derivative = 边缘检测的基础（scale-space theory）**

---

## ✅ **7. Second derivative of Gaussian（LoG）— 也在PPT提到**

**This is the basis of Laplacian of Gaussian.**  
这是高斯拉普拉斯算子的基础。

**Used for detecting edges via zero-crossings.**  
用于通过零交叉检测边缘。

---

## ✅ **8. Min / Max filters（非线性滤波器）**

**Kernel structure: neighborhood window; output = min or max of all pixels.**  
结构就是邻域窗口，但输出是最大或最小值。

**Used for morphology-like effects.**  
用于形态学效果。

![[Pasted image 20251116132108.png]]
B

# Part 2
## ⭐ 1. Spatial vs Frequency Domain

**Spatial domain processes pixels directly in the image plane.**  
空间域直接处理图像平面上的像素。

**Frequency domain processes the Fourier transform of the image.**  
频域在图像的傅里叶变换上进行处理。

---

## ⭐ 2. Fourier Transform Basics

**Fourier transform represents an image as a weighted sum of sinusoids of different frequencies.**  
傅里叶变换将图像表示为不同频率正弦波的加权和。

**Low frequencies encode smooth/large structures; high frequencies encode sharp edges and detail.**  
低频表示平滑、大结构；高频表示锐利边缘和细节。

**Forward transform → goes to frequency domain; inverse transform → returns to spatial domain.**  
正变换将图像变到频域，逆变换将图像拉回空间域。

---

## ⭐ 3. 1D Fourier Transform (Definition)

**Forward FT: $(F(u)=\int f(x)e^{-i2\pi ux}dx)$**  
前向傅里叶公式：将信号分解为频率分量。

**Inverse FT reconstructs the signal from all its frequencies.**  
逆变换用所有频率分量重建原信号。

---

## ⭐ 4. 2D Fourier Transform (for images)

**2D FT transforms an image (f(x,y)) into frequency domain (F(u,v)).**  
二维傅里叶将图像 (f(x,y)) 转换为频域 (F(u,v))。

**Magnitude = structure; Phase = geometry.**  
幅度决定结构， 相位决定图像的几何信息。

---

## ⭐ 5. Properties of Fourier Transform (Exam-Focused)

**Convolution in spatial domain = multiplication in frequency domain.**  
空间域卷积等同于频域中的乘法（卷积定理）。

**Correlation in spatial domain = multiplication with complex conjugate in frequency domain.**  
空间域相关对应频域中乘共轭。

**Translation in space introduces phase shift in frequency.**  
空间平移 → 频域相位移动。

**Differentiation multiplies by $((i2\pi u)^n)$.**  
微分操作在频域中相当于乘以 $((i2\pi u)^n)$。

---

## ⭐ 6. Discrete Fourier Transform (DFT)

**Images are discrete → use DFT instead of continuous FT.**  
图像是离散的 → 使用 DFT。

**DFT always exists and maps an M×N image to an M×N frequency representation.**  
DFT 始终存在，将 M×N 图像映射到 M×N 频域图。

---

## ⭐ 7. Frequency Domain Filtering Overview

**Filtering = multiply the Fourier transform (F(u,v)) by a filter (H(u,v)).**  
频域滤波 = 将傅里叶结果 (F(u,v)) 与滤波器 (H(u,v)) 相乘。

**High frequencies = edges & noise; low frequencies = smooth regions.**  
高频 = 边缘与噪声；低频 = 平滑区域。

---

## ⭐ 8. Centering the Fourier Transform

**To visualize/process FT, the low-frequency component is shifted to the center.**  
为了显示与处理，低频分量通常被移到中心。

**This is done by multiplying the spatial image by $((-1)^{x+y})$.**  
通过在空间域乘上 $((-1)^{x+y})$ 完成居中操作。

---

## ⭐ 9. Frequency-Domain Filtering Procedure (Important!)

1. **Multiply image by $((-1)^{x+y})$** → center the spectrum.  
    乘 ((-1)^{x+y}) → 频谱居中。
    
2. **Compute 2D DFT.**  
    计算二维 DFT。
    
3. **Multiply by frequency filter (H(u,v)).**  
    与频域滤波器相乘。
    
4. **Inverse DFT.**  
    做逆 DFT。
    
5. **Take the real part.**  
    取实部。
    
6. **Multiply again by $((-1)^{x+y})$** → undo centering.  
    再次乘 $((-1)^{x+y})$ 恢复图像位置。
    

---

## ⭐ 10. Low-Pass Filtering (Blur)

**Low-pass filter keeps low frequencies and suppresses high frequencies.**  
低通滤波保留低频，抑制高频。

**Result = blurred image.**  
结果 = 模糊图像。

---

## ⭐ 11. High-Pass Filtering (Edge Emphasis)

**High-pass filter keeps high frequencies and removes low frequencies.**  
高通滤波保留高频，去除低频。

**Result = sharp edges but noisy.**  
结果 = 强边缘，但噪声更强。

---

## ⭐ 12. Notch Filtering (Remove Patterns)

**Notch filters remove specific frequency spikes caused by periodic noise (e.g., scanline artifacts).**  
陷波滤波器移除特定频率的周期性噪声（如扫描线条纹）。

**Used to clean structured noise in satellite or machine-vision images.**  
用于去除卫星或工业图像中的固定模式噪声。

---

## ⭐ 13. Gaussian in Frequency Domain

**Fourier transform of Gaussian is also Gaussian.**  
高斯在频域中仍然是高斯。

**Thus Gaussian low-pass filters are smooth and non-ringing.**  
因此高斯低通滤波平滑且无振铃现象。

---

## ⭐ 14. Difference of Gaussians (DoG)

**DoG = Gaussian(σ1) − Gaussian(σ2), approximates Laplacian-of-Gaussian (LoG).**  
DoG = 两个不同 σ 的高斯之差，近似 LoG。

**DoG acts as a high-pass edge detector.**  
DoG 是高通滤波器，用于边缘检测。

**Used heavily in SIFT, blob detection, scale-space analysis.**  
在 SIFT、斑点检测、尺度空间中大量使用。

---

## ⭐ 15. Multiresolution Image Processing

**Some structures exist at coarse scale, others at fine scale → need multiple resolutions.**  
有些结构在粗尺度明显，有些在细尺度明显 → 需要多层尺度。

**Solution: image pyramids (Gaussian & Laplacian pyramids).**  
解决：图像金字塔（高斯与拉普拉斯金字塔）。

---

## ⭐ 16. Creating Image Pyramids

1. **Low-pass filtering + downsampling** → approximation image.  
    低通滤波并下采样 → 得到近似图。
    
2. **Upsample + filter** → predicted reconstruction.  
    上采样与滤波 → 预测重建图。
    
3. **Input − prediction** → residual.  
    输入 − 预测值 → 得到残差。
    

**Repeat to build multiple pyramid levels.**  
重复上述步骤得到多层金字塔。

---

## ⭐ 17. Pyramid Use Cases

**Compression, blending, multi-resolution processing, edge-aware filtering.**  
用于压缩、图像融合、多尺度处理、边缘保持滤波等。

---

## ⭐ 18. Exam Question (from PPT)

**Incorrect answer: C — High-pass filtering smooths fine details.**  
C 是错误的 → 高通不会平滑细节，而是强化细节。
![[Pasted image 20251117180737.png]]

> [!faq] Summary & Question
> ## ⭐ What is the Fourier Transform?
> 
> **The Fourier transform represents an image as a weighted sum of sinusoids at different frequencies.**  
> 傅里叶变换将图像表示为不同频率正弦波的加权组合。
> 
> **It converts $f(x,y)$ in spatial domain into $F(u,v)$ in frequency domain.**  
> 它把空间域的 $f(x,y)$ 转换成频域的 $F(u,v)$。
> 
> **Low frequencies capture smooth structure; high frequencies capture edges and details.**  
> 低频表示平滑结构，高频表示边缘和细节。
> 
> ---
> 
> ## ⭐ What does the Fourier Transform do?
> 
> **It reveals the image’s frequency components and their strengths.**  
> 它揭示图像里每种频率成分及其强度。
> 
> **It allows filtering by frequency instead of by position.**  
> 它让我们可以按“频率”而不是按“像素位置”进行滤波。
> 
> **Examples:**
> 
> - Removing high frequencies → blur
>     
> - Removing low frequencies → edge enhancement
>     
> - Removing specific frequencies → notch filtering
>     
> - Analyzing texture patterns
>     
> 
> ---
> 
> ## ⭐ Difference vs Point Operations
> 
> **Point operations transform pixels independently: $g(x,y)=T(f(x,y))$.**  
> 点操作独立处理每个像素：$g(x,y)=T(f(x,y))$。
> 
> **They do not use neighborhood or global structure.**  
> 它们不利用邻居像素，也不利用全局结构。
> 
> **Examples:** brightness change, contrast stretching, gamma, thresholding.  
> 例如亮度、对比度、阈值等操作。
> 
> 👉 **Point ops = single-pixel, local intensity changes.**  
> 👉 点操作 = 单点的局部强度变化。
> 
> ---
> 
> ## ⭐ Difference vs Neighbourhood Operations
> 
> **Neighbourhood operations use a local window (3×3, 5×5) around each pixel.**  
> 邻域操作使用像素周围的局部窗口（3×3 或 5×5）。
> 
> **They approximate derivatives, smoothing, sharpening using convolution kernels.**  
> 它们通过卷积核实现平滑、锐化、一阶/二阶导数等效果。
> 
> **Examples:** Gaussian blur, Sobel, Laplacian, median, unsharp masking.  
> 包括高斯模糊、Sobel、Laplacian、中值滤波、反锐化等。
> 
> 👉 **Neighbourhood ops = local spatial patterns.**  
> 👉 邻域操作 = 局部空间模式。
> 
> ---
> 
> ## ⭐ What is unique about Fourier Transform?
> 
> **Fourier transform is global: each $F(u,v)$ uses all pixels of $f(x,y)$.**  
> 傅里叶是全局操作：每一个 $F(u,v)$ 都由整幅图像决定。
> 
> **It sees periodic patterns and global frequency structures that local filters cannot detect.**  
> 它能看到局部滤波器看不到的周期性结构和全局频率分布。
> 
> 👉 **Fourier = global frequency information.**  
> 👉 傅里叶 = 全局频域信息。
> 
> ---
> 
> ## ⭐ What problem does Fourier Transform solve?
> 
> ### 🔹 1. Local filters cannot remove periodic noise
> 
> 本地滤波无法去除周期性噪声，如扫描线纹理。  
> 频域中这些噪声变成“尖点”，用 notch filter 轻松滤掉。
> 
> ### 🔹 2. Local filters cannot target specific frequencies
> 
> 本地滤波不能精准控制“滤掉哪个频率”。  
> 频域可以轻松设计 low-pass / high-pass / band-pass。
> 
> ### 🔹 3. Designing complex spatial filters is hard
> 
> 设计一个 30×30 的空间卷积核很困难，但在频域只需画一个掩膜 $H(u,v)$。
> 
> ### 🔹 4. Enables multi-resolution processing
> 
> 让 DoG、LoG、金字塔、尺度空间成为可能。
> 
> ---
> 
> ## ⭐ Final Summary (Short & Exam-oriented)
> 
> **Fourier transform converts an image into frequency domain, enabling global, frequency-selective filtering that point and neighborhood operations cannot achieve.**  
> 傅里叶将图像转换到频域，使我们能做点操作和邻域操作无法实现的全局、按频率选择性的滤波。
> 
