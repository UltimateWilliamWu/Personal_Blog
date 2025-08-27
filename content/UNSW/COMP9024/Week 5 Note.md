---
tags:
  - LectureNotes
---
## 1. Strings
Notation: length(P) … # characters in P 
- λ … empty string (length(λ) = 0) 
- Σm … set of all strings of length m over alphabet Σ 
- Σ* … set of all strings over alphabet Σ 
νω denotes the concatenation of strings ν and ω
-  Note: length(νω) = length(ν)+length(ω) λω = ω = ωλ
## 2. Pattern Matching（字符串匹配）
Pattern（模式串）:匹配的字符串
Text（字符串）:被匹配的字符串
### 2.1 Boyer-Moore Algorithm（博伊尔算法）
1. 计算匹配表：记录字符串中的所有字符最后一次在模式串中出现的下标
2. 根据公式$$i=i+m-min(j,1+L[T[i]])$$ 当字符不匹配时，记录在字符串中与模式串中不同的字符并计算移动之后的下标随后跳跃字符串
3. 注意：博伊尔算法从字符串尾部开始匹配
![[Pasted image 20250211234956.png]]
```C
BoyerMooreMatch(T,P,Σ): 
Input text T of length n, pattern P of length m, alphabet Σ 
Output starting index of a substring of T equal to P 
	-1 if no such substring exists 
	
	L=lastOccurenceFunction(P,Σ) 
	i=m-1, j=m-1 // start at end of pattern 
	repeat 
		if T[i]=P[j] then 
			if j=0 then 
				return i // match found at i 
			else 
				i=i-1, j=j-1 // keep comparing 
			end if 
		else // character-jump 
			i=i+m-min(j,1+L[T[i]]) 
			j=m-1 
			end if 
		until i≥n 
	return -1 
```
### 2.2 KMP（KMP算法）
1. 与博伊尔算法类似 不同的是建立匹配表的方式不同，KMP算法是计算前缀以及后缀的最长公共子串长度作为移动距离：移动位数 = 已匹配的字符数 - 对应的部分匹配值
	1. ![[Pasted image 20250211235109.png]]
2. KMP算法是从头开始匹配
### 2.3 Tries（字典树）
## 3. Huffman Code/Tree（霍夫曼编码）
## 4. Approximation（近似估计算法）
## 5. Randomised Algorithms
### 5.1 Linear Congruential Generator LCG
### 5.2 Non-randomised Quicksort



