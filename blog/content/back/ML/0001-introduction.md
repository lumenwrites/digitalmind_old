Title: Introduction to Machine Learning
Slug: introduction-to-machine-learning
Date: 2014-12-22 01:00
Status: Draft

This article is a general overview of Machine Learning and the surrounding fields.

## What is Machine Learning?

> The field of study that gives computers the ability to **learn** without being explicitly programmed.  
- Arthur Samuel.

Machine Learbing is a field that studies algorithms that can learn from data. These algorithms take a dataset as an input, and build a **model** based on it. And then they make predictions or decisions based on that model, as opposed to following explicit instructions, like the usual programs do.

Often it is impossible to create programms just by writing the code, becaue that would take too long, or you just don't know how to do that.
For example you can not write millions of programs for every one of amazon users that would suggest books this particular person would like, because it would just take too much effort, and you couldn't program a quadcopter to do some complex trick while it's flying, because you don't know how to express the commands it would need as a series of if-else statements.

That is where ML comes in. With ML you can analyze a lot of data, find patterns in it, and use these patterns to allow computer to "learn" to perform certain tasks.

Especially now, as more data becomes available, you can solve more and more complex problems by using ML, and now ML is used in [a lot of fields](/post/practical-applications-of-machine-learning). Availability of Big Data made machine learning much more valuavle.

So Machine Learning analyzes the data, finds patterns in it, extracts knowledge from it, and uses it to predicts the output.

It also allows us to discover new relationships and connections in the large sets of data, it allows us to "predict the future", and it allows computers to program themselves.

## Machine Learning process

<div class="mermaid">
graph LR;
	UR(Unknown Relatioinship <br/>Target Function)-->D(Data);
	D --> LA(Learning Algorithm <br/><br/> Model > Evaluate > Results > <br/> > Optimize > New Model > Repeat);
	M(Models) --> LA;
	LA --> FM(Final Model);
</div>


ML process begins with data(also called "training examples"), data contains examples of how some system operates, inputs and outputs. This data was produced by some process(also called "target function"), unknown to us, some pattern which we are trying to find out.

We create models(representations) that present mappings from inputs to outputs, possible functions that produce this model. And then we will use our learning algorithm to find the final model(hypothesis) that represents the target function as close as possible. The best model will be the one that best explains the underlying pattern of data, that is most accurate at mapping inputs to the outputs.

Learning algorithm is usuall y an iterative process, that takes a model evaluates it to find out how good the model is(how much errors doe it have), uses these results to  optimize the model to get a new one, that produces better results. It repeats until we get a final model that is good enough for our purposes.

This means that for Machine Learning it requires data with a predictable underlying pattern, usually it works best when this pattern is complex, otherwise we could use simpler algorithms.

## Components of machine learning

These are the 3 main components of machine learning:

- Representation  
  This is how we mathimatically/algorithmically represent our model.  
  Examples:  
	  - K-Nearest Neighbor
	  - Decision Trees
	  - Naive Bayes
	  - Linear Regression
	  - Neural Networks
	  - Support Vector Machines 
- Evaluation  n
	This is how we find the errors in our model and decide how good it is.  
	Examples:  
    - Accuracy
    - Error Rate
    - Squared Error
    - Info Gain
    - Cost
    - Margin
- Optimization
  It is a way to search among many models and choose the one that's best.  
  Examples:  
	  - Greedy Search
	  - Gradient Descent
	  - Newton's Method
	  - Linear Programming
	  - Quadratic Programming
	  - Evolutionary Computation

<!--
### Relationship between deep learning and other fields
[![ai-ml-dl](/images/deep-learning/ai-ml-dl.png)](/images/deep-learning/ai-ml-dl.png)

So Deep Learning(DL) is a subfield of Machine Learning(ML) which is a subfield Artificial Intelligence which is a subfield Computer Science.

## Deep Learning
<img src="/images/deep-learning/artificial_neural_network.png"
style="width: 300px; float: right;"/>

> "Deep learning" is the new big trend in Machine Learning. It promises general, powerful, and fast machine learning, moving us one step closer to AI.

Deep Learning is a part of Machine Learning that focuses on creating multilayer Artificial Neural Networks(ANN). "Deep" means that the algorithm has several hidden layers of "neurons".

ANNs are inspired by the theories of how biologial brain works, which in itself is awesome, and turns out that DL algorithms are extremely good at performing a lot of tasks, and in the past years they are making huge improvements upon other ML algorithms.

DL allows to find patterns in unlabeled data, for example it can look at a lot of youtube videos, extract concepts from them, and to learn to recognize a cat, without initially knowing what it is.

In the following years DL will be a huge driver of innovation, because it can be applied almost everywhere, and it can change the way we do things dramatically.

At this point a lot of [resources](/post/deep-learning-resources/) are available on the subject, so it's a grat time to get into this awesome field.
-->

### Related Posts:
- [Key Concepts in Machine Learning](/post/machine-learning-key-concepts)

