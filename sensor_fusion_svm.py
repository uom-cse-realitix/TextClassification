from __future__ import print_function
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from numpy import *
import numpy as np
from sklearn.externals import joblib

command_classes = {'count': 0, 'color': 1, 'focus': 2, 'no_op': 3}

data_x = np.loadtxt('data/input_x.csv', dtype=float)
data_y = np.loadtxt('data/input_y.csv', dtype=float)
#
data_x_test = np.loadtxt('data/input_x_test.csv', dtype=float)
data_y_test = np.loadtxt('data/input_y_test.csv', dtype=float)

classifier = svm.SVC(kernel='linear', gamma='scale')
classifier.fit(data_x, data_y)

cross_val_score(classifier, data_x_test, data_y_test, scoring='recall_macro')

command_classes_arr = ['count', 'color', 'focus', 'no_op']
words_file = open("data/words.txt", "r")
words = words_file.read().split('\n')[:-1]


def get_phrase(x):
    phrase = ""
    for i in range(len(words)):
        if x[i] == 1:
            phrase += words[i] + " "
    return phrase


predictions = classifier.predict(data_x_test)

ar = [(command_classes_arr[int(predictions[i])], get_phrase(data_x_test[i])) for i in range(len(predictions))]
print(ar)

joblib.dump(classifier, 'saved_model.pkl')
#
#
# clf_load = joblib.load('saved_model.pkl')


print(classification_report(data_y_test, predictions))
#
# print(predictions)
