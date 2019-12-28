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
        if i<50:
            i+=1
        elif i>=50 and i<80:
            tx.append(np.load(os.path.join(path,f,apk)))
            ty.append(f)
            i+=1
        elif i>=80:
            x.append(np.load(os.path.join(path,f,apk)))
            y.append(f)
clf = svm.SVC(C = 10,tol = 0.001, cache_size = 300, probability=True)
#clf = svm.SVC(C = 10,tol = 0.001, cache_size = 3000,kernel='linear')
clf.fit(x,y)
p=clf.predict_proba(tx)
s=clf.predict(tx)
print(clf.score(tx,ty))
with open(unicode('C:\Users\yhm\Desktop\ld代码\\outcome.txt','utf-8'),'w')as w:
    for i in range(len(tx)):
        w.writelines(str(p[i])+' 预测结果： '+s[i]+' : '+ty[i]+'\n')

