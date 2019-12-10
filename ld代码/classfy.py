# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:59:00 2019

@author: liudong
"""
import os
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

tx=[]
ty=[]
x=[]
y=[]
dirs = os.listdir('C:/liudongoutcome/')
for d in dirs:
    if os.path.isdir('C:/liudongoutcome/'+d):
#        i = 0
        fs = os.listdir('C:/liudongoutcome/'+d)
        for f in fs:           
#            if i < 250:
#                tx.append(np.load('C:/liudongoutcome/'+d+"/"+f).flatten())
#                ty.append(d)
#                i += 1
#            else:
                x.append(np.load('C:/liudongoutcome/'+d+"/"+f).flatten())
                y.append(d)            


for i in range(len(x)):
    sample=x[i]
    for j in range(len(sample)):
        if np.isnan(sample[j]):
            sample[j]=0
#for i in range(len(x)):
#    preprocessing.scale(x[i])
clf=KNeighborsClassifier(n_neighbors=5)    
#clf = svm.SVC(C = 10,tol = 0.001, cache_size = 1000, kernel ='linear', probability=True)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)
clf.fit(X_train,y_train)
print(clf.score(X_test,y_test))
print(clf.predict(X_test))
print(y_test)
