---
tags:
  - LectureNotes
---
## 1. Induction 数学归纳法
### Basic induction
Goal: Show P(n) holds for all n ∈ N. 
**Approach**: Show that: 
**Base case (B)**: P(0) holds; and 
**Inductive case (I)**: If P(k) holds then P(k + 1) holds. 
**Conclusion (C)**: P(n) holds for all n ∈ N.
## 2. Variations on Basic Induction
### Induction From m Upwards
![[Pasted image 20241114171430.png|525]]
### Induction Steps ℓ>1
![[Pasted image 20241114172032.png|500]]
![[Pasted image 20241114173858.png|500]]
### Strong Induction
![[Pasted image 20241114174154.png]]
![[Pasted image 20241114174324.png]]
![[Pasted image 20241114174336.png]]
### Negative Integers, Backward Induction
![[Pasted image 20241116135127.png]]
 
数学归纳法技巧：
1. 增添无效项 如 $8^{k+1}=8\cdot (8^k-2^k+2^k)$
2. 改写n+1项 如  $$\sum_{i=0}^{k+1}i=(\sum_{i=0}^{k+1}i)+(k+1)$$



1. 