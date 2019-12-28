# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 11:10:00 2019

@author: yhm
"""
#hits筛选效果不好，采取将tf-idf筛选的api全部做为特征，然后再添加hits筛选出来的靠前的特征合并组成特征集
import json
import collections
import re 
                
ordic={}
ordic=collections.OrderedDict()
api_ti=[]#存储tf-idf筛选出来的特征
api_sum=[]#存储两类特征合并之后的结果
with open(unicode('C:\Users\yhm\Desktop\ld代码\\api_hits_select.txt','utf-8'),'r')as r: 
    ordic=json.load(r)#获取之前生成的字典，里面保存的是hits筛选出来的api
with open(unicode('C:\Users\yhm\Desktop\ld代码\\api_ti_sec.txt','utf-8'),'r')as r: 
    api_ti=json.load(r)#获取之前获得的tf-idf筛选出来的api
for j in api_ti:
    api_sum.append(j)#将tf-idf筛选出来的特征完全添加到最后的特征集

i=593
#使用hits特征凑够500个特征
pat=re.compile('[a-z]\(\)V')
for i in ordic:
    if i>=1000:
        break
    if not i in api_sum:
        if pat.match(i)!=None:#去除掉经过代码混淆的毫无利用价值的api：类似 a()V
            continue
        api_sum.append(i+'\n')
        i+=1
#将结果存储到文件当中
with open(unicode('C:\Users\yhm\Desktop\ld代码\\api_1000.txt','utf-8'),'w')as w: 
        json.dump(api_sum,w)
#效果并不好，使用svm.SVC只有20%的准确率
print('done')