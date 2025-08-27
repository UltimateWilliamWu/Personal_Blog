---
tags:
  - LectureNotes
---
## 1. Sets
>[!note] Sets
>A set is a collection of objects (elements). If x is an element of A we write x ∈ A.
>- Tips:
>	- A set is defined by the collection of its elements. Order and multiplicity of elements is not considered. 
>	- We distinguish between an element and the set comprising this single element. Thus always a$\neq${a}. 
>	- Set ∅ = {} is empty (no elements); 
>	- Set {{}} is nonempty — it has one element.

>[!note] Subsets
>For sets S and T , we say S is a subset of T , written S ⊆ T , if every element of S is an element of T .
>- S ⊆ T includes the case of S = T
>- S ⊂ T a proper subset: S ⊆ T and S $\neq$ T
>- ∅ ⊆ S for all sets S
>- S ⊆ U for all sets S
>- N>0 ⊂ N ⊂ Z ⊂ Q ⊂ R
>- An element of a set; and a subset of that set are two different concepts
>
>**Difference between element and subset**
>a ∈ {a, b}, a $\not\subseteq$ {a, b}; 
## 2. Set Operation
### 2.1 Union
A ∪ B = {x : x ∈ A or x ∈ B}.
### 2.2 Intersection
A ∩ B = {x : x ∈ A and x ∈ B}
### 2.3 Complement
$A^c$ = {x : x ∈ U and x $\not\in$ A}.
### 2.4 Set Difference
A \\ B = A ∩ $B^c$
### 2.5 Symmetric Difference
A ⊕ B = (A \\ B) ∪ (B \\ A)
### 2.6 Power Set
The power set of a set X , Pow(X ), is the set of all subsets of X
### 2.7 Cardinality
The cardinality of a set X (various notation) is the number of elements in that set. |X | = #(X ) = card(X )
### 2.8 Cartesian Product
The Cartesian product of two sets S and T is the set of ordered pairs:
	S × T $=^{def}$ { (s, t) : s ∈ S, t ∈ T }
## 3. Formal Language
## 3.1 Symbols
Σ — alphabet, a finite, nonempty set
### 3.2 Words
>[!note] Definition of Words
>A word is a finite string (sequence) of symbols from Σ. 
>The empty word, λ, is the unique word with no symbols.

>[!note] Sets of Words
>- Σk or Σ=k : The set of all words of length k 
>- Σ≤k : The set of all words of length at most k 
>- Σ∗: The set of all finite words
>- Σ+: The set of all nonempty words

## 4. Set Equality
Two sets are equal (A = B) if they contain the same elements 
To show equality: 
- Examine all the elements 
- Show A ⊆ B and B ⊆ A 
- Use the Laws of Set Operations
## 5. Laws of Set Operations
For all sets A, B, C : 
Commutativity 
	A ∪ B = B ∪ A 
	A ∩ B = B ∩ A 
Associativity 
	(A ∪ B) ∪ C = A ∪ (B ∪ C )
	(A ∩ B) ∩ C = A ∩ (B ∩ C ) 
Distribution 
	A ∪ (B ∩ C ) = (A ∪ B) ∩ (A ∪ C ) 
	A ∩ (B ∪ C ) = (A ∩ B) ∪ (A ∩ C ) 
Identity 
	A ∪ ∅ = A
Complementation 
	A ∪ ($A^C$ ) = U 
	A ∩ ($A^C$ ) = ∅  
## 6. Derived Laws
![[Pasted image 20241005151354.png|475]]
## 7. Two useful results
![[Pasted image 20241005152536.png]]
![[Pasted image 20241113003942.png]]
