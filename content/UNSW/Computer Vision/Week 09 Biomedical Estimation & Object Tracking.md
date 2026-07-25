---
tags:
  - UNSW
  - UNSW/COMP9517
  - Topic/ComputerVision
  - Type/Lecture
---
## ⭐ What is Motion Estimation?

Motion estimation analyzes changes across frames to determine pixel/object movement.  
运动估计是通过分析图像序列的变化来推测像素或物体的移动。

It is the foundation of video analysis, tracking, and action recognition.  
它是视频分析、跟踪和动作识别等任务的基础。

---

# ⭐ 1. Why Motion Estimation?

Changes across time reveal object movement.  
随时间的变化揭示了物体的运动。

Used for tracking, surveillance, recognition, navigation, and activity detection.  
用于跟踪、监控、识别、导航、行为检测等。

---

# ⭐ 2. Motion Estimation Scenarios

## ⭐ Still camera

Still camera + changing objects → only objects move.  
静止相机 + 有物体移动 → 场景只有物体在动。

## ⭐ Moving camera

Camera moves → entire scene moves + possible object motion.  
相机移动 → 整个场景一起移动 + 可能的物体运动。

---

# ⭐ 3. Types of Motion Estimation

## ⭐ Change Detection（检测变化）

Detect moving objects using image subtraction.  
通过图像差分检测运动物体。

## ⭐ Sparse Motion Estimation（稀疏运动估计）

Track a set of key points (corners / interesting points).  
跟踪特征点（角点、兴趣点）。

## ⭐ Dense Motion Estimation（光流 Optical Flow）

Compute motion vector at every pixel.  
在每个像素估计运动矢量（光流）。

---

# ⭐ 4. Change Detection（基础运动检测）

## ⭐ Simple idea

Subtract current frame and previous frame → find changed pixels.  
当前帧减去前一帧 → 找到发生变化的像素。

Works best when background is static.  
背景不变时效果最好。

---

## ⭐ Image Subtraction Steps

1. Capture background image.  
    获取静态背景图。
    
2. Subtract background from each new frame.  
    新帧 - 背景。
    
3. Threshold the difference.  
    对差分图阈值化。
    
4. Use connected components to find moving regions.  
    连通域提取移动物体。
    
5. Optionally remove noise and apply closing.  
    可去噪并使用闭运算融合小区块。
    

输出：二值运动区域 + bounding boxes。  
得到运动区域和外接框。

---

# ⭐ 5. Sparse Motion Estimation（稀疏运动）

## ⭐ What idea?

Track only a few “interesting points” instead of all pixels.  
不追踪所有像素，只跟踪关键点（兴趣点）。

Efficient and robust.  
效率高且鲁棒。

---

## ⭐ Step 1. Detect interesting points

Use edge/corner detectors: Canny, Harris, SIFT, CNN features.  
利用边缘、角点或特征检测器找到关键点。

Interest operator measures local intensity variance.  
兴趣点算子通过局部亮度变化判断是否为关键点。

---

## ⭐ Step 2. Template Matching

For each point:  
Take a patch at time t and find best match at t + Δt in search window.  
对每个点：取时间 t 的小 patch，在 t+Δt 的邻域中搜索最匹配的 patch。

This yields a displacement vector → motion vector.  
得到位移向量，即运动矢量。

---

## ⭐ Similarity Measures

- Cross-correlation → maximize  
    交叉相关（最大化）
    
- SAD (sum absolute differences) → minimize  
    绝对差和（最小化）
    
- SSD (sum squared differences) → minimize  
    平方差和（最小化）
    
- Mutual information → maximize  
    互信息（最大化）
    

---

# ⭐ 6. Dense Motion Estimation — Optical Flow（光流）

## ⭐ Dense motion = motion at every pixel

光流 = 每个像素的运动估计。

Requires assumptions about pixel appearance staying constant over time.  
要求像素外观在短时间内基本不变。

---

## ⭐ Brightness Constancy Assumption

A pixel's intensity does not change as it moves.  
像素随运动其亮度不变。

This leads to the optical flow constraint equation.  
这引出了光流约束方程。

---

## ⭐ Optical Flow Constraint Equation

From Taylor expansion:  
根据泰勒展开，可得：

$$  
f_x v_x + f_y v_y = - f_t  
$$

Meaning: spatial gradient ⋅ velocity = negative temporal gradient.  
含义：空间梯度 · 速度 = 负的时间梯度。

---

## ⭐ Why optical flow is hard?

This is **one equation with two unknowns** → under-determined.  
光流方程只有一个方程两个未知数 → 无唯一解。

Need extra constraints → smoothness or neighbourhood consistency.  
需额外假设（邻域平滑假设）才能求解。

---

## ⭐ Lucas–Kanade Optical Flow

Assume neighbouring pixels share one motion vector.  
假设小邻域内所有像素速度一致。

This yields an over-determined linear system → solve by least squares.  
得到过定方程组 → 最小二乘求解。

Commonly used in real-time tracking.  
广泛用于实时跟踪。

---

# ⭐ 7. Example Exam Question（来自 PPT）

## ❓ Which statement is incorrect?

A. Subtraction works best with constant background  
B. Sparse motion uses template matching + MI  
C. Dense estimation assumes neighbourhood is constant over time  
D. Optical flow gives one equation per pixel but needs extra constraints

## ✔️ Correct answer: **B**

Because MI is **maximized**, not **minimized**.  
因为互信息是 **最大化** 而非最小化，因此 B 错。

（稀疏估计可使用 MI，但不是“通过最小化 MI”。）

---

# ⭐ Summary（你考试要记住的点）

Motion estimation = analyzing temporal change for detection/tracking.  
运动估计 = 从时间变化中提取运动。

Three levels: change detection, sparse motion, dense motion.  
三类：变化检测、稀疏运动、光流。

Change detection uses image subtraction.  
变化检测用图像差分。

Sparse motion uses feature points + template matching.  
稀疏运动用兴趣点 + 模板匹配。

Dense motion uses optical flow.  
稠密运动用光流。

Optical flow constraint gives fx vx + fy vy = –ft.  
光流约束方程 fx vx + fy vy = –ft。

Optical flow is under-determined → need neighbourhood constraints.  
光流方程欠定 → 需邻域平滑假设。

Lucas–Kanade = least-squares solution in small patch.  
Lucas–Kanade = 小邻域内最小二乘求解。

## ⭐ What is Object Tracking?

Object tracking estimates the motion and location of an object across time in a video.  
目标跟踪是在视频中随时间持续推测物体的位置与运动。

Tracking outputs a “trajectory” rather than a single detection.  
跟踪的输出是物体的轨迹，而不是单帧检测结果。

---

## ⭐ Why do we need tracking?

Tracking helps follow objects over time in surveillance, navigation, and recognition tasks.  
跟踪可以持续追踪目标，在监控、导航、识别等任务中至关重要。

It connects detections into a time-consistent sequence.  
它把逐帧检测结果连成连续的轨迹。

---

# ⭐ Object Tracking Applications

Object tracking is used in motion capture, surveillance, recognition from motion, and targeting.  
目标跟踪用于动作捕捉、监控、利用运动识别物体、目标打击等场景。

Tracking systems must handle noise, occlusion, fast motion, and illumination changes.  
跟踪系统需要应对噪声、遮挡、快速运动和光照变化。

---

# ⭐ Challenges in Object Tracking

Tracking must cope with noise, image artifacts, occlusions, nonrigid objects, and real-time constraints.  
跟踪必须应对噪声、伪影、遮挡、非刚性物体、以及实时性需求。

Object appearance may change over time, making tracking unstable.  
物体外观随时间变化会导致跟踪不稳定。

---

# ⭐ Motion Assumptions (Very Important!)

Objects move smoothly in position and velocity.  
物体的“位置”与“速度”随时间缓慢变化。

Objects cannot occupy the same space at the same time.  
两个物体不能在相同位置重叠。

Motion continuity is key to connecting detections into tracks.  
运动连续性是假设轨迹连续的关键。

---

# ⭐ Approaches to Tracking

COMP9517 focuses on **Bayesian inference**, **Kalman filtering**, and **Particle filtering**.  
本课程重点介绍 **贝叶斯推断**、**卡尔曼滤波**、与 **粒子滤波**。

These methods combine prediction + measurement to estimate state over time.  
这些方法通过“预测 + 测量”迭代更新物体状态。

---

# ⭐ State and Measurement

The object has a hidden state (position, velocity, shape).  
目标具有隐藏状态（位置、速度、形状等）。

We observe measurements derived from image features.  
从图像特征中得到可观测的测量值。

Tracking = infer the hidden state from noisy measurements.  
跟踪 = 从噪声测量中恢复隐藏的真实状态。

---

# ⭐ Bayesian Inference (General Framework)

Tracking is a recursive Bayesian estimation problem.  
跟踪是一个递归的贝叶斯估计问题。

Each timestep consists of:  
每个时间步骤包含三部分：

---

## ⭐ Prediction

Predict current state from previous state using a motion model.  
根据运动模型，从前一状态预测当前状态。

---

## ⭐ Association

Select which measurements correspond to the object.  
选择哪些测量值属于该物体（数据关联）。

---

## ⭐ Correction

Update prediction using current measurement and Bayes rule.  
用当前测量通过贝叶斯规则修正预测。

---

# ⭐ Hidden Markov Model Assumptions

The next state depends only on the previous state.  
下一状态只依赖上一状态（马尔可夫性）。

The measurement depends only on the current state.  
测量值只依赖当前状态。

Tracking under these assumptions becomes HMM inference.  
在这些假设下，跟踪变为隐马尔可夫模型问题。

---

# ⭐ Estimating the Final State

Two common estimates are:  
常用的两种估计是：

- EAP: expected a posteriori (mean)  
    EAP：后验分布的均值
    
- MAP: maximum a posteriori  
    MAP：后验概率最大的点
    

---

# ⭐ Kalman Filtering (Linear + Gaussian Case)

Kalman filter assumes linear dynamics and Gaussian noise.  
卡尔曼滤波假设线性系统 + 高斯噪声。

It represents state as a Gaussian with mean + covariance.  
状态被表示为高斯分布的均值和方差。

---

## ⭐ Kalman Filter Steps

### Prediction

Use matrix A to predict next state.  
用矩阵 A 预测下一状态。

### Correction

Use Kalman gain K to combine prediction and measurement.  
用卡尔曼增益 K 把预测与测量结合。

Kalman filter is optimal for linear-Gaussian systems.  
卡尔曼滤波是线性高斯系统的最优估计器。

---

# ⭐ Particle Filtering (Nonlinear + Non-Gaussian Case)

Particle filtering represents state distribution using many weighted samples.  
粒子滤波通过大量带权重的样本（粒子）表示状态分布。

It approximates Bayesian inference without assuming Gaussian/linear models.  
无需高斯/线性假设，可以近似任意复杂分布。

Each timestep:  
每一步包含：

1. Propagate particles (predict)  
    传播粒子（预测）
    
2. Reweight them using measurement likelihood  
    根据测量更新权重
    
3. Resample to keep high-weight particles  
    重采样保留高权重粒子
    

---

# ⭐ Kalman vs Particle Filtering

Kalman → fast, optimal for linear-Gaussian; cannot handle complex motion.  
卡尔曼 → 快速、适用于线性高斯；无法处理复杂非线性运动。

Particle → handles arbitrary nonlinear motion and multi-modal distributions.  
粒子 → 可处理任意非线性、多峰运动，但计算更慢。

---

# ⭐ Example Applications

Tracking active contours of objects.  
用于主动轮廓（snake）模型的跟踪。

Pedestrian tracking using bounding box state.  
用于行人框位置跟踪。

Particle filtering works well in clutter or occlusions.  
粒子滤波在遮挡、杂乱背景中表现更佳。

---

# ⭐ Example Exam Question

Which statement is incorrect?  
哪个选项是错误的？

Correct answer: **A**（假设错误）  
正确答案：**A**

Explain: Particle filtering does **not** assume a parametric form; it uses samples.  
原因：粒子滤波不要求模型参数化，它用样本近似分布。

---

# ⭐ Summary（你考试需要背下来的）

Object tracking = predict + associate + correct.  
跟踪 = 预测 + 关联 + 修正。

Bayesian inference is the general framework.  
贝叶斯推断是通用框架。

Kalman filter works for linear-Gaussian systems.  
卡尔曼滤波适用于线性高斯系统。

Particle filter handles nonlinear + non-Gaussian motion.  
粒子滤波适用于非线性 + 非高斯情况。

State transitions follow Markov assumption.  
状态转移满足马尔可夫假设。

Measurements depend only on current state.  
测量只依赖当前状态。
