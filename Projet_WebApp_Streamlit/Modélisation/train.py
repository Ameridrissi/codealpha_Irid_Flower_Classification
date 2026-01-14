import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
import pickle

iris=datasets.load_iris()
model_tree=DecisionTreeClassifier()
model_tree.fit(iris.data,iris.target)


pickle.dump(model_tree, open('modeltree', 'wb'))
