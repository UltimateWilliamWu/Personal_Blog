---
tags:
  - LectureNotes
---
## 1. Notation for Numbers
- Natural numbers N={0,1,2,...}
- Integers Z={...-1,0,1,2...}
- Positive integers ={1,2,3,...}
- Rational numbers (fractions) 
	$Q={\frac mn : m,n∈Z,n\neq0}$
- Real numbers (decimal or binary expansions) 
	$R r=a_1a_2...a_k$
## 2. Floor and ceiling
$\lfloor x \rfloor$:  R → Z — floor of x, the greatest integer ≤ x
$\lceil x \rceil$: R → Z — ceiling of x, the least integer ≥ x
	$\lfloor −x\rfloor = − \lceil x \rceil, hence \lceil x\rceil = − \lfloor −x \rfloor$
**Let k, m, n ∈ Z such that k > 0 and m ≥ n. The number of multiples of k between n and m (inclusive) is**
	$\lfloor\frac mk \rfloor-\lfloor\frac {n-1}{k} \rfloor$
## 3.Divisibility
>[!note] Definition
For m, n ∈ Z, we say m divides n if n = k · m for some k ∈ Z. We denote this by m|n
Also stated as: ‘n is divisible by m’, ‘m is a divisor of n’, ‘n is a multiple of m’
>>[!important] Take Notice
>>Notion of divisibility applies to all integers — positive, negative and zero.
## 4. Gcd and Lcm
>[!note] Definition
>The **greatest common divisor** of m and n, gcd(m, n), is the largest ==positive== d ∈ Z such that d|m and d|n. 
>The **least common multiple** of m and n, lcm(m, n), is the smallest ==positive== k ∈ Z such that m|k and n|k. 
>Exception: gcd(0, 0) = lcm(0, n) = lcm(m, 0) = 0.

>[!important] 
>gcd(m, n) and lcm(m, n) are always taken as **non-negative** even if m or n is negative.

## 5. Primes and relatively prime
>[!note] Definition
>A number n > 1 is prime if it is only divisible by ±1 and ±n. m and n are relatively prime if gcd(m, n) = 1

>[!important] 
>$lcm(m,n)=\frac{mn}{gcd(m,n)}$

## 6. Euclid's gcd Algorithm
![[Pasted image 20241003150216.png]]
>[!note] Fact
>- For m > 0, n > 0 the algorithm always terminates.
>- For m, n ∈ Z, if m > n then gcd(m, n) = gcd(m − n, n)

![[Pasted image 20241113002556.png]]
>[!warning] Fact
>For m, n ∈ Z, if m > n then gcd(m, n) = gcd(m % n, n) 
>Proof. Let k = m div n. Then m % n = m − k · n.
## 7. Euclid's division lemma
For m ∈ Z, n ∈ Z>0 there exists q, r ∈ Z with 0 ≤ r < n such that
	m = q · n + r
	q = $\lfloor \frac{m}{n} \rfloor$
	r= m-q$\cdot$n
## 8. mod and div
>[!note] Definition
>Let m,p $\in$ Z, n $\in$ Z >0
>- m div n = $\lfloor \frac{m}{n} \rfloor$
>- m % n = m - ( m div n)$\cdot$n
>- m$=_{(n)}$p if n $\mid$ (m-p)
>>[!important] Notice
>>m$=_{(n)}$p is not standard. More commonly written as 
>>- m = p (mod n)

>[!warning] Fact
>- 0 ≤ (m % n) < n.
>- m =(n) p if, and only if, (m % n) = (p % n).
>- m =(n) (m % n)
>- If m =(n) m′ and p =(n) p′ then: 
>	- m + p =(n) m′ + p′ and m · p =(n) m′ · p′
