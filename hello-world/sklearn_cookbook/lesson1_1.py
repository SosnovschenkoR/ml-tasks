import sklearn.datasets as d
import numpy as np

boston = d.load_boston()
print(boston.DESCR)

X,y = boston.data, boston.target
print(d.get_data_home())
d.make_biclusters
d.make_blobs
d.make_checkerboard
d.make_circles
d.make_classification
reg_data = d.make_regression()
complex_regdata = d.make_regression(1000, 10, 5, 2, 1.0)
print(complex_regdata[0].shape)

classification_set = d.make_classification(weights=[0.1])
np.bincount(classification_set[1])
print(classification_set[1])

blobs = d.make_blobs()

n_samples = 5;
n_features = 5;
n_target = 2;
n_informative = 5;
n_targets = 2;
bias = 0;
X = np.random.randn(n_samples, n_features)
ground_truth = np.zeros((n_samples, n_target))
ground_truth[:n_informative, :] = 100*np.random.rand(n_informative, n_targets)
y = np.dot(X, ground_truth) + bias