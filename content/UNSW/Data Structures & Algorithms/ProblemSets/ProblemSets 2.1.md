---
tags:
  - Assignment
---
## 1. (Counting primitive operations)
The following algorithm
- takes a sorted array A[1.._n_] of characters
- and outputs, in reverse order, all 2-letter words νω such that ν≤ω.
```
for all i=_n_ down to 1 do  //2n+1 
      for all j=_n_ down to _i_ do //n(n+2)
          print "A[i]A[j]"  //n(n+1)
      end for  
  end for
```
Count the number of primitive operations (evaluating an expression, indexing into an array). What is the time complexity of this algorithm in big-Oh notation?
**Primitive operations:**  $2n^2+5n+1$
**Big-Oh notation:** O($n^2$)
## 2. (Big-Oh Notation）
1. Prove mathematically that $$\sum_{i=1}^{n}i^2\in O(n^3)$$
	
> [!NOTE] Answer
> $$1+2+...+n=\frac {n(n+1)(2n+1)} 6=O(n^3)$$
2. Prove mathematically that $$\sum_{i=1}^nlog\ i\in O(n\ log\ n)$$

> [!NOTE] Answer
> $$\sum_{i=1}^nlog\ i\leq \sum_{i=1}^nlog\ n=O(n\ log\ n)$$

3. Prove mathematically that $$\sum_{i=1}^n\frac i {2^i}\in O(1)$$

> [!NOTE] Answer
> $$Let\ S=\sum_{i=1}^n\frac i {2^i}\ Then\ S=\sum_{i=1}^n\frac 1 {2^i}+\sum_{i=1}^n\frac {i-1} {2^i}=\sum_{i=1}^n\frac 1 {2^i}+\sum_{i=1}^{n-1}\frac {i} {2^{i+1}}<1+\frac 1 2 S\;\; Therefore\; S<2$$
### 3. (Algorithms and complexity)
Develop an algorithm to determine if a character array of length contains at least one letter more than once. For example, "repeat" is such a word but "until" is not
1. Write the algorithm in pseudocode.
2. Analyse the time complexity of your algorithm.
3. Implement your algorithm in C as a function
```C
#include<stdio.h>
#include<stdbool.h>
#include<string.h>

bool hasRepeatedLetter(char A[]){
    int size=strlen(A);
    for(int i=0;i<size;i++){
        for(int j=i+1;j<size;j++){
            if(A[i]==A[j]){
                return true;
            }
        }
    }
    return false;
}

int main(void){
    char str[32];
    printf("Enter a word:");
    scanf("%31s",str);
    bool result=hasRepeatedLetter(str);
    if(result==1){
        printf("yes");
    }else{
        printf("no");
    }
    return 0;
}
```
