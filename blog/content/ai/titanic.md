Title: Using ANN for Binary Classification
Date: 2016-08-12
Slug: deep-learning-binary-classification
Status: draft

The goal of this project is to train an ANN that will be able to perform binary classification.

For this example we will use a [Titanic passengers dataset](). It includes list of Titanic passengers and some information about them. We will try to predict whether or not the passenger will survive the catastrophe based on his class, age, and gender. 



# Initial setup

First let's import the tools and libraries that we'll need:

```python
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
```

and initialize the random seed so that we could consistently reproduce our results:

```python
# Initialzie random seed for reproducibility
seed = 7
numpy.random.seed(seed)
```

.

# Loading the dataset
We begin by using pandas to load the dataset:

```python
# load dataset
dataframe = pandas.read_csv("titanic.csv", header=None)
dataset = dataframe.values
```

Next we need to split the dataset into inputs(features) and outputs(labels). Inputs will be the columns x, y, and z, that represent passenger's class, gender, and age respectively. Outputs consit of one value representing whether or not the passenger has survived. 

```python
# split into input (X) and output (Y) variables
X = dataset[:,0:60].astype(float)
Y = dataset[:,60]
```

Because [] is string, we want to encode it as integer

```python
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
```



# building a model
Now we build our model.

```python
# baseline model
def create_baseline():
    # create model
    model = Sequential()
    model.add(Dense(60, input_dim=60, init='normal', activation='relu')) 
    model.add(Dense(1, init='normal', activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) 
    return model
```

We create a model with 4 inputs(one for each parameter) and two layers.


# Evaluating a model

Next we can evaluate our model:
    
```python
# evaluate model with standardized dataset
estimator = KerasClassifier(build_fn=create_baseline, nb_epoch=100, batch_size=5, verbose=0)
kfold = StratifiedKFold(y=encoded_Y, n_folds=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, encoded_Y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
```

We pass our model to the KerasClassifier, with other parameters such as nb_epoch and batch_size.

Then we use StratifiedKFold function to  train it and estimate it's perfomance.


This basic model returns the result of 81%

# Improving the model with data preparation
scaling the inputs

# Tuning network topology
Nany things to tune: initial weights, activation function, optimization procedure, etc. Experiment with making it smaller and larger.

Reduce hidden layer by half, 60>30
because This will put pressure on the network during training to pick out the most important structure in the input data to model.

Add one layer
because network is given the opportunity to model all input variables before being bottlenecked and forced to halve the representational capacity, much like we did in the experiment above with the smaller network. Instead of squeezing the representation of the inputs themselves, we have an additional hidden layer to aid in the process.


# Summary
With these improvements, our ann now has 86% accuracy
You can find the code [here]. 
