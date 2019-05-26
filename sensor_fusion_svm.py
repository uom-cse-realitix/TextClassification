from __future__ import print_function
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from numpy import *
import numpy as np

command_classes = {'count': 0, 'color': 1, 'focus': 2, 'no_op': 3}

data_x = np.loadtxt('data/input_x.csv', dtype=float)
data_y = np.loadtxt('data/input_y.csv', dtype=float)

data_x_test = np.loadtxt('data/input_x_test.csv', dtype=float)
data_y_test = np.loadtxt('data/input_y_test.csv', dtype=float)

classifier = svm.SVC(kernel='poly', gamma='scale', degree=4)
classifier.fit(data_x, data_y)

cross_val_score(classifier, data_x_test, data_y_test, scoring='recall_macro')

predictions = classifier.predict(data_x_test)

print(classification_report(data_y_test, predictions))

