from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
#Loading the dataset
irisdataset=datasets.load_iris()

#getting the data and response of the dataset
d=irisdataset.data
p=irisdataset.target

d_train, d_test, p_train, p_test=train_test_split(d, p, test_size=0.2)

#split the data for training and testing
mode= KNeighborsClassifier(n_neighbors=5)
mode.fit(d_train, p_train)

p_pred=mode.predict(d_test)

print("Accuracy: ", metrics.accuracy_score(p_test, p_pred))

kd_range=range(1, 20)
scoredd=[]

for kks in kd_range:
    knn=KNeighborsClassifier(n_neighbors=kks)
    knn.fit(d_train, p_train)
    p_pred=knn.predict(d_test)
    scoredd.append(metrics.accuracy_score(p_test, p_pred))

import matplotlib.pyplot as plt

plt.plot(kd_range, scoredd)
plt.xlabel("value of k")
plt.ylabel("testing accuracy")
plt.show()