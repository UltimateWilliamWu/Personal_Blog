---
tags:
  - LectureNotes
---
# Part 1

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

> [!NOTE] Note
> ## **Neighborhood operations**
> 
> Local window → convolution → border handling.  
> 局部窗口 → 卷积滤波 → 边界处理。
> 
> ## **Filtering methods**
> 
> Mean = simple blur  
> Gaussian = best blur  
> Median = salt-pepper removal  
> Sobel/Prewitt = gradient  
> Laplacian = second derivative  
> Separability = fast  
> Pooling = downsample
> 
> ## **Image enhancement**
> 
> Sharpen = boost high-frequency  
> USM = original − blur  
> Gradient magnitude = edge strength  
> Edge detection = find high gradients

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

## 1. Fourier transform for image processing

> [!NOTE] Note
> 
> ## ⭐ What is the Fourier transform?
> 
> **The Fourier transform converts an image from the spatial domain $f(x,y)$ into the frequency domain $F(u,v)$.**  
> 傅里叶变换把图像从空间域 $f(x,y)$ 转换到频域 $F(u,v)$。
> 
> **It represents the image as a sum of sinusoids of different frequencies and orientations.**  
> 它把图像表示成不同频率和方向的正弦波的加权组合。
> 
> ---
> 
> ## ⭐ Why do we need the Fourier transform?
> 
> **Because many image properties are easier to analyze in frequency domain than in spatial domain.**  
> 因为许多图像特性在频域中比在空间域更容易被分析。
> 
> **Edges, noise, blur, and periodic patterns have clear signatures in frequency space.**  
> 边缘、噪声、模糊、周期结构在频域中都有清晰的表现形式。
> 
> ---
> 
> ## ⭐ Forward Fourier Transform (2D FWT)
> 
> **It converts $f(x,y)$ into $F(u,v)$:**  
> 它将空间图像转换为频谱：
> 
> $$  
> F(u,v)=\sum_{x=0}^{M-1}\sum_{y=0}^{N-1} f(x,y)e^{-i2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}  
> $$
> 
> **Each frequency pair $(u,v)$ shows how strong a sinusoid of that frequency is in the image.**  
> 每个频率 $(u,v)$ 表示图像中该频率正弦波的强度。
> 
> ---
> 
> ## ⭐ Inverse Fourier Transform
> 
> **It reconstructs the original image from all frequency components.**  
> 逆变换负责用所有频率成分重建原始图像。
> 
> $$  
> f(x,y)=\frac{1}{MN}\sum_{u=0}^{M-1}\sum_{v=0}^{N-1}F(u,v)e^{i2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}  
> $$
> 
> ---
> 
> ## ⭐ Convolution Theorem（非常重要）
> 
> **Convolution in spatial domain equals multiplication in frequency domain.**  
> 空间域的卷积等价于频域中的乘法。
> 
> $$  
> f * h \quad \Longleftrightarrow \quad F(u,v)H(u,v)  
> $$
> 
> **This is why filtering is easier in frequency domain.**  
> 这就是为什么频域滤波更实际、更容易。
> 
> ---
> 
> ## ⭐ Properties of Fourier Transform（考试重点）
> 
> ### ✔ Linearity
> 
> **$a f_1 + b f_2$ transforms to $aF_1 + bF_2$.**  
> 线性组合在变换后依然保持线性。
> 
> ---
> 
> ### ✔ Shift property
> 
> **Shifting the image causes a phase shift in $F(u,v)$, but magnitude stays the same.**  
> 图像平移会改变频域相位，但不会影响幅度。
> 
> ---
> 
> ### ✔ Differentiation property
> 
> **Taking spatial derivatives multiplies by frequency:**  
> 空间求导相当于乘以频率：
> 
> $$  
> \frac{\partial f}{\partial x} \Longleftrightarrow (i2\pi u)F(u,v)  
> $$
> 
> **This explains why edges appear strong in high frequencies.**  
> 这解释了为什么边缘在高频区域非常强烈。
> 
> ---
> 
> ## ⭐ Discrete Fourier Transform (DFT)
> 
> **Images are discrete → must use DFT instead of continuous FT.**  
> 图像是离散的 → 必须使用 DFT。
> 
> **DFT always exists and gives an $M\times N$ transform of an $M\times N$ image.**  
> DFT 对任意 $M \times N$ 图像都定义良好，并且结果也是同样大小。
> 
> ---
> 
> ## ⭐ Relationship between spatial patterns and frequencies
> 
> ### ✔ Smooth regions = low frequencies
> 
> 平滑区域对应低频。
> 
> ### ✔ Fine details and edges = high frequencies
> 
> 细节与边缘对应高频。
> 
> ### ✔ Periodic patterns = sharp spikes
> 
> 周期结构对应尖锐的频率“亮点”。
> 
> ---
> 
> ## ⭐ Why use Fourier transform in image processing?
> 
> **1. To perform precise frequency filtering (low-pass, high-pass, band-pass).**  
> 用于精准滤波（低通、高通、带通）。
> 
> **2. To remove periodic noise using notch filtering.**  
> 用陷波滤波去除周期噪声。
> 
> **3. To analyze textures and repeating patterns.**  
> 分析纹理与重复结构。
> 
> **4. To enable multi-scale (multiresolution) analysis.**  
> 支持多尺度分析（如 DoG、金字塔）。
> 
> **5. To perform operations impractical in spatial domain (e.g., large filters).**  
> 执行空间域难以实现的大范围滤波。
> 
> ---
> 
> ## ⭐ Final 1-sentence summary
> 
> **Fourier transform enables a frequency-based view of images, allowing global analysis and precise filtering that spatial operations cannot achieve.**  
> 傅里叶变换让我们从频率角度理解图像，实现空间域无法完成的全局分析与精准滤波。
> 

## 2. Fourier domain filtering methods

> [!NOTE] Note
> 
> ## ⭐ What is Fourier domain filtering?
> 
> **Fourier domain filtering modifies an image by multiplying its Fourier transform $F(u,v)$ with a frequency filter $H(u,v)$.**  
> 频域滤波通过将图像的傅里叶变换 $F(u,v)$ 与频域滤波器 $H(u,v)$ 相乘来修改图像。
> 
> **Filtering happens frequency-by-frequency instead of pixel-by-pixel.**  
> 滤波在频率维度逐频率进行，而不是像素维度。
> 
> ---
> 
> ## ⭐ Why filter in the frequency domain?
> 
> **Frequency domain filtering allows precise control over which frequencies are kept or suppressed.**  
> 频域滤波可以精确控制保留或去除哪些频率。
> 
> **It is ideal for removing periodic noise, smoothing, sharpening, and multi-scale analysis.**  
> 非常适合去除周期噪声、平滑、锐化与多尺度分析。
> 
> ---
> 
> ## ⭐ The Fourier Filtering Procedure（PPT 强调步骤，必考）
> 
> **Step 1: Multiply input image $f(x,y)$ by $(-1)^{x+y}$ to center low frequencies.**  
> 步骤1：给输入乘以 $(-1)^{x+y}$，将低频移到中心。
> 
> **Step 2: Compute the 2D DFT → $F(u,v)$.**  
> 步骤2：计算二维 DFT，得到 $F(u,v)$。
> 
> **Step 3: Multiply with the filter mask → $G(u,v)=F(u,v)H(u,v)$.**  
> 步骤3：与频域滤波器相乘，得到 $G(u,v)=F(u,v)H(u,v)$。
> 
> **Step 4: Compute inverse DFT to go back to spatial domain.**  
> 步骤4：对 $G(u,v)$ 做逆 DFT 回到空间域。
> 
> **Step 5: Take the real part (imaginary part should be negligible).**  
> 步骤5：取实部（虚部通常是数值误差）。
> 
> **Step 6: Multiply again by $(-1)^{x+y}$ to undo the centering.**  
> 步骤6：再次乘 $(-1)^{x+y}$ 恢复图像。
> 
> ---
> 
> ## ⭐ Low-Pass Filtering（低通滤波）
> 
> **Low-pass filters keep low frequencies and suppress high frequencies.**  
> 低通滤波器保留低频，抑制高频。
> 
> **Result: smooth, blurred image with removed noise and fewer edges.**  
> 结果：图像更平滑、更模糊，高频噪声和边缘被移除。
> 
> **Common shapes: Gaussian LPF, ideal LPF, Butterworth LPF.**  
> 常见形状有：高斯低通、理想低通、巴特沃斯低通。
> 
> ---
> 
> ## ⭐ High-Pass Filtering（高通滤波）
> 
> **High-pass filters keep high frequencies and suppress low frequencies.**  
> 高通滤波器保留高频，抑制低频。
> 
> **Result: edge enhancement or edge extraction.**  
> 结果：增强边缘或提取边缘。
> 
> **Used for sharpening and detecting fine details.**  
> 用于锐化和检测细节。
> 
> ---
> 
> ## ⭐ Band-Pass / Band-Stop Filtering（带通 / 带阻滤波）
> 
> **Band-pass filters keep a specific frequency band and remove others.**  
> 带通滤波保留特定频段。
> 
> **Band-stop (notch) filters suppress specific frequency bands only.**  
> 带阻（陷波）滤波只抑制特定频段。
> 
> 👉 两者都是频域才能轻松实现的。
> 
> ---
> 
> ## ⭐ Notch Filtering（陷波滤波）
> 
> **Notch filters remove specific frequency spikes caused by periodic noise.**  
> 陷波滤波用于移除周期性噪声引起的尖点频率。
> 
> **Periodic stripes or repeating patterns in spatial domain become isolated bright points in frequency domain.**  
> 空间中的周期条纹噪声在频域中变成单独的亮点。
> 
> **By zeroing out those points, the unwanted stripes disappear.**  
> 把这些尖点设为 0，条纹噪声就消失了。
> 
> 👉 **Only frequency domain can do this cleanly.**  
> 👉 **这类去噪只有频域能做得干净！**
> 
> ---
> 
> ## ⭐ Why use Gaussian filters in frequency domain?
> 
> **The Fourier transform of a Gaussian is also a Gaussian, so filtering is smooth and ring-free.**  
> 高斯的傅里叶变换仍是高斯 → 滤波平滑且无振铃（无假边缘）。
> 
> **Gaussian LPF and HPF produce the most natural results.**  
> 高斯低通与高通通常效果最好。
> 
> ---
> 
> ## ⭐ How spatial filters relate to frequency filters
> 
> **Convolution in spatial domain = multiplication in frequency domain.**  
> 空间域卷积等价于频域中的乘法。
> 
> **This is the convolution theorem (important!).**  
> 这就是卷积定理（考试重点）。
> 
> **Large spatial filters ↔ small simple frequency masks.**  
> 空间域的大卷积核对应频域中的小而简单的频率掩膜。
> 
> ---
> 
> ## ⭐ Visual intuition (must understand)
> 
> **Low frequencies = slow changes → smooth regions.**  
> 低频 = 变化慢 → 图像平滑部分。
> 
> **High frequencies = fast changes → edges and noise.**  
> 高频 = 变化快 → 边缘和噪声。
> 
> 👉 所以：
> 
> - 去噪 = 去高频
>     
> - 模糊 = 去高频
>     
> - 锐化 = 增强高频
>     
> - 去条纹 = 去掉特定频率的尖点
>     
> 
> ---
> 
> ## ⭐ Final summary (exam-short version)
> 
> **Fourier domain filtering = multiply $F(u,v)$ by $H(u,v)$**  
> 频域滤波 = 让 $F(u,v)$ 和 $H(u,v)$ 相乘
> 
> **Low-pass → blur**  
> 低通 → 模糊
> 
> **High-pass → edges/sharpen**  
> 高通 → 边缘/锐化
> 
> **Notch → remove periodic noise**  
> 陷波 → 去周期噪声
> 
> **Gaussian filters → smoothest, no ringing**  
> 高斯滤波 → 最平滑、无伪影
> 
> **Procedure = center → DFT → multiply → IDFT → uncenter**  
> 流程 = 居中 → DFT → 相乘 → IDFT → 取消居中

## 3. Multiresolution image processing

> [!NOTE] Note
> ## ⭐ What is multiresolution image processing?
> 
> **Multiresolution image processing represents an image at multiple scales or resolutions simultaneously.**  
> 多分辨率图像处理是在多个尺度或分辨率下同时表示一幅图像。
> 
> **It allows us to analyze coarse (large-scale) structures and fine (detail) structures separately.**  
> 它让我们可以分别分析图像的粗结构（大范围）和细节（小范围）。
> 
> ---
> 
> ## ⭐ Why do we need multiple resolutions?
> 
> **Some information is visible only at coarse scale, others only at fine scale.**  
> 图像中有些结构在“粗尺度”才明显，有些在“细尺度”才明显。
> 
> **Human vision naturally processes images at multiple scales.**  
> 人类视觉系统也天然按多尺度理解图像。
> 
> **Many tasks—blending, compression, edge-preserving filtering—require separating scales.**  
> 诸如融合、压缩、边缘保持滤波等任务都需要按尺度分解图像。
> 
> ---
> 
> ## ⭐ How do we achieve multiresolution processing?
> 
> **We create multiple smoothed and downsampled versions of the image, forming a pyramid.**  
> 我们通过多次平滑和下采样来创建图像的多尺度版本，形成图像金字塔。
> 
> ---
> 
> ## ⭐ Gaussian Pyramid（高斯金字塔）
> 
> **A Gaussian pyramid is created by repeatedly low-pass filtering and downsampling the image.**  
> 高斯金字塔通过不断地低通滤波和下采样构建。
> 
> **Each level removes more high-frequency detail to provide a coarser version of the image.**  
> 每一层都会移除更多的高频细节，让图像更加粗糙。
> 
> ---
> 
> ## ⭐ Laplacian Pyramid（拉普拉斯金字塔）
> 
> **A Laplacian pyramid stores the difference between Gaussian levels, capturing band-pass details.**  
> 拉普拉斯金字塔存储高斯层之间的差值，从而捕获中频/细节信息。
> 
> **Each level represents details that were lost during smoothing.**  
> 每一层表示在平滑过程中“丢失的细节”。
> 
> ---
> 
> ## ⭐ Why build pyramids?
> 
> **Pyramids separate an image into smooth components and detail components.**  
> 金字塔将图像分解为平滑部分与细节部分。
> 
> **This enables operations like image blending, texture analysis, and efficient compression.**  
> 这样就能实现图像融合、纹理分析、高效压缩等功能。
> 
> ---
> 
> ## ⭐ Pyramid construction steps (Gaussian)
> 
> **1. Apply low-pass filter (usually Gaussian).**
> 
> 1. 对图像做低通滤波（通常是高斯滤波）。
>     
> 
> **2. Downsample by factor 2 (take every second pixel).**  
> 2. 下采样（每隔一个像素取一个）。
> 
> **3. Repeat to create multiple levels.**  
> 3. 重复执行多次，得到多层金字塔。
> 
> ---
> 
> ## ⭐ Pyramid reconstruction (Laplacian)
> 
> **1. Upsample the coarse image (insert zeros).**
> 
> 4. 上采样（插入零）。
>     
> 
> **2. Low-pass filter to smooth interpolation.**  
> 5. 用低通滤波器平滑插值。
> 
> **3. Add the stored detail layer back.**  
> 6. 将之前保存的细节层加回去。
> 
> **Repeat until original size is restored.**  
> 重复该步骤直到重建原始图像。
> 
> ---
> 
> ## ⭐ Difference of Gaussians (DoG) and multiresolution
> 
> **DoG = Gaussian($\sigma_2$) − Gaussian($\sigma_1$) approximates a band-pass filter.**  
> DoG = $G(\sigma_2) - G(\sigma_1)$，近似一个带通滤波器。
> 
> **This acts like one level of the Laplacian pyramid.**  
> 它的效果就像拉普拉斯金字塔的一层。
> 
> ---
> 
> ## ⭐ Why multiresolution is powerful
> 
> **Different tasks need different scales: edges, textures, illumination, shapes.**  
> 不同任务需要不同尺度：边缘、纹理、光照、形状等。
> 
> **Multiresolution processing allows each scale to be handled properly.**  
> 多分辨率处理能让每个尺度的信息都得到恰当处理。
> 
> **This produces cleaner, more natural results than single-scale methods.**  
> 比单尺度方法得到更自然、更干净的结果。
> 
> ---
> 
> ## ⭐ Final Summary
> 
> **Multiresolution processing decomposes an image into multiple spatial scales using Gaussian and Laplacian pyramids.**  
> 多分辨率处理通过高斯和拉普拉斯金字塔把图像分解为多个空间尺度。
> 
> **It enables operations like blending, compression, and scale-space analysis that single-scale filtering cannot achieve.**  
> 它能实现单尺度滤波无法做到的图像融合、压缩、尺度空间分析等操作。
