---
tags:
  - LectureNotes
---
## 1. Composition of functions
>[!note] Definition
>If f : S → T and g : T → U then the composition of f and g , written g ◦ f , is the function given by (g ◦ f )(x) = g (f (x)). That is, g ◦ f = f ; g.
## 2. Iteration of Functions 函数迭代
If a function maps a set into itself, i.e. when Dom(f ) = Codom(f ), the function can be composed with itself — iterated f ◦ f , f ◦ f ◦ f , . . . , also written f 2, f 3, . . .
## 3. Converse of a function
>[!note] Definition
>If $f^←$（逆映射）is a function then it is called the inverse function; denoted $f^{-1}$（逆函数）.
>$f^←$ only exists if f is a bijection. 
>$f^←$ always exists. 
>$f^{-1}$ is the procedure of “undoing” f .

>[!important] Fact
>If f : S → T and f −1 exists then: f −1 ◦ f = IdS and f ◦ f −1 = IdT . 
>Conversely, if f : S → T and g : T → S and g ◦ f = IdS and f ◦ g = IdT 
>then f −1 exists and is equal to g .
## 4. Matrices
转置矩阵
![[Pasted image 20241113201637.png]]
![[Pasted image 20241113201704.png]]
![[Pasted image 20241113202432.png]]
## 5. Big-O Notation
- **常数时间复杂度**：O(1)
- **对数时间复杂度**：O(log⁡n)
- **线性时间复杂度**：O(n)
- **线性对数时间复杂度**：O(nlog⁡n)
- **平方时间复杂度**：O($n^2$)
- **立方时间复杂度**：O($n^3$)
- **指数时间复杂度**：O($2^n$)
- **阶乘时间复杂度**：O(n!)
## 6. Boolean logic & Boolean Functions
![[Pasted image 20241113204216.png]]
![[Pasted image 20241113204242.png]]
## 7. Conjunctive and Disjunctive normal form
![[Pasted image 20241113205720.png]]
## 8. Karnaugh Maps
For up to four variables (propositional symbols) a diagrammatic method of simplification called Karnaugh maps works quite well. \
- For every propositional function of k = 2, 3, 4 variables we construct a rectangular array of 2k cells. 
- Column labels and row labels are ordered by Gray code. 
- Squares corresponding to the value true are marked with eg “+”. 
- We try to cover these squares with as few rectangles with sides 1 or 2 or 4 as possible.
## 9. Boolean Algebra
>[!note] Definition
>A Boolean algebra is a structure (T , ∨, ∧,′ , 0, 1) where 
>- 0, 1 ∈ T 
>- ∨, ∧ : T × T → T (called join and meet respectively) 
>- ′ : T → T (called complementation)

## 10. Duality
>[!note] Definition
>If E is an expression defined using variables (x, y , z, etc), constants (0 and 1), and the operations of Boolean Algebra (∧, ∨, and ′) then dual(E ) is the expression obtained by replacing ∧ with ∨ (and vice-versa) and 0 with 1 (and vice-versa).
>