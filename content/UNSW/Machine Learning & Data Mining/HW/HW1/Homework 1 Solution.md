---
tags:
  - Assignment
---
## Question 1. Data Wrangling    
(a) Create a variable X containing only features, and a variably y containing the target (Heart Disease). Remove the Last Checkup feature. 

>[!note] ScreenShot
![[Pasted image 20250306135258.png]]
![[Pasted image 20250306131200.png]]

>[!todo] Commentary
>1. Load dataset
>2. Separate features and target as required

(b) For Age, some values are negative. You are informed that this is a data entry error and negatives should be replaced with their positive versions. That is, $-x$ should be replaced with $x$ .  

>[!note] Screen Shot
![[Pasted image 20250306124535.png]]

>[!todo] Commentary
>1. Using abs() functions to get the positive number

(c) For Gender and Smoker, the variables have been coded in inconsistent ways. For example, Female gender is encoded as ‘Female’ and as  'F'. Write code to make these codings consistent. Then use categorical encoding instead. For gender, map (Male/M,Female/F, Unknown) to (0,1,2). For Smoker, map (No/N,Yes/Y,Nan) to (0,1,2).     

>[!note] Screen Shot
![[Pasted image 20250306131848.png]]

>[!todo] Commentary
>1. Using replace() for value substitution in a Series or DataFrame.
>2. Using map() for mapping existing values to new values, but it has a key difference: if a value is not found in the mapping dictionary, it is converted to NaN

(d) Blood pressure is given in the form systolic/diastolic. Write code to create two variables, systolic and diastolic. Remove the original blood pressure variable.     

>[!note] Screen Shot
![[Pasted image 20250306133945.png]]

>[!todo] Commentary
>1. Split Blood Pressure into Systolic and Diastolic with '/'
>2. Transfer into numeric
>3. Replace origin Blood Pressure

>[!FAQ] Why using pd.to_numeric() instead of astype() ?
>Since we dont know if the data is valid ,using pd.to_numeriv() handles missing or malformed values by converting them to NaN instead of causing an error.

(e) Using sklearn.model selection.train test split, split the data into training and test sets. Set the test size parameter to 0.3, and the random state to 2 for reproducibility.     

>[!note] Screen Shot
![[Pasted image 20250306135211.png]]
![[Pasted image 20250306135009.png]]

>[!todo] Commentary
>1. Set the test size parameter to 0.3, and the random state to 2 for reproducibility

(f) Now, note that some values in ‘Age’ in your test data are missing. We will manually impute values according to the following rule: If a Male (Female) is missing their age, set it to be the median of all other Male (Female) patients. Note that you should NOT use test data for this step, so your medians should be computed based on training set data. Be careful not to include missing values when calculating your median.  

>[!note] Screen Shot
![[Pasted image 20250306140247.png]]

>[!todo] Commentary
>1. Filter gender from the data and split into male and female
>2. Drop invalid values and calculate the median age
>3. Set the median age for patients who is missing their age 

>[!tip] Boolean Indexing
>- **No need for apply() or loops**, making execution significantly faster.
>- **More readable**, directly expressing the logic: “If Age is missing, assign the corresponding median based on Gender.”
>- **Avoids function definitions**, making the code cleaner and more efficient.

(g) Scale the columns: $'\mathrm{Age^{\prime}}$ , ’Height feet’, ’Weight kg’, ’Cholesterol’, ’Systolic’, ’Diastolic’ using a min-max normalizer. This means that for each feature, you should replace $x$ with    
  
$$  
{\frac{x-\operatorname*{min}}{\operatorname*{max}-\operatorname*{min}}},  
$$
where min, max are the minimum and maximum values for that feature column, respectively.     
Make sure to do this separately for train and test data. 

>[!note] Screen Shot
![[Pasted image 20250306142410.png]]

>[!todo] Commentary
>1. Fit & transform training data
>2. Transform test data (without fitting again)

(h) Plot a histogram of your target variable (from your training data). You should notice that a large portion of the target value is clustered around zero. Do you think linear regression is a reasonable model for this data? Create a new target variable by quantizing the original target variable. You can do this by setting values below a certain threshold (say 0.1) to be 0 and those above the threshold to be 1.  

>[!note] Screen Shot
![[Pasted image 20250306144813.png]]

>[!important] Result
>![[Pasted image 20250306174302.png|600]]

>[!FAQ] Linear regression is a reasonable model for this data?
>No. I don't think it's a suitable model for this data.
>- Scatter plots between numerical features (Age, Height_feet, Weight_kg, Cholesterol) and Heart_Disease show no clear linear relationship. The points are widely scattered, suggesting **non-linearity**.
>- When y $\approx$ 0 variance is low, but when y>0.1 variance is higher. **Variance is likely not constant** across different levels of predicted values.
>- The histogram of Heart_Disease shows that values are skewed towards 0, implying that residuals are **unlikely to be normally distributed**.

## Question 2. Regularized Logistic Regression    
(a) Consider the sklearn logistic regression implementation (section 1.1.11), which claims to minimize the following objective:    
  
$$  
\hat{w},\hat{c}=\arg\operatorname*{min}_{w,c}\left\{\mathrm{penalty}(w)+C\sum_{i=1}^{n}\log(1+\exp(-\tilde{y}_{i}(w^{T}x_{i}+c)))\right\}.  
$$    
  
It turns out that this objective is identical to our objective above (when the same penalty function is used), but only after re-coding the binary variables to be in $\{-1,1\}$ instead of binary values $\{0,1\}$ . That is, $\widetilde{y}_{i}\,\in\,\{-1,1\}$ whereas $y_{i}\,\in\,\{0,{1}\}$ . Argue rigorously that the two objectives are identical, in that they give us the same solutions $\hat{\beta}_{0}=\hat{c}$ and $\hat{\beta}=\hat{w}$ ). Further, describe the role of $C$ in the objectives, how does it compare to the standard Ridge parameter $\lambda$ as you have seen in the class? What to submit: some commentary/your working.    

>[!note] Proof
>Knowing that 
>$$
>L(\beta_{0},\beta)=penalty(\beta)+\frac{\lambda}{n}\sum_{i=1}^{n}\left[y_{i}\ln\left(\frac{1}{\sigma(\beta_{0}+\beta^{T}x_{i})}\right)+(1-y_{i})\ln\left(\frac{1}{1-\sigma(\beta_{0}+\beta^{T}x_{i})}\right)\right]
\\ \widetilde{y}_{i}\,\in\,\{-1,1\} 
>$$
>Suppose $z_i= {\beta_{0}+\beta^{T}x_{i}}$ we can get
>$$
>L(\beta_{0},\beta)=penalty(\beta)-\frac{\lambda}{n}\sum_{i=1}^{n}\left[y_{i}\ln\left({\sigma(z_i)}\right)+(1-y_{i})\ln\left(1-\sigma(z_i)\right)\right]
>$$
>From $\widetilde{y}_{i}\,\in\,\{-1,1\}$, $y_{i}\,\in\,\{0,{1}\}$ we can construct function $y_{i} = \frac{\left(\widetilde{y}_{i}+1\right)}{2}$ and we can get 
>$$
>L(\beta_{0},\beta)=penalty(\beta)-\frac{\lambda}{2n}\sum_{i=1}^{n}\left[(\widetilde{y}_{i}+1)\ln\left({\sigma(z_i)}\right)+(1-\widetilde{y}_{i})\ln\left(1-\sigma(Z_i)\right)\right]
>$$
>When $y_{i}=1$, which means $\widetilde{y}_{i}=1$ and we also know that $\sigma(z_{i})=(1+e^{-z_{i}})^{-1}$ so the form becomes
>$$
>\begin{aligned}
>L(\beta_{0},\beta)&=penalty(\beta)-\frac{\lambda}{n}\sum_{i=1}^{n}\ln({\sigma(Z_i)})\\ 
>&=penalty(\beta)-\frac{\lambda}{n}\sum_{i=1}^{n}\ln(\frac{1}{1+e^{-z_{i}}}) \\
>&=penalty(\beta)+\frac{\lambda}{n}\sum_{i=1}^{n}\ln(1+e^{-z_{i}})
>\end{aligned}
>$$
>Because when $y_{i}=1$, $-z_{i}=-y_{i}z_{i}$ so we can get
>$$
>\begin{aligned}
>L(\beta_{0},\beta)&=penalty(\beta)+\frac{\lambda}{n}\sum_{i=1}^{n}\ln(1+e^{-y_{i}z_{i}})
>\end{aligned}
>$$
>For the same reason when $y_{i}=0$, $\widetilde{y}_{i}=-1$, $z_{i}=-y_{i}z_{i}$ we can also get
>$$
>L(\beta_{0},\beta)=penalty(\beta)+\frac{\lambda}{n}\sum_{i=1}^{n}\ln(1+e^{-y_{i}z_{i}})
>$$
>For $\hat{\beta}_{0}=\hat{c}$ and $\hat{\beta}=\hat{w}$, $z_i= {\beta_{0}+\beta^{T}x_{i}}$ which is equal to 
>$$
>\hat{w},\hat{c}=\arg\operatorname*{min}_{w,c}\left\{penalty(w)+C\sum_{i=1}^{n}\log(1+\exp(-\tilde{y}_{i}(w^{T}x_{i}+c)))\right\}
>$$
>so prove has been done.

>[!FAQ]  Answer
>## The $C$ and $\lambda$ in the problem
>We see that:
>- The sklearn implementation uses **C as an inverse regularization parameter**, while our provided function uses **λ as a direct regularization parameter**.
>- The relationship between the two is: $$\lambda=Cn$$
>
>This means:
>- **Smaller C (smaller λ\lambdaλ) → Less regularization (weeker penalty on coefficients).**
>- **Larger C (larger λ\lambdaλ) → Larger regularization (stronger penalty on coefficients)**
>## The $C$ and the Ridge parameter $\lambda$ mentioned in class
>$$
>\begin{aligned}
>penalty(\beta) &=\frac{1}{2}\|\beta\|_{2}^{2} \\
>\lambda &= \frac{1}{2}
>\end{aligned}
>$$
>The standard Ridge parameter $\lambda$ in the problem I think is $\frac{1}{2}$ and has no realation with the $C$

(b) Create a grid of $100~C$ values using the code np.logspace(-4, 4, 100). For each $C_{.}$ , fit a logistic regression model (using the LogisticRegression class in sklearn) on the training data. Plot a series showing the train and test log-losses against $C$ . Be sure to use predict proba to generate predictions from your fitted models to plug into the log-loss. Also, use $\ell_{2}$ regularization, and the lbfgs solver when fitting your models. Discuss the shape of the two loss curves. How would you pick $C$ based on these plots? State your choice of $C$ .    

>[!note] Screen Shot
>![[Pasted image 20250307174432.png|1125]]

>[!important] Result
>![[Pasted image 20250307171755.png|600]]

>[!FAQ] Answer
>## Discussion on the shape
>The graph shows the log-loss values for the training and test datasets as a function of C (the inverse of regularization strength). The key observations are:
>1. **Left Side** (Small C, Strong Regularization)
>    - When C is very small (i.e., strong regularization), both **train** and **test** log-loss values are high.
>    - This suggests **underfitting**, meaning the model is too constrained and cannot capture important patterns in the data.
>1. **Middle Range** (Moderate C)
>	- As C increases, **both train and test log-loss values decrease**, indicating better model performance.
>	- There is an optimal region where both curves reach their lowest values, meaning the model balances bias and variance effectively.
>1. **Right Side** (Large C, Weak Regularization)
>	- When C becomes too large, the **training log-loss continues to decrease**, but the **test log-loss starts increasing slightly**.
>	- This suggests **overfitting**, where the model memorizes the training data but performs poorly on unseen data.
>## Choice of C
>Based on the plot, the optimal C appears to be in the range of $10$ to $100$.
>Final choice: C=50

(c)    Create a grid of $C$ values as before. For each value of $C$ in your grid, perform 5-fold cross validation (i.e. split the train data into 5 folds, fit logistic regression (using the settings from before) with the choice of $C$ on 4 of those folds, and record the log-loss on the $5\mathrm{th},$ repeating the process 5 times.) For this question, we will take the first fold to be the first $N/5$ rows of the training data, the second fold to be the next $N/5$ rows, etc, where $N$ denotes the number of observations in the training data.        

>[!note] Screen Shot
>![[Pasted image 20250307210035.png|800]]
>
>![[Pasted image 20250307210125.png|800]]

>[!important] Result
>![[Pasted image 20250307211248.png]]
>![[Pasted image 20250307204450.png|650]]

(d) In this part we will compare our results in the previous section to the sklearn implementation of gridsearch, namely, the GridSearchCV class. My initial code for this section looked like:    
```Python
from sklearn.model_selection import GridSearchCV 
param_grid = {’C’: Cs} 
grid_lr = GridSearchCV(estimator= 
						LogisticRegression(penalty=’l2’, 
											solver=’lbfgs’), 
							cv=5, 
							param_grid=param_grid) 
grid_lr.fit(X_train, y_train_q)
```
However, this gave me a very different answer to the result obtained by hand. Provide two reasons for why this is the case, and then, if it is possible, re-run the code with some changes to give consistent results to those we computed by hand, and if not, explain why. It may help to read through the documentation. What to submit: some commentary, a screen shot of your code for this section, a copy of your python code in solutions.py    

>[!note] Screen Shot
>![[Pasted image 20250308145651.png|850]]

>[!important] Result
>![[Pasted image 20250308145432.png]]

>[!todo] Commentary
>## 1. GridSearchCV Uses Stratified K-Folds by Default
>- **Difference**
>	- In the manual implementation, **we split the dataset sequentially into 5 equal parts (first N/5N/5N/5 rows, then next N/5N/5N/5, etc.)**.
>	- GridSearchCV, by default, uses **Stratified K-Folds**, which ensures that **each fold has the same proportion of positive and negative labels**.
>- **Effect Results**
>	- **Stratified folds** create a more balanced dataset across all folds, leading to **more stable and representative cross-validation results**.
>	- **Manual folds may be imbalanced**, leading to more variance and a different optimal C.
>## 2. GridSearchCV Shuffles Data Before Splitting
>- **Difference**
>	- The manual cross-validation **does NOT shuffle the data**, so **training and validation sets may be ordered and not truly random**.
>	- GridSearchCV **shuffles data before splitting into folds**.
>- **Effect on Results**
>	- If the dataset is ordered in a specific way, the **manual split might not represent the true distribution**, leading to different results.
>	- **Shuffling helps reduce the effect of ordering and gives more robust results**.
  
(e) Suppose that you were going to solve (1) using gradient descent and chose to update each coordinate individually. Derive gradient descent updates for each of the components $\beta_{0},\beta_{1},\dots,\beta_{p}$ for step size $\eta$ and regularization parameter $\lambda$ . That is, derive explicit expressions for the terms $\dagger$ in the following:    

$$  
\begin{array}{r l}&{\beta_{0}^{(k)}=\beta_{0}^{(k-1)}-\eta\times\dagger}\\ &{\beta_{1}^{(k)}=\beta_{1}^{(k-1)}-\eta\times\dagger}\\ &{\beta_{2}^{(k)}=\beta_{2}^{(k-1)}-\eta\times\dagger}\\ &{\qquad\qquad\vdots}\\ &{\beta_{p}^{(k)}=\beta_{p}^{(k-1)}-\eta\times\dagger}\end{array}  
$$

Make your expression as simple as possible, and be sure to include all your working. what to submit: your coordinate level $G D$ updates along with any working.    

>[!note] Answer
>From Q2(a) suppose $z_i= {\beta_{0}+\beta^{T}x_{i}}$ we can get
>$$
>L(\beta_{0},\beta)=penalty(\beta)-\frac{\lambda}{n}\sum_{i=1}^{n}\left[y_{i}\ln\left({\sigma(z_i)}\right)+(1-y_{i})\ln\left(1-\sigma(z_i)\right)\right]
>$$
>Knowing that $\sigma(z_{i})=(1+e^{-z_{i}})^{-1}$ and take the derivative $\sigma'(z_{i})=(1+e^{-z_{i}})^{-2}e^{-z_{i}}$ so we can get 
>$$
>\sigma'(z_{i})=\sigma(z_{i})(1-\sigma(z_{i}))
>$$
>Suppose $y_{i}\ln\left({\sigma(z_i)}\right)+(1-y_{i})\ln\left(1-\sigma(z_i)\right)=T$
>$$
>\begin{aligned}
>\frac{\partial T}{\partial z}&=y\frac{\sigma'(z)}{\sigma(z)}+(1-y)\frac{-\sigma'(z)}{1-\sigma(z)}\\
>&=\sigma'(z)\left(\frac{y}{\sigma(z)}{-\frac{1-y}{1-\sigma(z)}}\right)\\
>&=\sigma'(z)\cdot\frac{y-\sigma(z)}{\sigma(z)(1-\sigma(z))}\\
>&=y-\sigma(z)
>\end{aligned}
>$$
>According to the chain rule, we can get $\dagger$:
>$$
>\begin{aligned}
>\frac{\partial(L)}{\partial(\beta_{0})}&=-\frac{\lambda}{n}\cdot\frac{\partial(T)}{\partial(z)}\cdot\frac{\partial(z)}{\partial(\beta_{0})}\\
>&=-\frac{\lambda}{n}\cdot\sum_{i=1}^{n}(y_{i}-\sigma(z_{i}))\cdot\beta_{0}
>\end{aligned}
>$$
>$$
>\frac{\partial(L)}{\partial(\beta_{i})}=-\frac{\lambda}{n}\cdot\sum_{i=1}^{n}(y_{i}-\sigma(z_{i}))\cdot x_{i}y_{i}
>$$

(f) For the non-intercept components $\beta_{1},\ldots,\beta_{p},$ re-write the gradient descent updates of the previous question in vector form, i.e. derive an explicit expression for the term $\dagger$ in the following:    

$$  
\beta^{(k)}=\beta^{(k-1)}-\eta\times\dagger  
$$

Your expression should only be in terms of $\beta_{0},\beta,x_{i}$ and $y_{i}$ . Next, let $\gamma=[\beta_{0},\beta^{T}]^{T}$ be the $(p+1)$ - dimensional vector that combines the intercept with the coefficient vector $\beta$ , write down the update    
  
$$  
\gamma^{(k)}=\gamma^{(k-1)}-\eta\times\dagger.  
$$

Note: This final expression will be our vectorized implementation of gradient descent. The point of the above exercises is just to be careful about the differences between intercept and non-intercept parameters. Doing GD on the coordinates is extremely innefficient in practice. what to submit: your vectorized GD updates along with any working.

>[!note] Answer
>From the question q2(e), we now know that:
>$$
>\begin{aligned}
>\beta^{(k)}&=\beta^{(k-1)}-\eta\left[penalty(\beta)-\frac{\lambda}{n}\cdot\sum_{i=1}^{n}(y_{i}-\sigma(z_{i}))\cdot x_{i}\right]\\
>\beta_{0}^{(k)}&=\beta^{(k-1)}-\eta\left[-\frac{\lambda}{n}\cdot\sum_{i=1}^{n}(y_{i}-\sigma(z_{i}))\cdot\beta_{0}\right]
>\end{aligned}
>$$
>Knowing that $\gamma=\left(\begin{matrix}\beta_{0} \\ \beta_{T} \end{matrix}\right)$
>$$
>\begin{aligned}
>\gamma^{(k)}&=\left(\begin{matrix}\beta_{0}^{(k-1)} \\ \beta_{T}^{(k-1)} \end{matrix}\right)-\eta\cdot\left(\begin{matrix}0 \\ \nabla\beta \end{matrix}\right)+\frac{\lambda\eta}{n}\sum_{i=1}^{n}(y_{i}-\sigma(z_{i}))\cdot x_{i}\\
>\gamma^{(k)}&=\gamma^{(k-1)}+\frac{\lambda\eta}{n}\sum_{i=1}^{n}(y_{i}-\sigma(z_{i}))\cdot x_{i}
>\end{aligned}
>$$

