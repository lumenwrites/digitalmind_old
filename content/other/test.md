Title: Test article
Slug: test
Date: 2015-02-14
Status: draft


# Top header

Lorem ipsum paragraph

## Sub-section header

### Smaller thing

#### Yet smaller

> Quottidy quote!
> Whatever can be destroyed by the truth shall be!


List:

- a  
  Explainidy stuff!!  
  More stuff
- b
- c
- d

# Python code

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

# Ipython notebook 

{% notebook vectors/vectors.ipynb %}
# Mathjax


You can write vectors like this:
$$\vec{v}_1 = (4,4)$$

or like this:

$$
\vec{v}_2 =
\begin{bmatrix}
4 \\ 1
\end{bmatrix}
$$


$$
\begin{bmatrix}
1 & 0 & 0 \cr
0 & 1 & 0 \cr
0 & 0 & 1 
\end{bmatrix}
$$
