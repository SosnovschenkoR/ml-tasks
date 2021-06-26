from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
#print (iris)
print (iris.keys())
features = iris.data
print (features)
labels = iris.target
print (labels)
print (iris.target_names)
print (iris.feature_names)

for i in range(len(iris.target)):
    print("Example %d: label %s, features %s %s" % (i, iris.target[i], iris.data[i],
                                                    iris.target_names[iris.target[i]]))

# features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# labels = [0, 0, 1, 1]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, labels)
# print(clf.predict([[150, 0]]))