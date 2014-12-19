Title: Introduction to Linear Algebra: Vectors
Date: 2014-12-18 20:30
Slug: vectors
Category: math
Status: draft

Vector is something that has both magnitude and direction.

For example, wind has both a direction(North, South-West, etc) and a magnitude (10 km/hour) and could be represented as a vector (10 km/hour South-West).

In algebra vectors can represent many things, often vectors represent points in a coordinate system.

You can write vectors like this:
$$\vec{v}_1 = (4,4)$$

or like this:

$$
\vec{v}_2 =
\begin{bmatrix}
4 \\ 1
\end{bmatrix}
$$

And if you plot them, it would look like so:
{% notebook vectors/vectors.ipynb %}


## Vector addition
## Scalar multiplication
## Linear combination




<style>
div.input {
    display: none;
}
</style>


<!--
Python code:

	:::python
	import numpy as np
	import matplotlib.pyplot as plt  
	import math

	soa =np.array( [ [0,0,4,4], [0,0,4,1],]) 
	X,Y,U,V = zip(*soa)
	plt.figure()
	ax = plt.gca()
	ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)
	ax.set_xlim([-1,8])
	ax.set_ylim([-1,8])
	plt.draw()
	plt.show()

Another graph notebook:
{% notebook vectors/another-graph.ipynb %}

-->
