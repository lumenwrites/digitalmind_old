Title: Multiclass Classification of Flower Species
Date: 2016-07-23
Slug: iris
Status: draft


The purpose of this project is to learn the basics of training an ANN on a simple example. I will use Keras, TensorFlow, and scikit-learn to train ANN that will classify flower species based on a few basic parameters.
  

## Iris Dataset

I will use a simple dataset that describes different species of flowers and their properties. There are 3 species of iris flowers(Iris setosa, Iris virginica and Iris versicolor), and the dataset contains examples describing 4 properties of each flower (the length and the width of the sepals and petals), and the species it belongs to. The goal is to predict the species of a flower based on these parameters.

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

# load dataset
dataframe = pandas.read_csv("iris.csv", header=None)
dataset = dataframe.values
X = dataset[:,0:4].astype(float)
Y = dataset[:,4]
```


## Importing tools
Let's import the tools that we're going to use:

```python
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.cross_validation import cross_val_score, KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
```

We will use numpy to ...,  keras to ..., and scikitlearn to ...


## Initialize seed, encode output variable.

```python
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
```


#encode class values as integers 
```python
#encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# convert integers to dummy variables (hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)
```

## Defining our model

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
