# -*- coding: utf-8 -*-
"""
Created on Wed Nov 06 19:15:27 2019

@author: liudong
"""

import os
import json
import re
import math

def termf(dic):#tf=该类别包含当前api的apk数/该类别总的apk数
    pat=re.compile(r'\d+')
    s=float(pat.findall(f)[0])
    tf={}
    for i in dic:
        tf[i]=dic[i]/s
    return tf

def inversedf(dic,sum_all):
    idf={}
    for i in dic:
        idf[i]=math.log(sum_all/(dic[i]+1))
    return idf

def sum_apk():
    sum_all=0
    pat=re.compile(r'\d+')
    for f in os.listdir('C:\Users\yhm\Desktop\class\classtodownload'):
        if f.startswith('api_') :
            n=int(pat.findall(f)[0])
            sum_all+=n
    return sum_all

path='C:\\Users\\yhm\\Desktop\\class\\classtodownload'
sum_all=sum_apk()#apk总数
with open(os.path.join(path,'api-apk-all.json'),'r')as r:
    t_all=json.load(r)
t_idf=inversedf(t_all,sum_all)#每一个api的idf
#求每一个类别中每一个api的tf值
for f in os.listdir(path):
    if f.startswith('api_'):
        tf_idf={}
        with open(os.path.join(path,f),'r')as r:
            t=json.load(r)
        t_tf=termf(t)
        for i in t_tf:
            if i in t_idf.keys():
                tf_idf[i]=t_tf[i]*t_idf[i]
        res={}
        i=0
        for k in sorted(tf_idf.items(), key=lambda item:item[1],reverse=True):#对每个类别的tf-idf进行排序取前25个
            if i>=100:
                break
            res[k[0]]=tf_idf[k[0]]
            i+=1
        
        with open(unicode('C:\Users\yhm\Desktop\ld代码\\tf-idf','utf-8')+'\\'+re.split('(\d+_)',f)[2].split('.')[0]+'-'+str(len(res))+'-ti.json','w')as w:
            #re.split('(\d+_)',f)[2]中使用数字_把类别名提取出来
            json.dump(res,w)       