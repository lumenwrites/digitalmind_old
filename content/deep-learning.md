Title: Deep Learning - Getting Started
Slug: deep-learning
Date: 2014-12-19

This post lists a collection of the best resources for getting into Machine Learning (specifically - Deep Learning for Computer Vision), and the roadmap for studying it.


## Resources

#### General Machine Learning introduction

- Andrew Ng [Machine Learning course](https://www.coursera.org/course/ml) on Coursera.  
  And his [course on Deep learning ](http://openclassroom.stanford.edu/MainFolder/CoursePage.php?course=ufldl)
  And here's is the link to the [full course](http://see.stanford.edu/see/lecturelist.aspx?coll=348ca38a-3a6d-4052-937d-cb017338d7b1) Ng taught at Stanford that his coursera course is based upon.

- [Pedro Domingos ML course](https://class.coursera.org/machlearning-001/lecture/preview) 

-  Book "[Programming Collective Intelligence](http://www.amazon.com/Programming-Collective-Intelligence-Building-Applications/dp/0596529325)" 

- TutsPlus course "[Machine Learning Distilled](http://code.tutsplus.com/courses/machine-learning-distilled)"


#### Deep Learning Basics

- Geoffrey Hinton's coursera course "[Neural Networks for Machine Learning](https://class.coursera.org/neuralnets-2012-001/lecture)"
  
- MIT Book on [Deep Learning](http://www.iro.umontreal.ca/~bengioy/dlbook/)
 
- [UFLDL tutorial by Stanford](http://deeplearning.stanford.edu/wiki/index.php/UFLDL_Tutorial) (alternative [link](http://deeplearning.stanford.edu/tutorial/))

- [deeplearning.net tutorials](http://deeplearning.net/tutorial/)
  

#### Other

- NYU Course on [Deep Learning](http://techtalks.tv/deep_learning_nyu_spring_2014/)

<!-- - [Anothre course on ML](http://www.cs.cmu.edu/~tom/10701_sp11/lectures.shtml) taught at Carnegie Mellon University by Tom Mitchell. -->

- Book "[Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com)" by Michael Nielsen

- Book Neural "[Networks and Learning Machines](http://www.amazon.com/Neural-Networks-Learning-Machines-Edition/dp/0131471392)" by Simon O. Haykin

- [deeplearning.net reading list](http://deeplearning.net/reading-list/)

- [Metacademy](http://www.metacademy.org)

- [Khan Academy math videos](http://www.youtube.com/user/khanacademy/playlists).

- [Coding the Matrix](https://cs.brown.edu/video/channels/coding-matrix-fall-2014/?page=2) - Brown University course on Linear Algebra for CS. 

- [kaggle - ML competitions](http://www.kaggle.com/)
<!--
## Topics

- General overview, terms, into, background.
    - What is ML? Applications of ML
        - Types of Learning: supervised/unsupervised learning
    - classification/regression(difference)
- ML Algorithms
    - Supervised Learning
      - Linear Regression with one variable
          - Model Representation
          - Cost function
          - Gradient Descent
      - Linear Regression with multiple variables
          - Gradient descent for multiple vectors
          - Features and polynomial regression
          - Normal Equation
      - Logistic Reression
      - k-Nearest Neighbor
      - Decision Tree
      - Naive Bayesian Classifiers

      - Support Vector Machines
      - Random Forests
    - Unsupervised Learning
      - k-Means Clustering
      - Hierarchical Clustering
      - Self-Organizing Maps
      - Apriori Association
- Deep Learning
  - Perceptron
	- Linear Regression
  - Gradient Descent
  - Stochastic Gradient descent
  - Multilayer Perceptrons
  - Backpropogation
  - Hidden Layer Representations

  - Neural Networks: Representation and learning
      - Neurons
      - Model representation
      - Cost function
      - Backpropogation algorithm
      - Gradient checking
      - Random Initialization

  - Perceptron
    
  - Artificial Neural Networks Representation
  - General Regression Neural Networks
  - Feed-Forward Neural Networks
- Other/General ML
  - ML Systems design
    - Error  Analysis
  - Dimensionality Reduction
  - Anomaly Detection
  - Recommender Systems
-->


<!-- To Sort, other topics
- Neural networks:
  - Types of neurons,
  - Learning rules for binary,
  - linear and logistic neurons,
  - FeedForward Neural Networks (FFNN)
  - Backpropagation (BP),
  - BP with weight constraints.
  - Recurrent Neural Networks (RNN),
  - FFNN interpretation for RNN,
  - BP through time,
  - Exploding/Vanishing gradients.
- Energy-based models:
  - Hopfield Nets (HN),
  - Learning & unlearning in HN,
  - HN with hidden units,
  - Simulated annealing,
  - Boltzmann machines (BM),
  - BM Learning algorithm.
- Deep Neural Networks:
  - Deep Boltzmann Machines (DBM),
  - Restricted Boltzmann Machines (RBM),
  - Contrastive Divergence and variants (PCD, CD_k),
  - Stacked RBMs for pre-training,
  - Discriminative finetuning using BP.
- Nonlinear Dimensionality Reduction:
  - Autoencoders (AE),
  - AE for document retrieval/visualization,
  - AE for semantic hashing
- Other:
  - Minibatch gradient descent,
  - Momentum method,
  - Adaptive Learning rates,
  - Limiting size of weights,
  - Weight decay,
  - Early stopping,
  - Noise as regularizer,
  - Dropouts,
  - Bagging/Averaging and Boosting,
  - Bias-variance tradeoff,
  - Implementation on GPGPUs. 
-->

## Roadmap 

First of all - the general overview of all the major topics, and the order in which to study them
(made based on the overview of the Deep Learning from [metacademy](http://metacademy.org/roadmaps/rgrosse/deep_learning))

[![deep learning roadmap](/images/deep-learning/deep-learning-roadmap.png)](/images/deep-learning/deep-learning-roadmap.png)

Now - the list of resources and projects, in order of learning:

### Basic Math
- [Calculus](http://www.youtube.com/playlist?list=PL19E79A0638C8D449)
- [Linear Algebra](http://www.youtube.com/playlist?list=PLFD0EB975BA0CC1E0)
- [Probability](http://www.youtube.com/playlist?list=PLC58778F28211FA19) & [Statistics](http://www.youtube.com/playlist?list=PL1328115D3D8A2566)

###  Andrew Ng course
Andrew Ng [Machine Learning course](https://www.coursera.org/course/ml),  
supplemented with his [course on Deep learning ](http://openclassroom.stanford.edu/MainFolder/CoursePage.php?course=ufldl), and Neural Networks explanation from [Pedro Domingos ML course](https://class.coursera.org/machlearning-001/lecture/preview)(for things that are unclear).

Projects:

- Linear Regression
- Logistic Regression
- Feed Forward Neural Network
- Backpropagation

## Neural Networks for Machine Learning
Geoffrey Hinton's coursera course "[Neural Networks for Machine Learning](https://class.coursera.org/neuralnets-2012-001/lecture)", supplemented with  MIT Book on [Deep Learning](http://www.iro.umontreal.ca/~bengioy/dlbook/) and [UFLDL tutorial by Stanford](http://deeplearning.stanford.edu/wiki/index.php/UFLDL_Tutorial) (alternative [link](http://deeplearning.stanford.edu/tutorial/))

Projects:

- Use neural network to recognize hand-written digits from MNIST database.
- Use Restricted Boltzmann machines to create Deep Belief nets.

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
