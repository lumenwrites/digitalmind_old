Title: Multiclass Classification of Flower Species
Date: 2016-07-23
Slug: iris


The purpose of this project is to learn the basics of training an ANN on a simple example. I will use Keras, TensorFlow, and scikit-learn to train ANN that will classify flower species based on a few basic parameters.
  

## Iris Dataset

I will use a simple dataset that describes different species of flowers and their properties. There are 3 species of iris flowers(Iris setosa, Iris virginica and Iris versicolor), and the dataset contains examples describing 4 properties of each flower (the length and the width of it's sepals and petals), and the species it belongs to. The goal is to predict the species of a flower based on these parameters.

The data looks like this:
```
5.1,3.5,1.4,0.2,Iris-setosa
5.0,3.3,1.4,0.2,Iris-setosa
....
7.0,3.2,4.7,1.4,Iris-versicolor
6.4,3.2,4.5,1.5,Iris-versicolor
....
6.3,3.3,6.0,2.5,Iris-virginica
5.8,2.7,5.1,1.9,Iris-virginica
```

![Iris Scatterplot](https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Iris_dataset_scatterplot.svg/749px-Iris_dataset_scatterplot.svg.png)

To load the dataset download the csv file [here](https://github.com/raymestalez/dm/blob/master/flowers/iris.csv), and then load it like this:

```python
import pandas
import numpy
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils

# load dataset
dataframe = pandas.read_csv("iris.csv", header=None)
dataset = dataframe.values
X = dataset[:,0:4].astype(float)
Y = dataset[:,4]
```

'X' is a variable that contains the feautres that describe the lenghts of each of the flower parts:

```python
[[ 5.1  3.5  1.4  0.2]
 [ 4.9  3.   1.4  0.2]
 [ 4.7  3.2  1.3  0.2]
 ....
 [ 5.9  3.   5.1  1.8]]
```
and 'Y' contains the corresponding labels that describe the species of the flower:

```
['Iris-setosa'     'Iris-setosa'     ... 'Iris-setosa'
 ...
 'Iris-versicolor' 'Iris-versicolor' ... 'Iris-versicolor' 
 ...
 'Iris-virginica'  'Iris-virginica'  ... 'Iris-virginica']
```

Now to be able to use these labels in our network, we want to represent each of them as vector of 3 <!-- boolean --> values that looks like this:


```
Iris-setosa Iris-versicolor Iris-virginica
     1              0             0
     0              1             0 
     0              0             1
```

To do that, we will first use LabelEncoder(), that will turn the strings describing names of the plants into numerical values("Iris-setosa" will be represented by 0, "Iris-versicolor" by 1, and "Iris-virginica" by 2):


```python
#encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
```

So that our encoded list of labels (encoded_Y) now looks like this:

```python
[0 0 ... 0
 ...
 1 1 ... 1
 ...
 2 2 ... 2]
```

And then we will use np_utils.to_categorical():
```python
# convert integers to dummy variables (hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)
```

to convert it into a binary matrix that looks like this:

```python
[[ 1.  0.  0.] [ 1.  0.  0.] ... [ 1.  0.  0.]
 ...
 [ 0.  1.  0.] [ 0.  1.  0.] ... [ 0.  1.  0.]
 ...
 [ 0.  0.  1.] [ 0.  0.  1.] ... [ 0.  0.  1.]]
```

This process is called "one-hot encoding".

Now we have the data we can use to train our neural network.



## Defining the model

The next step is to define our model(the shape of the neural network). 


Initialize random seed
We initialize the random number generator with a specific value, so that we could reproduce the same results in the future:

```python
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
```

We want to create a simple fully connected neural network. It will have 4 inputs(one for each feature describing the property of the flower), one hidden layer with 4 neurons, and an output layer with 3 values(one for each class of the flower).

```python
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

# define baseline model
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(4, input_dim=4, init='normal', activation='relu'))
    model.add(Dense(3, init='normal', activation='sigmoid'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    return model
```

We create a Seuential model, add two layers to it, and specify their paramteters.
 
- Dense class creates a fully connected layer
- The first parameter describes the number of neurons in the layer
- `input_dim`(on the first layer) specifies the number of inputs
- `init` specifies the way we set the initial weights. ("normal" means that we want to intialize them to small random numbers.) <!-- from a Gaussian distribution. -->
- `activation` determines the activation function for every neuron.

After the model is defined, we can compile it.   <!-- ? --> To do that we need to set a few additional parameters required for training the network. Our goal is to find the best set of weights to make predictions for this problem.

- Loss function is used to determine how inaccurate the current prediction is and evaluate the set of weights.
- Optimizer is used to search through different weights for the network and minimize the error.

Finally, we pass our model to the KerasClassifier function, which allows us to wrap the model built with Keras to use in scikit learn:

```python
estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=200, batch_size=5, verbose=0)
```

We pass the model we have created to it's build_fn parameter, which specifies a name of a function used to create the model. We also specify the number of epochs and the batch size parameters, which will be automatically passed to the fit() function. 


## Evaluating the model using scikit
Now we want to train and evaluate our model on the training data.

```python
from sklearn.cross_validation import cross_val_score, KFold
from sklearn.pipeline import Pipeline

kfold = KFold(n=len(X), n_folds=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, dummy_y, cv=kfold)

print("Accuracy: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
```

We use KFold to define the model evaluation procedure,  <!-- ? --> and then use the cross_val_score function that evaluates our model(estimator), on our dataset(X and dummy_y), using the 10-fold cross validation procedure(kfold).

Finally, we have completed our training and can print the accuracy results.

You can see the [whole code on github](https://github.com/raymestalez/dm/blob/master/flowers/iris.py).

