# 1. **Neighbourhood Operations**

**Neighbourhood operations compute each output pixel using a small local region around the input pixel.**  
邻域操作通过输入像素周围的一个小区域来计算输出像素。

**This region is typically a 3×3, 5×5, or 7×7 square subimage.**  
该区域一般是 3×3、5×5 或 7×7 的邻域。

**The weights of this region form the kernel (or filter).**  
邻域中每个像素对应的权重组成“核（滤波器）”。

**Neighbourhood operations can smooth, sharpen, enhance, or detect features in an image.**  
邻域操作可以实现平滑、锐化、增强或特征检测等功能。

---

# 2. **Spatial Filtering by Convolution**

**Convolution computes the output o(x,y) = ΣΣ f(x−i, y−j) h(i, j).**  
卷积通过公式 o(x,y) = ΣΣ f(x−i, y−j) h(i,j) 来计算输出。

**The kernel is flipped before sliding over the image (definition of convolution).**  
根据卷积定义，核在滑动前需要“翻转”。

**Convolution is linear and shift-invariant.**  
卷积是线性且平移不变的操作。

**Because it is LSI, convolution behaves consistently across the entire image.**  
由于其 LSI 特性，卷积在整个图像范围内行为一致。

---

# 3. **The Border Problem and Fixes**

**Filtering near borders requires defining pixel values outside the image.**  
在边界进行滤波时需要定义图像外的像素如何处理。

**Common solutions include padding, clamping, wrapping, and mirroring.**  
常见方案包括零填充、边缘复制、循环复制和镜像扩展。

**Mirroring produces smooth boundaries and avoids artifacts.**  
镜像扩展可以避免伪影，是最佳边界处理方式之一。

---

# 4. **Properties of Convolution**

**Convolution satisfies commutativity, associativity, and distributivity.**  
卷积满足交换律、结合律和分配律。

**Convolution in spatial domain equals multiplication in frequency domain.**  
空间域卷积等价于频域中的乘法（下一周详细讲）。

---

# 5. **Uniform Smoothing (Mean Filter)**

**The mean filter replaces each pixel with the average of its neighborhood.**  
均值滤波将每个像素替换为邻域的平均值。

**It reduces noise but also blurs edges.**  
它可降噪但会导致边缘模糊。

**Uniform smoothing corresponds to a kernel filled with equal weights.**  
均值滤波对应的核是全 1 的均匀权重矩阵。

---

# 6. **Gaussian Filter**

**The Gaussian filter applies a weighted average with weights following a Gaussian distribution.**  
高斯滤波使用符合高斯分布的权重进行加权平均。

**It is separable and circularly symmetric, making it efficient and stable.**  
高斯滤波可分离且具有圆对称性，因此高效且稳定。

**It smooths images while preserving structure better than the mean filter.**  
它比均值滤波更能保留结构信息。

**Sigma (σ) controls the scale—the larger σ is, the stronger the blur.**  
σ 控制模糊强度，σ 越大模糊越明显。

---

# 7. **Median Filter**

**The median filter selects the median value within the neighborhood.**  
中值滤波选择邻域像素的中位数作为输出。

**It removes salt-and-pepper noise without smoothing edges.**  
它能移除椒盐噪声，同时保持边缘清晰。

**It is nonlinear (not a convolution operation).**  
它是非线性的，因此不是卷积。

---

# 8. **Gaussian vs Median Filtering**

**Gaussian filtering preserves small structures but blurs noise gradually.**  
高斯滤波能保留小结构，但对噪声的处理较柔和。

**Median filtering completely removes impulse noise but may erase small objects.**  
中值滤波对脉冲噪声非常有效，但可能删除小目标。

---

# 9. **Sharpening by Unsharp Masking**

**Unsharp masking enhances high-frequency components by adding back (Input − Blurred).**  
反锐化（Unsharp Masking）通过增强高频成分 (原图 − 平滑图) 来提高锐度。

**This boosts edges and fine details.**  
该方法主要强化边缘与细节。

---

# 10. **Pooling**

**Pooling downsamples an image by selecting a summary statistic over a local region.**  
池化通过对局部区域取统计值实现图像降采样。

**Common types include max, min, average, and median pooling.**  
常见方式包括最大池化、最小池化、平均池化和中值池化。

**Pooling reduces computation and removes small variations.**  
池化减少计算量并抑制小范围噪声变化。

**Widely used in CNNs.**  
广泛应用于卷积神经网络。

---

# 11. **Derivative Filters (for Edge Detection)**

**Spatial derivatives detect intensity changes—key for edge detection.**  
空间导数用于检测亮度变化，是边缘检测的核心。

**Approximated with finite differences: forward, backward, or central.**  
数字图像中通过前向差分、后向差分与中心差分近似。

**First derivatives detect edges; second derivatives detect zero crossings.**  
一阶导数检测边缘，二阶导数检测零交叉。

---

# 12. **Prewitt and Sobel Filters**

**Prewitt and Sobel compute derivatives with smoothing in the perpendicular direction.**  
Prewitt 与 Sobel 通过在垂直方向的平滑来计算导数。

**Sobel gives stronger smoothing, making it more stable to noise.**  
Sobel 有更强的平滑能力，对噪声更加稳定。

---

# 13. **Separable Filters**

**A 2D kernel is separable if it can be written as the product of two 1D kernels.**  
一个 2D 核可分离，当它能被写成两个一维核的乘积。

**Separable filters reduce computation from O(n²) to O(2n).**  
分离滤波能将计算从 O(n²) 降到 O(2n)。

**Gaussian, Sobel, and uniform filters are separable.**  
高斯、Sobel、均值核等都可以分离。

---

# 14. **Laplacian Filter**

**The Laplacian approximates the sum of second-order derivatives.**  
拉普拉斯算子近似计算二阶导数之和。

**It responds strongly to edges and zero-crossings.**  
它对边缘与零交叉反应明显。

**Kernel:  \[[0,1,0],[1,−4,1],[0,1,0]].**  
其典型核为 \[\[0,1,0],\[1,−4,1],\[0,1,0]]。

---

# 15. **Gradient Vector & Magnitude**

**The gradient vector points in the direction of strongest intensity increase.**  
梯度向量指向亮度上升最快的方向。

**Magnitude = sqrt(fx² + fy²).**  
梯度幅值 = sqrt(fx² + fy²)。

**Used for edge maps and edge strength.**  
用于生成边缘图和计算边缘强度。

---

# 16. **Edge Detection**

**Gradient magnitude detects edges via high-intensity changes.**  
梯度幅值通过检测亮度快速变化找到边缘。

**Laplacian detects edges via zero-crossings.**  
拉普拉斯通过零交叉点检测边缘。

**Correct scale (σ) is essential — too small detects noise, too large loses detail.**  
选择合适 σ（尺度）很重要——太小会检测到噪声，太大则会丢失细节。

---

# 17. **Differentiation in Fourier Domain**

**Differentiation becomes multiplication by (iω) in the frequency domain.**  
在频域中，求导对应乘以 (iω)。

**This boosts high frequencies, which also boosts noise.**  
求导会放大高频，从而也放大噪声。

---

# 18. **Sharpening Using Laplacian**

**A sharpened image can be computed as f − Laplacian(f).**  
锐化图像可以表示为 f − Laplacian(f)。

**This enhances edges by subtracting low-frequency content.**  
通过去除低频部分来强化边缘。

---

# 19. **Typical Exam Points**

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

> [!faq] Neighborhood Operations & Filtering Methods & Image Enhancement
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

![[Pasted image 20251116132108.png]]
B

