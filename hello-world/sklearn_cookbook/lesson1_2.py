from sklearn import preprocessing
import numpy as np
import sklearn.datasets as d

boston = d.load_boston()
X, y = boston.data, boston.target
X[:, :3].mean(axis=0)  # mean of the first 3 features
# array([  3.59376071,  11.36363636,  11.13677866])
X[:, :3].std(axis=0)
# array([  8.58828355,  23.29939569,   6.85357058])
X_2 = preprocessing.scale(X[:, :3])
X_2.mean(axis=0)
# array([  6.34099712e-17,  -6.34319123e-16,  -2.68291099e-15])
X_2.std(axis=0)