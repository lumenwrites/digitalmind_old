Title: Multiclass Classification of Flower Species
Date: 2016-07-23
Slug: iris
Status: draft


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

The next step is to define our model(shape of the neural network). First let's import the tools that we're going to use:

```python
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
```



Initialize random seed
We initialize the random number generator with a specific value, so that we could reproduce the same results in the future:

```python
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
```



```python
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




```python
from sklearn.cross_validation import cross_val_score, KFold
from sklearn.pipeline import Pipeline
```






## Evaluating our model

```python
estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=200, batch_size=5, verbose=0)
kfold = KFold(n=len(X), n_folds=10, shuffle=True, random_state=seed)
```

## Training, complete

```python
results = cross_val_score(estimator, X, dummy_y, cv=kfold)
print("Accuracy: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
```

Completed the training, accuracy is this.
You can see the [whole code on github](https://github.com/raymestalez/dm/blob/master/flowers/iris.py).
