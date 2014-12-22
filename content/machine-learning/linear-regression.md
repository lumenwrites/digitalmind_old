Title: Linear regression
Date: 2014-12-20 12:00
Status: draft

Linear regression.  
Fitting line through the data  
Supervised learning(as opposed to unsupervised) - given the "right answer" for each example in the data.  
Regression(as oppoed to classification) - predict real-valued output.  
<br/>

## Model Representation

[house size vs prices graph]  
<br/>

[beautiful tutsplus-like data table size/prices]  

| Size (x) | Price(y) |
|----------|----------|
|     2104 |      460 |
|     1416 |      232 |
|     1534 |      315 |
|      852 |      178 |

Notation:  
$\textbf m$ - number of training examples  
$\textbf x$'s - "input" variable/features  
$\textbf y$'s - "output" variable/"target" variable  
$(x,y)$ - one training example  
$(x^{(i)},y^{(i)})$ - $i^{th}$ training example(not exponentiation)  

for example:  
$x^{(2)} = 1416$  
$y^{(3)} = 315$  


![linear-regression-hypothesis](/images/linear-regression/linear-regression-hypothesis.png)

h maps from x's to y's.

$h_\theta(x) = \theta_0 + \theta_1x $  
shorthand - $h(x)$, without the $_\theta$ subscript.

This is a linear regression with one variable, it's called univariate linear regression.

The goal is to choose the right parameters of $\theta_0$ and $\theta_1$, these parameters define the position of a line that goes throug the data.

3 graphs.
1.5;0
0; 0.5;
1; 0.5

The goal is to come up with parameters that produce the straight line that fits the data well.

Idea: Choose $\theta_0$ and $\theta_1$ so that $h(x)$ is close to $y$ for our taining examples $(x, y)$


## Cost function
$\underset{\theta_0 \theta_1}{minimize} \frac{1}{2m} \sum\limits_{i=1}^m (h(x^{(i)}) - y^{(i)})^2$.  
Explanation:
Minimize the difference between what our hypothesis function predicts($h(x)$), and the values of $y$ from the training examples.  
//why squared?  
$\frac{1}{2m}$ - "to make math easier for later" - ??  

$J(\theta_0 \theta_1) = \frac{1}{2m} \sum\limits_{i=1}^m (h(x^{(i)}) - y^{(i)})^2$.  
$\underset{\theta_0 \theta_1}{minimize} J(\theta_0 \theta_1)$.  
$J(\theta_0 \theta_1)$ - Cost function(squared error function).

## Cost funcion - intuition

Hypothesis:

$h_\theta(x) = \theta_0 + \theta_1x $

Parameters:

$\theta_0, \theta_1$

Cost function:

$J(\theta_0 \theta_1) = \frac{1}{2m} \sum\limits_{i=1}^m (h(x^{(i)}) - y^{(i)})^2$.  

Goal:

$\underset{\theta_0 \theta_1}{minimize} J(\theta_0 \theta_1)$.

### Simplified
$h(x)=\theta_1x$  
$\theta_0=0$  
Looking for $\theta_1$
$\underset{\theta_1}{minimize} J(\theta_1)$.  

$\theta_0$   controls the slope.

[graph with theta = 1]

Plotting cost function.
cost - amount of error.

j plot
3d theta 0,1 plot

contow plots

do both in matplotlib

<!--
<div class="wrapper">
<div class="bg">
This is your div with the specified aspect ratio.
sadfs
asdfsf j
sadf
sadf

</div>
</div>
-->

<!-- <div class="mermaid"> -->
<!-- graph TD; -->
<!-- 	A(Training Set)-\->B(Learning Algorithm); -->
<!-- 	B-\->C;	 -->
<!-- </div> -->
<!-- <div class="mermaid"> -->
<!-- graph LR; -->
<!-- 	I(Input)-\->H(h); -->
<!-- 	H-\->O(Output); -->
<!-- </div>	 -->

<!-- I(input)-\->C; -->
<!-- C-\->O(output); -->

<!-- C-\->|One|D[Result one]; -->
<!-- C-\->|Two|E[Result two]; -->

## Math

#### General Machine Learning introduction

- Vectors

- Dot Product

- Linear systems as matrices

- Matrix Multiplication

- Matrix Inverse


- Functions of several variables

- Partial derivatives

- Limits and continuity in R^n

- Linear Approximation

- Gradient

- Loss function

## Linear Regression
### Model representation
housing prices - better example
[graph]

supervised learnong, regression.
[table] size vsprice

m - number of training examples
x - "input" variable - features
y - output"("target") variable
(x,y) - one raining example
(x^(i), y^(i)) - i'th training example. i'th row of the table.

![linreg](/theme/images/linear-regression/linear-regression-gradient-descent.png)
## Gradient descent
