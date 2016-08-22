Title: Developing a simple Neural Network with Keras
Date: 2016-08-14
Slug: hello-world



This is a very simple introduction to deep learning. The goals of this tutorial is to develop a very simple ANN in Keras
This is the introduction to deep learning
simplest way to develop a neural network.


# Load Data

This is the dataset we will use

Here's how it looks like:

Download it here


# Define Model
# Compile Model
# Fit Model
# Evaluate Model
# Tie It All Together

# Complete code

```python
# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init= ' uniform ' , activation= ' relu ' ))
model.add(Dense(8, init= ' uniform ' , activation= ' relu ' ))
model.add(Dense(1, init= ' uniform ' , activation= ' sigmoid ' ))
# Compile model
model.compile(loss= ' binary_crossentropy ' , optimizer= ' adam ' , metrics=[ ' accuracy ' ])
# Fit the model
model.fit(X, Y, nb_epoch=150, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
```
