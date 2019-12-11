# -*- coding: utf-8 -*-
"""
Created on Wed Nov 06 19:15:27 2019

@author: liudong
"""

import os
import json
import re
import math

def termf(dic):
    s=0
    for i in dic:
       s+=dic[i]
    tf={}
    for i in dic:
        tf[i]=dic[i]*700/s#频率值太小，因此乘500，1000太大，300太小，但实际上都存在严重的重复问题，也就是说tf-idf筛选能力很弱
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
        if f.startswith('api_'):
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
        for i in tf_idf:
            if tf_idf[i]!=0:
                res[i]=tf_idf[i]
        with open('C:\Users\yhm\Desktop\class\classtodownload'+'\\'+re.split('(\d+_)',f)[2].split('.')[0]+'-'+str(len(res))+'-ti.json','w')as w:
            #re.split('(\d+_)',f)[2]中使用数字_把类别名提取出来
            json.dump(res,w) 