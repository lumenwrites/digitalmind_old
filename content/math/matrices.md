Title: Matrices and vectors
Date: 2015-02-13
Slug: matrices-and-vectors
Category: math
Status: draft

This is an introduction to matrices and vectors and basic operations on them.
<!-- If you wanted to read about the enslavement of a human race by the malevolent machines - wait 20-30 years and read /r/worldnews. -->

<div class="panel">
<ul>
	<li><a href="#matrices"> Matrices</a></li>
	<li><a href="#vectors"> Vectors</a></li>
	<li><a href="#addition-and-subtraction"> Addition and subtraction </a></li>
	<li><a href="#scalar-multiplication-and-division"> Scalar multiplication and division </a></li>
	<li><a href="#dot-product"> Dot product </a></li>
	<li><a href="#matrix-multiplication"> Matrix multiplication </a></li>
	<li><a href="#inversion"> Inversion </a></li>
	<li><a href="#identity-matrix"> Identity matrix </a></li>
	<li><a href="#transpose"> Transpose </a></li>		
	<!-- <li><a href="#resources"> Other Resources</a></li>	 -->
</ul>
</div>

<span id="matrices">
### Matrices
**Matrix** is just a convention for representing the data that is very useful for solving all kinds of problems. Yes, just that. If you wanted to read about the virtual reality built by the malevolent machines for the purposes of enslaving the human race - wait 20-30 years and read /r/worldnews.

<!-- **Matrices** are just a convention for representing the data that is very useful for solving all kinds of problems. -->
<!-- If you're disappointed that it isn't a virtual reality built by machines to enslave human race... -->

For example, matrices can be used to represent:

- Linear equations.
- Pixels on a screen (useful for computer graphics)
- Points in a coordinate space.
- The training data for a Machine Learning problem.
- Many other things.

A matrix looks like a table of numbers within square brackets. For example this is a matrix:

$$
A
=
\begin{bmatrix}
1 & 42  & 6 \cr
0 & 13  & 4 \cr
2 & 8 & 15 \cr
16 & 23 & 32 \cr
\end{bmatrix}
$$


This matrix has 4 **rows** and 3 **columns**, therefore it is called 4x3 ("4 by 3") matrix.
The number of rows/columns a matrix as is called it's "**dimensions**".

If you want to refer to a specific **element**("entry") of a matrix, for example a number in a 3rd row, 2nd column, you can do it like this:

$$
A_{3,2} = 8
$$

$ A_{ij} $ is an element of a matrix , in the $ i^{th} $ row, $ j^{th} $ column.


<span id="vectors">
### Vectors

Vector is a special case of a matrix, a matrix that has only one row or one column(nx1, or 1xn matrix).
<!-- vector is one-dimensional matrix -->

Matrices with only one row are called **row vectors**, and the ones that have only one column are called **column vectors**.

This is a 3-dimensional column vector:

$$
\vec{y} =
\begin{bmatrix}
23 \cr
31 \cr
42
\end{bmatrix}
$$


$ \vec{y}_i $ is an $ i^{th} $ element of a vector. For example $ \vec{y}_2 = 31 $.

<!--
Sometimes vectors are 1-indexed(numbers of elements start with 1):
$$
\vec{y} =
\begin{bmatrix}
y_1 \cr
y_2 \cr
y_3 \cr
y_4
\end{bmatrix}
$$

and sometimes they're 0-indexed:
$$
\vec{y} =
\begin{bmatrix}
y_0 \cr
y_1 \cr
y_2 \cr
y_3
\end{bmatrix}
$$

In math 1-indexed vectors are more common, but in ML 0-indexed are more convenient.

In my math articles I'll use 1-indexed vectors.
-->

By convention, capital letters usually refer to matrices, and lowercase letters are used for vectors.



## Basic operations  <!-- on matrices -->

<span id="addition-and-subtraction">
### Addition and subtraction

To add matrices together you simply add up the corresponding elements one at a time.


<!-- <div class="bg-no-frame"> -->
$$
\begin{bmatrix}
1 & 0 \cr
2 & 13 \cr
3 & 6
\end{bmatrix}
+
\begin{bmatrix}
4 & 7 \cr
8 & 0.5 \cr
22 & -1 \cr
\end{bmatrix}
=
\begin{bmatrix}
(1 + 4) & (0 + 7) \cr
(2 + 8) & (13 + 0.5) \cr
(3 + 22) & (6 - 1) \cr
\end{bmatrix}
=
\begin{bmatrix}
5 & 7 \cr
10 & 13.5 \cr
25 & 5 \cr
\end{bmatrix}
$$
<!-- </div> -->

Because vectors are just special cases of matrices, the same applies to them.

Subtraction is the same, you simply subtract the corresponding elements.

You can only add/subtract matrices of the same dimension.

<!-- Just like with numbers, matrix addition/subtraction has the property of /??, A+B = B+A -->

<span id="scalar-multiplication-and-division">
### Scalar multiplication and division

To multiply a matrix by a number(scalar) you multiply each of it's elements by that number.

$$
3 *
\begin{bmatrix}
1 & 0 \cr
2 & 5 \cr
3 & 1
\end{bmatrix}
=
\begin{bmatrix}
3 & 0 \cr
6 & 15 \cr
9 & 3 \cr
\end{bmatrix}
$$

Similar with division:
$$
\begin{bmatrix}
4 & 0 \cr
6 & 12
\end{bmatrix}
/2
=
\begin{bmatrix}
2 & 0 \cr
3 & 6 \cr
\end{bmatrix}
$$

(because dividing by a number is the same as multiplying by 1 divided by a number.)

<span id="dot-product">
### Dot product

Let's say we have 2 vectors:

$$
\vec{a} =
\begin{bmatrix}
3 & 2 \cr
\end{bmatrix}
$$

$$
\vec{b} =
\begin{bmatrix}
7 \cr
9 \cr
\end{bmatrix}
$$

To find the dot product, you need to multiply the corresponding elements, and then add the results together:

$$
3 * 7 + 2 * 9 = 39
$$

<span id="matrix-multiplication">
### Matrix multiplication

Matrix multiplication is a little more elaborate than addition.

Let's say we want to multiply matrices $A$ and $B$ to get the resulting matrix $C$.

<div class="mathjax-align-left">
$$
A =
\begin{bmatrix}
\color{Lightseagreen}1 & \color{Lightseagreen}2 \cr
\color{Purple}3 & \color{Purple}4 \cr
\end{bmatrix}
$$

$$
B =
\begin{bmatrix}
\color{#CD5F5F}5 & \color{Green}6 \cr
\color{#CD5F5F}7 & \color{Green}8 \cr
\end{bmatrix}
$$

$$
C =
\begin{bmatrix}
c_{11} & c_{12} \cr
c_{21} & c_{22} \cr
\end{bmatrix}
=
?
$$
</div> <!-- End align -->

To get the resulting elements of a matrix $C$ you need to find a dot product of a corresponding *row* from the matrix $A$ and the *column* from the matrix $B$.

For example to find $c_{11}$, you calculate a dot product of the *first* row of a matrix $A$ and a *first* column of a matrix $B$.

<div class="mathjax-align-left">
$$
c_{11} =
\color{Lightseagreen}1 * \color{#CD5F5F}5 + \color{Lightseagreen}2 * \color{#CD5F5F}7
= 19
$$

You can do the same for the rest of the elements:

$$
c_{12} =
\color{Lightseagreen}1 * \color{Green}6 + \color{Lightseagreen}2 * \color{Green}8
= 22
$$

$$
c_{21} =
\color{Purple}3 * \color{#CD5F5F}5 + \color{Purple}4 * \color{#CD5F5F}7 
= 43
$$

$$
c_{22} =
\color{Purple}3 * \color{Green}6 + \color{Purple}4 * \color{Green}8
= 50
$$

Now we put them together in a result:

$$
C =
\begin{bmatrix}
c_{11} & c_{12} \cr
c_{21} & c_{22} \cr
\end{bmatrix}
=
\begin{bmatrix}
19 & 22 \cr
43 & 50 \cr
\end{bmatrix}
$$

Here it all together, for clarity:

$$
\begin{bmatrix}
\color{Lightseagreen}1 & \color{Lightseagreen}2 \cr
\color{Purple}3 & \color{Purple}4 \cr
\end{bmatrix}
*
\begin{bmatrix}
\color{#CD5F5F}5 & \color{Green}6 \cr
\color{#CD5F5F}7 & \color{Green}8 \cr
\end{bmatrix}
=
\begin{bmatrix}
(\color{Lightseagreen}1 * \color{#CD5F5F}5 + \color{Lightseagreen}2 * \color{#CD5F5F}7) & (\color{Lightseagreen}1 * \color{Green}6 + \color{Lightseagreen}2 * \color{Green}8) \cr
(\color{Purple}3 * \color{#CD5F5F}5 + \color{Purple}4 * \color{#CD5F5F}7) & (\color{Purple}3 * \color{Green}6 + \color{Purple}4 * \color{Green}8) \cr
\end{bmatrix}
=
\begin{bmatrix}
19 & 22 \cr
43 & 50 \cr
\end{bmatrix}
$$

</div> <!-- end align -->

Properties of matrix multiplication:

- You can only multiply matrices when the number of columns of the first one equals the number of rows of the second one.

- Multiplying m x n matrix (m rows, n columns) by n x o matrix(n rows, o columns) will result in m x o matrix.

- Unlike with addition, $A * B != B * A$, multiplication order matters.

<!-- unlike with addition, multiplication order matters. -->



- **Exercise** multiply these 2 matrices:  
  <div class="mathjax-align-left">
	$$
	A =
	\begin{bmatrix}
	2 & -3 \cr
	7 & 5 \cr
	\end{bmatrix}
	$$
	$$
	B =
	\begin{bmatrix}
	10 & -8 \cr
	12 & -2 \cr
	\end{bmatrix}
	$$
	
	<!-- $$ -->
	<!-- C = -->
	<!-- \begin{bmatrix} -->
	<!-- c_{11} & c_{12} \cr -->
	<!-- c_{21} & c_{22} \cr -->
	<!-- \end{bmatrix} -->
	<!-- = -->
	<!-- ? -->
	<!-- $$ -->
	</div> <!-- end align -->

<span class="expand">[Show the Answer]</span>  
<div class="description">
<div class="mathjax-align-left">
$$
c_{11} =
\begin{bmatrix}
2 & -3 \cr
\end{bmatrix}
*
\begin{bmatrix}
10 \cr
12 \cr
\end{bmatrix}
=
(2 * 10) + (-3 * 12)
=
20 - 36
=
-16
$$

$$
c_{12} =
\begin{bmatrix}
2 & -3 \cr
\end{bmatrix}
*
\begin{bmatrix}
-8 \cr
-2 \cr
\end{bmatrix}
=
(2 * -8) + (-3 * -2)
=
-16 + 6 
=
-10
$$

$$
c_{21} =
\begin{bmatrix}
7 & 5 \cr
\end{bmatrix}
*
\begin{bmatrix}
10 \cr
12 \cr
\end{bmatrix}
=
(7 * 10) + (5 * 12)
=
70 + 60
=
130
$$

$$
c_{22} =
\begin{bmatrix}
7 & 5 \cr
\end{bmatrix}
*
\begin{bmatrix}
-8 \cr
-2 \cr
\end{bmatrix}
=
(7 * -8) + (5 * -2)
=
-56 -10
=
-66
$$
$$
C =
\begin{bmatrix}
c_{11} & c_{12} \cr
c_{21} & c_{22} \cr
\end{bmatrix}
=
\begin{bmatrix}
-16 & -10 \cr
130 & -66 \cr
\end{bmatrix}
$$
</div> <!-- End align -->
</div> <!-- End description -->

<!-- End Exercise  -->

<span id="inversion">
### Inversion

Now that we know how to add, subtract and multiply matrices, it's time to learn about the inversion, which is analogous to division. To learn that you will first need to understand a couple of concepts.

When you multiply a number $x$ by $1$, you get the number $x$ itself. So here, $1$ is called the **identity of x.**

**Inverse of x** is a number which, when multiplied by $x$, produces identity.
For example ${1\over2}$ is an inverse of $2$, beause  ${1\over2} * 2 = 1$


When you divide a real number by $x$, it is the same as multiplying it by  ${1\over x}$

$$
3 / 2 = 3 * {1\over2}
$$

In other words, dividing by a number is the same as multiplying by the inverse of it.

So to "divide" by a matrix you need to multiply by it's inverse. 

<span id="identity-matrix">
### Identity matrix

Identity matrix ($I$), is a matrix such that:

$$
I*A = A
$$

Unlike other matrices, in the case of identity matrix the order of multiplication doesn't matter:

$$
I * A = A * I
$$

Identity matrix is analogous to 1 for real numbers.

Identity matrix for any 3 by 3 matrix looks like so:

$$
\begin{bmatrix}
1 & 0 & 0 \cr
0 & 1 & 0 \cr
0 & 0 & 1 \cr
\end{bmatrix}
$$

Identity matrix for any 4 by 4 matrix looks like so:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 \cr
0 & 1 & 0 & 0 \cr
0 & 0 & 1 & 0 \cr
0 & 0 & 0 & 1 \cr
\end{bmatrix}
$$

Etcetera, you get the pattern. Onces in a diagonal from top left to bottom right, and the rest are zeros. That works for any n x n matrix.

Here's an example for a general 2 x 2 matrix:

$$
\begin{bmatrix}
1 & 0 \cr
0 & 1 \cr
\end{bmatrix}
*
\begin{bmatrix}
a & b \cr
c & d \cr
\end{bmatrix}
=
\begin{bmatrix}
(1 * a + 0 * c) & (1 * b + 0 * d) \cr
(0 * a + 1 * c) & (0 * b + 1 * d) \cr
\end{bmatrix}
=
\begin{bmatrix}
a & b \cr
c & d \cr
\end{bmatrix}
$$

### Inverse matrix

Inverse matrix ($A^{-1}$), is a matrix such that:

$$
A^{-1}*A = I
$$

Calculating the inverse is a pretty long and messy process, it's easy enough to do for 2 x 2 matrix, but when dimensions get bigger, like 5 x 5, it becomes very hard for a human to do, so in practice you will end up using libraries that make computer to calculate it automatically for you.

Only square matrices (m x m) have inverses.

<span id="transpose">
### Transpose

Transpose is another type of matrix operations.

Transpose is essentially "flipping" the matrix across it's diagnoal. To compute a transpose you take the rows of a matrix, and turn them into columns.

$$
A =
\begin{bmatrix}
1 & 2 & 3 \cr
4 & 5 & 6 \cr
7 & 8 & 9 \cr
\end{bmatrix}
$$


$$
A^{T} =
\begin{bmatrix}
1 & 4 & 7 \cr
2 & 5 & 8 \cr
3 & 6 & 9 \cr
\end{bmatrix}
$$

The other way to put it is that to get an element i,j of a transposed matrix, you take the element j,i from an original matrix:

$$
A^{T}_{ij} = Aji
$$

<div id="article-info">
<hr/>
<!-- Author: <a href="http://rationalfiction.io/users/rayalez">Ray Alez</a> -->

<a style="float:right;"
href="https://github.com/raymestalez/dm/blob/master/content/math/matrices.md">Edit on GitHub</a>
</div>







<!--
## Matrix vector multiplication

Multiplying matrix by a vector is a little more elaborate.

When you multiply matrix by a vector you get a vector as a result.
To get the first element of a vector you to take elements from the first **row** of a matrix and multiply them with corresponding elements from the vector **column**, and then add the results together. Then you repeat that process for each of the rows to get each of the elements of a vector.

$$
\begin{bmatrix}
1 & 3 \cr
4 & 0 \cr
2 & 1
\end{bmatrix}
*
\begin{bmatrix}
1 \cr
5
\end{bmatrix}
=
\begin{bmatrix}
16 \cr
4 \cr
7 
\end{bmatrix}
$$

1 * 1 + 3 * 5 = 16  
4 * 1 + 0 * 5 = 4  
2 * 1 + 1 * 5 = 7  


$$
A * \vec{x} = \vec{y}
$$

To get $\vec{y}_{i}$, you multiply $A$'s $i^{th}$ row with elements of vector x, and add them up.

## Applying function to several features

Features:  
2104  
1416  
1534  
852

Function:

$$
h_\theta(x) = -40 + 0.25x
$$

Applying it to all the features at the same time:
$$
\begin{bmatrix}
1 & 2104 \cr
1 & 1416 \cr
1 & 1534 \cr
1 & 852
\end{bmatrix}
*
\begin{bmatrix}
-40 \cr
0.25
\end{bmatrix}
$$
The result of this multiplication will be a vector of $h_\theta()$ applied to all the features.

## Matrix matrix multiplication
$$
\begin{bmatrix}
1 & 3 & 2 \cr
4 & 0 & 1
\end{bmatrix}
*
\begin{bmatrix}
1 & 3 \cr
0 & 1 \cr
5 & 2
\end{bmatrix}
=
\begin{bmatrix}
11 & 10 \cr
9  &  14
\end{bmatrix}
$$

Number of columns in the first matrix must equal to number of rows in the 2nd matrix.

Ith column of mmatrix C is obtained by multiplying A with the ith column of vector B.

## Applying several hypotheses to features

[![Applying several hypotheses to features]
(/images/math/applying-hypotheses-with-matrix-multiplication.png)](/images/math/applying-hypotheses-with-matrix-multiplication.png)


## Properties of matrix multiplication

not commutative - order matters

order of multiplication matters too  
3x5x2  
(is associative)

### Identity matrix

When you multiply a matrix by it you get the same matrix.

$I_{n*n}$

AI = IA

$$
\begin{bmatrix}
1 & 0 & 0 \cr
0 & 1 & 0 \cr
0 & 0 & 1 
\end{bmatrix}
$$
-->
<!--
## Inverting matrices

1 = "Identity" for real numbers.

Inverse of a number - when you multiply a number by it you get 1.

Inverse of a matrix - when you multiply a matrix by it's inverse you get an identity matrix.

$A^{-1}$


A*A^-1=A^-1A=I

## Transposing matrices

[![matrix-transpose]
(/images/math/matrix-transpose.png)](/images/math/matrix-transpose.png)

$B_{ij} = A_{ji}$


## Inverting matrices
A^-1 = (1/|A|)*Adj(A)

You get |A| of 3x3 matrix by multiplying each of it's elements by it's corresponding cofactor(thing in the same place in Adj(A))(?)
### Determinant

a b
c d 

|a d| - c - b

### Adjegate
flip accross the diagonal
-->


<!-- <style> -->
<!-- img { -->
<!-- width: 100%; -->
<!-- padding: 40px; -->
<!-- height: 40px; -->
<!-- background: url("/theme/img/bg.png"); -->
<!-- background-size:100%; -->
<!-- } -->
<!-- </style> -->



<!-- Scripts -->
<!-- Expanding List -->
<script>
function prepareList() {
  $('body').find('li:has(ul)')
  	.click( function(event) {
  		if (this == event.target) {
  			$(this).toggleClass('expanded');
  			$(this).children('ul').toggle('medium');
  		}
  		return false;
  	})
  	.addClass('collapsed');
	//.children('ul').hide();
  };

function prepareExpand() {
  $('.expand').click( function(event) {
  		if (this == event.target) {
			$(this).parent().parent().find('.description').toggle('fast');
  		}
  		return false;
  	}).parent().parent().find('.description').hide();
  	//.addClass('collapsed');
	//.children('ul').hide();
};

$(document).ready( function() {
  //prepareList();
  prepareExpand();
  });
</script>

<style>
.expand {
color: gray;
cursor: pointer;
}
<!-- font-size: 12px;-->
</style>



<!-- Align mathjax to the left -->
<style>
.mathjax-align-left .MathJax_Display {
  text-align: left !important;
}
</style>
