Title: Getting Started with Deep Learning - Resources
Slug: deep-learning-resources
Date: 2014-12-22 05:00

This post lists a collection of the best resources for getting into Machine Learning (specifically - Deep Learning for Computer Vision), and the roadmap for studying it.

## Resources

### Basic Math

#### Calculus

- [Khan Academy Calculus videos](http://www.youtube.com/playlist?list=PL19E79A0638C8D449)  

- [Coursera Calculus course](https://www.coursera.org/course/m2o2c2)

- MIT lectures on [Multivariable Calculus](http://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/index.htm)

#### Linear Algebra

- [Khan Academy Linear Algebra videos](http://www.youtube.com/playlist?list=PLFD0EB975BA0CC1E0)

- [MIT linear algebra videos](http://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/) by Gilbert Strang

- [Coding the Matrix](https://cs.brown.edu/video/channels/coding-matrix-fall-2014/?page=2) - Brown University course on Linear Algebra for CS. 

#### Probability and statistics   

- Khan Academy [Probability](http://www.youtube.com/playlist?list=PLC58778F28211FA19) & [Statistics](http://www.youtube.com/playlist?list=PL1328115D3D8A2566) videos  

- [edx probability course](https://www.edx.org/course/introduction-probability-science-mitx-6-041x#.VJfS2LQAKc)

### General Computer Science 

- Algorithms coursera course [part 1](https://www.coursera.org/course/algo) and [part 2](https://www.coursera.org/course/algo2)

- MIT course [Structure and Interpretation of Computer Programs](https://www.youtube.com/watch?v=2Op3QLzMgSY&list=PLE18841CABEA24090#t=253)
(based on [SICP book](http://www.amazon.com/Structure-Interpretation-Computer-Programs-Engineering/dp/0262510871))

### Artificial Intelligence introduction

- Book "[Artificial Intelligence: A Modern Approach (AIMA)](http://www.amazon.com/Artificial-Intelligence-Modern-Approach-Edition/dp/0136042597)"  

- [Artificial Intelligence course](https://www.youtube.com/channel/UCshmLD2MsyqAKBx8ctivb5Q/videos) from UC Berkeley(CS 188)  

### General Machine Learning introduction

- Andrew Ng [Machine Learning course](https://www.coursera.org/course/ml) on Coursera.  
  And his [course on Deep learning ](http://openclassroom.stanford.edu/MainFolder/CoursePage.php?course=ufldl)
  And here's is the link to the [full course](http://see.stanford.edu/see/lecturelist.aspx?coll=348ca38a-3a6d-4052-937d-cb017338d7b1) Ng taught at Stanford that his coursera course is based upon.

- [Pedro Domingos ML course](https://class.coursera.org/machlearning-001/lecture/preview) 

- [Udacity Course on ML](https://www.udacity.com/course/cs271) by Perer Norvig

-  Book "[Programming Collective Intelligence](http://www.amazon.com/Programming-Collective-Intelligence-Building-Applications/dp/0596529325)" 

- TutsPlus course "[Machine Learning Distilled](http://code.tutsplus.com/courses/machine-learning-distilled)"


### Deep Learning Basics

- Geoffrey Hinton's coursera course "[Neural Networks for Machine Learning](https://class.coursera.org/neuralnets-2012-001/lecture)"
  
- MIT Book on [Deep Learning](http://www.iro.umontreal.ca/~bengioy/dlbook/)
 
- [UFLDL tutorial by Stanford](http://deeplearning.stanford.edu/wiki/index.php/UFLDL_Tutorial) (alternative [link](http://deeplearning.stanford.edu/tutorial/))

- [deeplearning.net tutorials](http://deeplearning.net/tutorial/)
  

### Other

- [Metacademy](http://www.metacademy.org) - "package manager" for Machine Learning knowledge

- [kaggle](http://www.kaggle.com/) - Machine Learning competitions

- [mathematicalmonk](http://www.youtube.com/playlist?list=PLD0F06AA0D2E8FFBA) - Machine Learning youtube tutorials

#### More DL and ML courses
- NYU Course on [Deep Learning](http://techtalks.tv/deep_learning_nyu_spring_2014/)

- [Anothre course on ML](http://www.cs.cmu.edu/~tom/10701_sp11/lectures.shtml) taught at Carnegie Mellon University by Tom Mitchell.

#### Books about Deep Learning
- Book "[Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com)" by Michael Nielsen

- Book Neural "[Networks and Learning Machines](http://www.amazon.com/Neural-Networks-Learning-Machines-Edition/dp/0131471392)" by Simon O. Haykin

- [deeplearning.net reading list](http://deeplearning.net/reading-list/)

#### Books on "how mind works"
- Jeff Hawkins - [On Intelligence](http://www.amazon.com/On-Intelligence-Jeff-Hawkins/dp/0805078533>) ([Audiobook](http://www.audible.com/pd/Science-Technology/On-Intelligence-Audiobook/B002V8LK))

- Ray Kurzweil - [How to Create a Mind](http://www.amazon.com/How-Create-Mind-Thought-Revealed/dp/0143124048/) ([Audiobook](http://www.audible.com/pd/Science-Technology/How-to-Create-a-Mind-Audiobook/B009S7OKJ))





<div style="clear: both;"></div>



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
 
  $(document).ready( function() {
      prepareList();
  });
</script>

<style>
.collapsed {
	cursor: pointer;
	<!-- content:' ►';  -->

	<!-- background: url({{ site.baseurl }}/images/small_right_arrow.gif) no-repeat left top; -->
	<!-- padding: 3px 0px 3px 20px; -->
	<!-- list-style: none; -->
	}

.collapsed {
cursor: pointer;
	<!-- content:' ►';  -->
	<!-- background: url({{ site.baseurl }}/images/small_right_arrow.gif) no-repeat left top;p -->
	<!-- padding: 3px 0px 3px 20px; -->
	<!-- list-style: none; -->
	}

.entry img {
float:left;
}
<!-- max-width: 400px;
max-height: 400px; -->


</style>
<!--
list-style-image: url({{ site.baseurl }}/images/small_right_arrow.gif);
 -->
