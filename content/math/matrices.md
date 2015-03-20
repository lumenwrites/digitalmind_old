Title: Matrices and vectors
Date: 2015-02-13
Slug: matrices
Category: math
Status: draft

This article is about the basics of matrices and operations on them.

Matrices are a convention to represent data, they are very convenient for solving all kinds of problems. A lot of these problems are often encountered in Machine Learning, and that is why it is so useful.

Matrix is a rectangular array of numbers within square brackets.

A matrix looks like that:

$$
\begin{bmatrix}
1 & 2 \cr
3 & 4 \cr
5 & 6
\end{bmatrix}
$$


This matrix has 3 rows and 2 columns, therefore it is 3x2 ("3 by 2") matrix.
This is called a dimension of matrix.

$ A_{ij} $ is an element(entry) of a matrix, in the $ i^{th} $ row, $ j^{th} $ column.

For example $A_{21}$ is 3.

## Vector

Vector is a matrix with only one column(nx1 matrix).

This is a 3-dimensional vector:

$$
\vec{y} =
\begin{bmatrix}
23 \cr
31 \cr
42
\end{bmatrix}
$$


$ \vec{y}_i $ is an $ i^{th} $ element of a vector.

For example $ \vec{y}_2 = 31 $.

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


By convention, capital letters usually refer to matrices, and lowercase letters are used for vectors.


## Matrix addition

To add matrices you just add up the corresponding elements one at a time.

$$
\begin{bmatrix}
1 & 0 \cr
2 & 5 \cr
3 & 1
\end{bmatrix}
+
\begin{bmatrix}
4 & 0.5 \cr
2 & 5 \cr
0 & 1 \cr
\end{bmatrix}
=
\begin{bmatrix}
5 & 0.5 \cr
4 & 10 \cr
3 & 2 \cr
\end{bmatrix}
$$

You can only add matrices of the same dimension.

## Scalar multiplication and division

To multiply a matrix by a number(scalar) you multiply each of it's elements by this number.

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


<!-- matrix -->
$$ \matrix{1&2\cr
         3&4} $$
