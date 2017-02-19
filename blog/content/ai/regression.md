Title: Regression Keras
Date: 2016-08-22
Status: Draft

The goal of this project is to learn how to use Keras to train ANN for a regression problem.

# Dataset

The dataset we will use for this problem is

# Loading dataset

# Creating baseline ANN

Full code:

```python
# Regression Example With Boston Dataset: Baseline
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# load dataset
dataframe = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:13]
Y = dataset[:,13]

# define base model
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(13, input_dim=13, init='normal', activation='relu')) model.add(Dense(1, init='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# evaluate model with standardized dataset
estimator = KerasRegressor(build_fn=baseline_model, nb_epoch=100, batch_size=5, verbose=0)
kfold = KFold(n=len(X), n_folds=10, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
print("Baseline: %.2f (%.2f) MSE" % (results.mean(), results.std()))

```


# Improving perfomance by standardizing the dataset

Next we will modify our data to improve the perfomance

# Tuning the network topology

Now we will try to make it wider

Now we will try to make it deeper

And conpare the results

# Conclusion

I have achieved an accuracy rate of x%.
You can experiment with this other housing prices dataset.

Final code:
