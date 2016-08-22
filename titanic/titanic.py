import numpy as np
import pandas
from sklearn.preprocessing import LabelEncoder

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.cross_validation import cross_val_score

from sklearn.cross_validation import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline



# from keras.models import Sequential
# from keras.layers import Dense


# fix random seed for reproducibility
seed = 7
np.random.seed(seed)


# load the dataset
dataframe = pandas.read_csv("titanic.csv", header=None).fillna(0)
dataset = dataframe.values

# Selecting features.
# "1:" to select all the lines except the first one(that contains feature labels)
dataset = dataset[1:]

# (2,4,5) to select 2,4 and 5th columns(passenger class, gender, age)
X = dataset[:,(2,4,5)]

# Encode gender values as integers. Turn it from "male" and "female" to 1 and 0.
encoder = LabelEncoder()
encoder.fit(X[:,(1)])
encoded_Gender = encoder.transform(X[:,(1)])
X[:,(1)] = encoded_Gender
X = X

# Selecting labels. (survived or not)
Y = dataset[:,(1)]
# Y = Y.astype(np.float32)
Y = Y.astype(np.float32, copy=False)

print(X)
print(Y)


# baseline model
def create_baseline():
    # create model
    model = Sequential()
    model.add(Dense(3, input_dim=3, init='normal', activation='relu')) 
    model.add(Dense(1, init='normal', activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) 
    return model

model = create_baseline()

model.fit(X, Y, nb_epoch=150, batch_size=10)

# evaluate model with standardized dataset
# estimator = KerasClassifier(build_fn=create_baseline, nb_epoch=100, batch_size=5)
# kfold = StratifiedKFold(y=Y, n_folds=10, shuffle=True, random_state=seed)
# results = cross_val_score(estimator, X, Y, cv=kfold)
# print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
