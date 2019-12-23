# -*- coding: utf-8 -*-
"""
Created on Tue Nov 05 16:51:52 2019

@author: liudong
"""
import json
import os
import io

def api_apk(dic,path):#用于tf-idf初步筛选api的统计信息，统计每一个api在多少apk中出现。path中要包含类名
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path,f)) and os.path.exists(os.path.join(path,f,'smali_parse.txt')):
            flag={}#每个api在每个apk中只统计一次，该字典用于统计标记
            with io.open(os.path.join(path,f,'smali_parse.txt'),'r',encoding='utf-8') as r:
                for line in r.readlines():
                    if line in flag.keys():
                        continue
                    else:
                        if line not in dic.keys():
                            dic[line]=1
                            flag[line]=1
                        elif line in dic.keys():
                            dic[line]+=1
                            flag[line]=1
    return dic

path='C:\\Users\\yhm\\Desktop\\class\\classtodownload'
funcs=[]
for f in os.listdir(path):
    if os.path.isdir(os.path.join(path,f)) and f!='WEATHER':#统计23个类别名称
        funcs.append(f)
api_num_f_editon={}#初版统计所有的api
api_num={}#筛选掉一部分出现次数太少的api

for i in range(len(funcs)):
    api_apk(api_num_f_editon,os.path.join(path,funcs[i]))
for i in api_num_f_editon:
    if api_num_f_editon[i]>50:#只有至少在50个apk中出现过，才会被保留
        api_num[i]=api_num_f_editon[i]
with open('C:\\Users\\yhm\\Desktop\\class\\classtodownload\\api-apk.json','w')as w:#api-apk.json保存每个api在多少个apk中出现，所有类别
    json.dump(api_num,w)