# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 19:12:27 2019

@author: yhm
"""

from sklearn import svm
import os
import numpy as np

tx=[]
ty=[]
x=[]
y=[]
path='C:\\Users\\yhm\\Desktop\\datas'
for f in os.listdir(path):
    i=0
    for apk in os.listdir(os.path.join(path,f)):
        if i<60:
            tx.append(np.load(os.path.join(path,f,apk)))
            ty.append(f)
            i+=1
        else:
            x.append(np.load(os.path.join(path,f,apk)))
            y.append(f)
clf = svm.SVC(C = 5,tol = 0.001, cache_size = 3000,kernel='linear')
clf.fit(x,y)
print(clf.score(tx,ty))