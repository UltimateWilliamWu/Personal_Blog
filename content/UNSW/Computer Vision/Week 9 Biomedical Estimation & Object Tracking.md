---
tags:
  - LectureNotes
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
