import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
pip --user install matplotlib
iris = datasets.load_iris()

D = iris.data
P = iris.target
targname = iris.target_names

from sklearn.model_selection import train_test_split
D_train, D_test, P_train, P_test = train_test_split(X, P, test_size=0.30)

from sklearn.neighbors import KNeighborsClassifier
clas = KNeighborsClassifier(n_neighbors=5)
clas.fit(D_train, P_train)

P_pred = clas.predict(D_test)


ld = LinearDiscriminantAnalysis(n_components=2)
X = ld.fit(D_test, P_pred).transform(X)

plt.figure()
colors = ['YELLOW', 'PINK', 'orange']
lw = 2


for color, i, target_name in zip(colors, [0, 1, 2], targname):
    plt.scatter(X[P == i, 0], X[P == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of IRIS dataset')

plt.show()