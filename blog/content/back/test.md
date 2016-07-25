Title: Test article
Slug: test
Date: 2015-02-14
Status: draft


# Top header

## Sub-section header

Paragraph: 

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### Third-level header

Table of contents:

<div class="panel">
<ul>
	<li><a href="#"> Element one</a></li>
	<li><a href="#python-code"> Python code</a></li>
	<li><a href="#"> Three </a></li>
	<li><a href="#"> Four </a></li>
	<!-- <li><a href="#resources"> Other Resources</a></li>	 -->
</ul>
</div>


#### Fourth level

Quote:
> Whatever can be destroyed by the truth shall be!  
> - Somebody Wise.


List:

- a  
  Explanation  
  More explanation
- b
- c
- d

This is a [link](#).

Image:

![my image](/images/math/limits-01.svg)


## Expanding list

- **Permutation City** by Greg Egan  
	[[amazon](http://www.amazon.com/Permutation-City-Novel-Greg-Egan/dp/1597805394)]
	[[wiki](http://en.wikipedia.org/wiki/Permutation_City)] 
	<span class="expand">[Show Description]</span>  
	<div class="description">

	> This is simply the best science-fiction book ever written, the Grand Bull
	Moose Award Winner for really really good fiction.  It is, in short, my all-time favorite.
Can you imagine a book where the premise is that human beings have
been scanned into computers as virtual Copies?  "Darn it," you cry,
"now you've spoiled it for me!"  Oh, no, I haven't.  Can you imagine a
book where this concept is introduced on the first page?
That bit about Copies?  That's not the plot.  That's just the starting
assumption.  The surprises this book delivers are unbelievable.  It
shocked the living daylights out of me.
But I wouldn't want to spoil it for you.  So if you want to know more,
 read the book  
	> - Eliezer Yudkowsky
	</div>


<span id="python-code">
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

1
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

# Mathjax, sexy bg, no-frame
<div class="bg-no-frame">
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
</div>

# Image with sexy bg and aspect ration
<div class="wrapper">
<div class="bg">
<img src="/images/linear-regression/linear-regression-hypothesis.png" />
</div>
</div>



<div id="article-info">
<hr/>
<!-- Author: <a href="http://rationalfiction.io/users/rayalez">Ray Alez</a> -->

<a style="float:right;"
href="https://github.com/raymestalez/dm/blob/master/content/machine-learning/0005-deep-learning-resources.md">Edit on GitHub</a>
</div>






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

