import numpy as np
from sklearn.svm import LinearSVC
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_boston

#crime_data = np.loadtxt("data/crime_data.csv", delimiter=",")
#crime_target = np.loadtxt("data/crime_target.csv")

#crime_data_train, crime_data_test, crime_target_train, crime_target_test =\
    #train_test_split(crime_data, crime_target)

#crime_clf = LinearSVC().fit(crime_data_train, crime_target_train)

boston = load_boston()

boston_X_train, boston_y_train, boston_X_test, boston_y_test = train_test_split(boston.data, boston.target)

print("Crime data:", len(crime_data))
