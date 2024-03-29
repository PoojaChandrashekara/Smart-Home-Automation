# -*- coding: utf-8 -*-
"""KNN FINAL YEAR PROJECT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bELItbc_TjDgVNPnoWHsLXaxYqEAzCOg
"""

!pip install adafruit-blinka

!pip install adafruit-io

import numpy as np
import pandas as pd
import seaborn as sns
from Adafruit_IO import Client
sns.set_palette('husl')
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import csv as cv

a="MADHUYASHU"
b="8d7ee5784a5e4989bf04aadb530f3808"

aio=Client(a,b)

T = (input("Calculating time : "))

data = pd.read_csv('data (1).csv')

print (data.head())

print (data.info())

print (data.describe())

print (data['label'].value_counts())

X = data.drop(['Time', 'label'], axis=1)
y = data['label']
# print(X.head())
print(X.shape)
# print(y.head())
print(y.shape)

# experimenting with different n values
k_range = list(range(1,24))
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, y)
    y_pred = knn.predict(X)
    scores.append(metrics.accuracy_score(y, y_pred))

plt.plot(k_range, scores)
plt.xlabel('Value of k for KNN')
plt.ylabel('Accuracy Score')
plt.title('Accuracy Scores for Values of k of k-Nearest-Neighbors')
plt.show()
print("Accuracy: {}%".format(knn.score(X, y) * 100 ))

with open('data (1).csv', 'r') as F0:
    out = cv.DictReader(F0)
    for row in out:
        t = (row['Time'])
        if(t == T):
            a = (row['R1'])
            b = (row['R2'])
            c = (row['R3'])
            print ("At the time the user mentioned, that is at", T, "the value of relay is")
            print (a,b,c)
            knn = KNeighborsClassifier(n_neighbors=12)
            knn.fit(X, y)
            predicted_data = (knn.predict([[a,b,c]]))
            d = int(predicted_data)
            print ("That is",d,"should be on")
            print (type(d))
            test = aio.feeds("button1")
            aio.send_data(test.key,d)
            print ("done")
            break