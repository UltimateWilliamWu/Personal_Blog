Introduction The goal of this optional self assessment is to review some important mathematical concepts that are used regularly in machine learning, and which are assumed knowledge for the course. If you find yourself struggling significantly with any aspects of this homework, please reach out to course staff so that we can better help you prepare for the course. Please also note that we have posted some helpful resources under the Week 0 tab on Moodle which may be of use to you for this homework.    
  
# Question 1. (Calculus Review)    
  
(a) Consider the function    
  
$$  
f(x,y)=a_{1}x^{2}y^{2}+a_{4}x y+a_{5}x+a_{7}  
$$    
  
compute all first and second order derivatives of $f$ with respect to    
  
(b) Consider the function    
  
$$  
f(x,y)=a_{1}x^{2}y^{2}+a_{2}x^{2}y+a_{3}x y^{2}+a_{4}x y+a_{5}x+a_{6}y+a_{7}  
$$    
  
compute all first and second order derivatives of $f$ with respect to $x$ and $y$ .    
  
(c) Consider the logistic sigmoid:    
  
$$  
\sigma(x)=\frac{1}{1+e^{-x}}  
$$    
  
show that $\begin{array}{r}{\sigma^{\prime}(x)=\frac{\partial\sigma}{\partial x}=\sigma(x)(1-\sigma(x))}\end{array}$    
  
(d) Consider the following functions:    
  
$$  
{\begin{array}{r l}&{\bullet\;\,y_{1}=4x^{2}-3x+3}\\ &{\bullet\;\,y_{2}=3x^{4}-2x^{3}}\\ &{\bullet\;\,y_{3}=4x+{\sqrt{1-x}}}\\ &{\bullet\;\,y_{4}=x+x^{-1}}\end{array}}  
$$    
  
Using the second derivative test, find all local maximum and minimum points.    
  
# Question 2. (Probability Review)    
  
(a) A manufacturing company has two retail outlets. It is known that $20\%$ of potential customers buy products from Outlet I alone, $10\%$ buy from both I and $\mathrm{II},$ , and $40\%$ buy from neither. Let $A$ denote the event that a potential customer, randomly chosen, buys from outel I, and $B$ the event that the customer buys from outlet II. Compute the following probabilities:    
  
$$  
P(A),\quad P(B),\quad P(A\cup B),\quad P(\bar{A}\cap\bar{B})  
$$    
  
Here, $\bar{A}$ denotes the complement of $A$ .    
  
(b) Let $X,Y$ be two discrete random variables, with joint probability mass function $P(X=x,Y=y)$ displayed in the table below:    
  
Compute the following quantities:    
  
(i) $r$ (ii) $P(X=2,Y=3)$     
(iii) $P(X=3)$ and $P(X=3|Y=2)$     
(iv) $\mathbb{E}[X],\mathbb{E}[Y]$ and $\mathbb{E}[X Y]$ (v) $\mathbb{E}[X^{2}],\mathbb{E}[Y^{2}]$     
(vi) $\operatorname{Cov}(X,Y)$     
(vii) $\operatorname{Var}(X)$ and $\operatorname{Var}(Y)$     
(viii) $\operatorname{Corr}(X,Y)$     
(ix) $\mathbb{E}[X+Y],\mathbb{E}[X+Y^{2}],\operatorname{Var}(X+Y)\;{\mathrm{and~}}\operatorname{Var}(X+Y^{2}).$    
  
# Question 3. (Linear Algebra Review)    
  
(a) Write down the dimensions of the following objects:    
  
$$  
\boldsymbol{A}=\left[\begin{array}{l l l l l}{1}&{3}&{1}&{0}&{2}\\ {1}&{1}&{4}&{1}&{2}\\ {1}&{1}&{1}&{5}&{2}\end{array}\right],\qquad\boldsymbol{b}=\left[\begin{array}{l}{1}\\ {1}\\ {1}\\ {3}\\ {2}\end{array}\right],\qquad\boldsymbol{A}^{T}  
$$    
  
(b) Consider the following objects:    
  
$$  
\begin{array}{r}{1=\left[\!\!\begin{array}{l l l}{1}&{3}&{4}\\ {2}&{2}&{1}\\ {6}&{4}&{3}\end{array}\!\!\right],\quad B=\left[\!\!\begin{array}{l l}{2}&{4}\\ {1}&{1}\end{array}\!\!\right],\quad C=\left[\!\!\begin{array}{l l l}{7}&{3}&{3}\\ {2}&{1}&{1}\\ {2}&{2}&{2}\end{array}\!\!\right],\quad D=\left[\!\!\begin{array}{l l}{4}&{2}\\ {4}&{6}\\ {1}&{3}\end{array}\!\!\right],\quad u=\left[\!\!\begin{array}{l}{1}\\ {1}\end{array}\!\!\right],\quad v=\left[\!\!\begin{array}{l}{2}\\ {4}\\ {1}\end{array}\!\!\right].}\end{array}  
$$    
  
Compute the following:    
  
(i) $A B$ and $B A$ (ii) $A C$ and $C A$ (iii) $A D$ and $D A$ (iv) $D C$ and $C D$ and $D^{T}C$ (v) $B u$ and $u B$ (vi) $A u$ (vii) $A v$ and $v A$ (viii) $A v+C v$    
  
(c) Consider the following objects:    
  
$$  
A=\left[\!\!{\begin{array}{c c c}{1}&{3}&{4}\\ {2}&{2}&{1}\\ {6}&{4}&{3}\end{array}}\!\!\right],\quad u=\left[\!\!{\begin{array}{c}{1}\\ {3}\end{array}}\!\!\right],\quad v=\left[\!\!{\begin{array}{c}{2}\\ {4}\\ {1}\end{array}}\!\!\right],\quad w=\left[\!\!{\begin{array}{c}{1}\\ {-2}\\ {2}\end{array}}\!\!\right].  
$$    
  
Compute the following:    
  
$$  
\begin{array}{r l}&{\|u\|_{1},\|u\|_{2},\|u\|_{2}^{2},\|u\|_{\infty}}\\ &{\|v\|_{1},\|v\|_{2},\|v\|_{2}^{2},\|v\|_{\infty}}\\ &{\|v+w\|_{1},\|v+w\|_{2},\|v+w\|_{\infty}}\\ &{\|A v\|_{2},\|A(v-w)\|_{\infty}}\end{array}  
$$    
  
(d) Consider the following vectors in $\mathbb{R}^{2}$    
  
$$  
u={\binom{1}{2}}\,,\quad v={\binom{1}{1}}\,,\quad w={\binom{-1}{1/2}}  
$$    
  
Compute the dot products between all pairs of vectors. Note that the dot product may be written using the following equivalent forms:    
  
$$  
\langle x,y\rangle=x\cdot y=x^{T}y.  
$$    
  
Then compute the angle between the vectors and plot.    
  
(e) Dot products are extremely important in machine learning, explain what it means for a dot product to be zero, positive or negative.    
  
(f) Consider the $2\times2$ matrix:    
  
$$  
A={\left[\begin{array}{l l}{1}&{3}\\ {4}&{1}\end{array}\right]}  
$$    
  
Compute the inverse of $A$ .    
  
(g) Consider the $2\times2$ matrix    
  
$$  
A={\left[\begin{array}{l l}{3}&{3}\\ {4}&{4}\end{array}\right]}  
$$    
  
Compute its inverse $A^{-1}$ .    
  
(h) Let $X$ be a matrix (of any dimension), show that $X^{T}X$ is always symmetric.