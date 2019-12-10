# -*- coding: utf-8 -*-
"""
Created on Wed Nov 06 16:56:02 2019

@author: liudong
"""

import json

def dic_add(path1,path2):#因为weather文件夹不在服务器上，所以要把weather类的内容加到总数中
    with open(path1,'r')as r:
        dic1=json.load(r)
    with open(path2,'r')as r:
        dic2=json.load(r)
    for i in dic1:
        if i in dic2.keys():
            dic2[i]+=dic1[i]
        else:
            dic2[i]=dic1[i]
    return dic2

path1=unicode('C:\\Users\\yhm\\Desktop\\ld代码\\api-apk-WEATHER.json', 'utf8')
path2='C:\\Users\\yhm\\Desktop\\class\\classtodownload\\api-apk.json'
with open('C:\\Users\\yhm\\Desktop\\class\\classtodownload\\api-apk-all.json','w')as w:
    json.dump(dic_add(path1,path2),w)