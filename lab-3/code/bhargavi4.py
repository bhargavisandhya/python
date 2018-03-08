from sklearn.metrics import accuracy_score
from sklearn import neighbors,datasets
from sklearn.model_selection import train_test_split

#HERE WE WILL BE DEFINING AND ASSIGNING THE VARIABLES
BHS =datasets.load_iris()
DETAILS=BHS.data
labeldata=BHS.target
#THE TEST DATA IS BEING SPLIT INTO TWENTY PERCENT AND EIGHTY PERCENT
XtrainER,XtestER,XtrainER,YtestER=train_test_split(DETAILS, labeldata, test_size=0.8, random_state=56)
knn=neighbors.KNeighborsClassifier(n_neighbors=1)
#WE WILL BE SETTING THE VALUE FOR KKNN
knn.fit(XtrainER,YtrainER)
YpredictOR=knn.predict(Xtest)
#OUTCOMES ARE BEING PREDICTED HERE
#HERE WE WILL BE CALCULATING THE ACCURACY USING THE KNN
print("The accuracy score is ",accuracy_score(YpreDictOR,YtEstER))