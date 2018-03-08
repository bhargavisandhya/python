from scipy import sparse
from sklearn import datasets, metrics
from sklearn import svm
from sklearn.datasets import load_boston,load_digits
from sklearn.cross_validation import train_test_split
#Choose one of the dataset using the datasets features in the scikit-learn


import numpy as np
#import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning)

D = 1.0
#getting the data and response of the dataset
#choosing
di=load_digits() #load dataset
d=di.data
p=di.target
#According to your dataset, split the data to 20% testing data, 80% training data(you can also use any other number)
d_train, d_test, p_train, p_test=train_test_split(d, p, test_size=0.2)
#Apply SVC with Linear kernel
moddde = svm.SVC(kernel='linear')
moddde.fit(d_train, p_train)
p_pred=moddde.predict(d_test)
print("Accuracy for SVC linear kernel " + str(metrics.accuracy_score(p_test, p_pred)))
#Apply SVC with RBF kernel
moddde = svm.SVC(kernel='rbf')
moddde.fit(d_train, p_train)
p_pred=moddde.predict(d_test)
print("Accuracy for SVC with rbf kernel " + str(metrics.accuracy_score(p_test, p_pred)))