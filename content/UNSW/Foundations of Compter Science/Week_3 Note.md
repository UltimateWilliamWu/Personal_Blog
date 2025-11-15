---
tags:
  - LectureNotes
---
## 1. Relations and Functions
>[!note] Definition
>An n-ary relation is a subset of the Cartesian product of n sets. 
>R ⊆ S1 × S2 × . . . × Sn
## 2. Binary relations
A binary relation between S and T is a subset of S × T : i.e. a set of ordered pairs.
### 2.1 Operatiosn for binary relations
![[Pasted image 20241005155947.png]]
## 3. Properties of Binary Relations
![[Pasted image 20241008202236.png]]
![[Pasted image 20241008210203.png]]
![[Pasted image 20241008214033.png]]
## 4.Functions
>[!important] Definition
>![[Pasted image 20241010111137.png]]
>domain 定义域 Dom(f) 
>co-domain 值域 Codom(f)
>- Function f : S → T is called an injection or 1-1 (one-to-one) if it satisfies (Inj) 单射
>- Function f : S → T is called a surjection or onto if it satisfies (Sur). That is, if lm(f)=Codom(f) 满射
>- Bijection 双射 同时满足单射和满射
>![[Pasted image 20241113192428.png]]
>![[Pasted image 20241113193454.png]]
### 4.1 Converse of a function
![[Pasted image 20241010111323.png]]
## 5. Equivalence Relations
![[Pasted image 20241011195958.png]]
### 5.1 Equivalence Classes and Partitions
![[Pasted image 20241112233954.png]]![[Pasted image 20241112234028.png]]
 >[!note] Partitions
 >![[Pasted image 20241112234128.png]]
The collection of all equivalence classes {[s] : s $\in$ S} forms a partition of S.
In the opposite direction, a partition of a set defines the equivalence relation on that set. If S=S1$\cup$....$S_k$, then we can define ∼⊆ S × S as: 
>- s ∼ t exactly when s and t belong to the same Si .
## 6. Partial Order
A partial order ⪯ on S satisfies R, AS, T.
We call (S, ⪯) a poset ---- partially ordered set
### 6.1 Hasse diagram
Every finite poset (S, ⪯) can be represented with a Hasse diagram: 
- Nodes are elements of S 
- An edge is drawn upward from x to y if x ≺ y and there is no z such that x ≺ z ≺ y
### Ordering Concepts
>[!note] Definition
>Let (S, ⪯) be a poset. 
>- x is an upper bound for A if a ⪯ x for all a ∈ A
>- x is a lower bound for A if x ⪯ a for all a ∈ A
>- The set of upper bounds for A is defined as ub(A) = {x : a ⪯ x for all a ∈ A}
>- The set of lower bounds for A is defined as lb(A) = {x : x ⪯ a for all a ∈ A}
>- The least upper bound of A, lub(A), is the minimum of ub(A) (if it exists)
>- The greatest lower bound of A, glb(A) is the maximum of lb(A) (if it exists)
### 6.2 glb and lub
To show x is glb(A) you need to show:
- x is a lower bound: x ⪯ a for all a ∈ A.
- x is the greatest of all lower bounds: If y ⪯ a for all a ∈ A then y ⪯ x.
### Ordering Concepts
>[!note] Definition
>Let (S, ⪯) be a poset.
>- (S, ⪯) is a lattice if lub(x, y ) and glb(x, y ) exist for every pair of elements x, y ∈ S.
>- (S, ⪯) is a complete lattice if lub(A) and glb(A) exist for every subset A ⊆ S.

![[Pasted image 20241112235614.png]]
![[Pasted image 20241112235707.png]]
### 6.3 Total orders
>[!note] Definition
>A total order is a partial order that also satisfies:
>(L) Linearity (any two elements are comparable):
>- For all x, y either: x ≤ y or y ≤ x (or both if x = y )

![[Pasted image 20241112235923.png]]
### 6.4 Ordering of a Poset ---- Topological Sort
>[!note] Definition
>For a poset (S, ⪯) any total order ≤ that is consistent with ⪯ (if a ⪯ b then a ≤ b) is called a topological sort.
### 6.5 Well-Ordered Sets
>[!note] Definiton
>A well-ordered set is a poset where every subset has a least element.
>>[!important] Take Notice
>>1. The greatest element is not required.
>>2. Well-ordered sets are an important mathematical tool to prove termination of programs. 
### 6.6 Orders for Cartesian products and languages
There are several practical ways of combining orders:
- Product order: Given posets (S, ⪯S ) and (T , ⪯T ), define: (s, t) ⪯ (s′, t′) if s ⪯S s′ and t ⪯T t′
- Lexicographic order: Given posets (S, ⪯S ) and (T , ⪯T ), define: (s, t) ≤lex (s′, t′) if s ⪯S s′ or (s = s′ and t ⪯T t′)
	- Extension to words: λ ≤lex w for all words
- Lenlex order: Lexicographic ordering, but order by length first.
>[!note] Product order
>- No implicit weighting. 
>- No bias toward any component.
>- In general, it is only a partial order, even if combining total orders.

>[!note] Lexicographic order
>- No implicit weighting. 
>- Gives total order when combining total orders. 
>- Can be sensibly extended to words.

>[!note] Lenlex order
>- Only applicable for languages (subsets of Σ∗). 
>- Gives total order when Σ is totally ordered. 
>- Gives an enumeration of Σ∗.