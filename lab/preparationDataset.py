# coding:utf-8

import sklearn.datasets as datasets


iris = datasets.load_iris()
X, y = iris.data, iris.target

print(X.isnull().sum())
