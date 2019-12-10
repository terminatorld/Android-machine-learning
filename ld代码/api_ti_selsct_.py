# -*- coding: utf-8 -*-
"""
Created on Thu Nov 07 17:10:30 2019

@author: liudong
"""
#筛选api，看有多少api最终被各个类别筛选出来
import os
import json
path=unicode('C:\Users\yhm\Desktop\ld代码','utf-8')
api_ti=[]
for f in os.listdir(path):
    if f.endswith('-ti.json'):#读取了每一个类别tf-idf值最高的api，汇总到一起，但是显然有大量重复，很多所谓有代表性的api在每个类别中都出现
        api_f={}
        with open(os.path.join(path,f),'r')as r:
           api_f=json.load(r)
        for i in api_f:
            if i not in api_ti:
                api_ti.append(i)
for j in range(len(api_ti)):
    print(api_ti[j])      
print(len(api_ti))           
      