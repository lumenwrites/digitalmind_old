Title: List of the key terms and concepts of ML
Slug: machine-learning-key-concepts
Date: 2014-12-22 04:00

This is a list of the key terms and concepts in Machine Learning.

### Model
Our goal in ML is to create a good model. You take the input data and try to find underlying patterns in it, and the model is the output of your learning algorithms, it represents the patterns in data that you could find.

<!-- TODO what is the difference between the model and a Target Variable/Function? -->

### Dataset
When you start with a machine learning problem the first thing you need is data.
All the data you have is your dataset.

Imagine it like a table with rows and columns.

Dataset contains **instances**, also called **vectors**, or **training examples**.
These are the specific entries in your data, *rows* of your table.

And **features** (also called **attributes** of the instances) are the *columns* of your table.

What you do is you split your data into 2 parts: a training set and a test set.  
**Training set** you will use as an input, you will run learning algorithms on it to train your model.  
**Test set** is the part of your dataset that you put aside, so that when your model is created you can test it and make sure that it predicts things correctly.


## Types of machine learning

### Supervised Learning

The goal of supervised learning is prediction.  
You are given a set of labeled data, that contains inputs and outputs, so you know what you are looking for, what the right answers are, and you are trying to understand the mapping between inputs and outputs.

Process:  

![supervised learning](/images/machine-learning-intro/supervised-learning.png)



Model here is a mapping between inputs and outputs.  
You run learning algorithms on the data to find a model, and once we have that model, we can feed it new inputs, and it will correctly predict new outputs. So now we can make new predictions on data that wasn't in the dataset.

Types:

### Regression
The output is continuous, it can be any real number.  

Example: predicting house prices based on house size.


###  Classification
The output is discrete. Yes/no,  or red/blue/green. You are taking the input and trying to classify it into groups.

Example: Classify emails as spam or not spam.

<!-- Example:  
Housing prices.
price/size in feet.
fit a straight line through the data. or a quadratic/polynomial functio
prive/size in feet - graph in matplotlib!!
(regression - fitting a line) -->


## Unsupervised Learning

In unsupervised learning you don't know what you're looking for, you're just trying to find patterns in the unlabeled data, and group this data according to it.

Process:  
![unsupervised learning clustering](/images/machine-learning-intro/unsupervised-learning-clustering.png)

Types: Clustering and Association.

Example: Figure out types of items that are frequently bought together.

## Overfitting. Approximation vs Generalization
**Approximation** is how well your model fits into the training data, **generalization** is how well your model can make predictions about new data that isn't in the training set.

There is a fundamental tradeoff in machine learning, between how well the training data can be approximated, and how well model generalizes to new data.

<!-- Example: [Graph. Linear function vs parabola] -->

**Overfitting** is too much approximation with bad generalization.
It happens  when the function we've predicted fits great with a training set, but can't generalize and predict the actual new inpits.

<img style="width:320px; float:right;" src="/images/machine-learning-intro/overfitting.jpg" />

For example in the graph to the right the green line represents the actual underlying function that created the data, and blue line represents the model made by a machine learning algorithm that suffers from overfitting. 

So it is always important to remember that the goal is not to fit the training data, but to fit the underlying model that created the data, and make the best predictions on new examples.


<!--
### Classification
//clustering
Breast cancer malignant/benign.
Estimate probability of that.

Features/attributes.

Examples

## Unsupervised learning
Unlabeled data, without knowing what data means, find the patterns.
Find some structure in data.
CLustering.
Example - google news.

Group peoply by genes. find structure in genes.
social vetwork analysis
market segmentation
astronomical data analysis

coctail party problem.

- definition
- examples

## Other
Reinforcement learning, recommender systems

## Cross-validation
## Generalization
## Dimensionality
the curse of dimensionality

-->


