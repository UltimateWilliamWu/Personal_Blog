## 1. Counting Techniques
乘法法原理：完成一件事需要n个步骤 每个步骤有m种不同方法 $m\cdot m\cdot m$.....
加法原理：完成一件事有n种方法 每种方法有m种实现方式 m+m+m......
排列：从n个元素中选出m个元素 按一定顺序组成：
$$\mathrm{A}_m^n= \frac {m!}{(m-n)!}=(m)_n $$
组合：从n个元素中选出m组元素 排为一组：
$$\mathrm{C}_m^n=\frac{m!}{n!(m-n)!}= \left(\begin{matrix}m \\ n\end{matrix}\right)$$
## 2. The Union Rule
Union rule — S and T disjoint 
$$∣S ∪ T ∣ = ∣S∣ + ∣T ∣ $$
S1, S2, . . . , Sn pairwise disjoint (Si ∩ Sj = ∅ for i ≠ j) 
$$∣S1 ∪ . . . ∪ Sn∣ = ∑ ∣Si ∣$$
## 3. The Product Rule
Product rule:
$$|S_1\times ... \times S_k|=|S_1|\cdot|S_2|...|S_k|=\prod \limits_{i=1}^k|S_i|$$
![[Pasted image 20241116161833.png]]