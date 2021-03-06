# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 11:32:01 2019

@author: yhm
"""

import os
import numpy as np
import json

def data(orderdic,path,c):#为每个类别的apk生成向量
    for f in os.listdir(os.path.join(path,c)):
        if os.path.isdir(os.path.join(path,c,f)) :
            vector=np.zeros(1000)#初步设定500维
            if os.path.exists(os.path.join(path,c,f,'smali_parse.txt')):
                with open(os.path.join(path,c,f,'smali_parse.txt'),'r')as r:
                    for line in r.readlines():
                        if line in api500:
                            vector[api500.index(line)]=1
                np.save(os.path.join('C:\\Users\\yhm\\Desktop\\datas',c,f,),vector)#将生成的向量保存到对应的文件夹内
                
path='C:\\Users\\yhm\\Desktop\\class\\classtodownload'
api500=[]
with open(unicode('C:\Users\yhm\Desktop\ld代码\\api_1000.txt','utf-8'),'r')as r: 
    api500=json.load(r)#获取之前生成的字典，里面保存的是hits筛选出来的api
for c in os.listdir(path):
    if os.path.isdir(os.path.join(path,c)) and c!='.ipynb_checkpoints' and c!='WEATHER':
        if(os.path.exists(os.path.join('C:\\Users\\yhm\\Desktop\\datas',c))):
            data(api500,path,c)
        else:
            os.makedirs(os.path.join('C:\\Users\\yhm\\Desktop\\datas',c))
            data(api500,path,c)
