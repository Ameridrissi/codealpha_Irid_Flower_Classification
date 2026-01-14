import pickle
from sklearn import datasets
from sklearn import datasets

iris=datasets.load_iris()


load_model = pickle.load(open('modeltree', 'rb'))
prediction= load_model.predict([[7.1, 7.5, 6.4,4.2]])

print (iris.target_names[prediction])