# -*- coding: utf-8 -*-
"""
Created on Fri Nov 01 17:05:39 2019

@author: liudong
"""

import os
import json

def stastic(path,func):#统计每一个类别的api在多少个apk中出现
    api_sole={}#使用字典存储每一个类别的每个api在多少apk中出现
    num_p=0#统计所有apk数量
    global num_all
    for f in os.listdir(os.path.join(path,func)):
        if os.path.isdir(os.path.join(path,func,f)):
            if 'smali_parse.txt' in os.listdir(os.path.join(path,func,f)):
                flag={}#每个api在每个apk中只统计一次，该字典用于统计标记
                num_all+=1
                num_p+=1
                with open(os.path.join(path,func,f,'smali_parse.txt'),'r')as r:#smali_parse.txt包含每个应用的api
                    for line in r.readlines():
                        if line in flag.keys():
                            continue
                        else:
                            if line not in api_sole.keys():
                                api_sole[line]=1
                                flag[line]=1
                            elif line in api_sole.keys():
                                api_sole[line]+=1
                                flag[line]=1
    with open(path + "/api" + "_"+str(num_p) + '_'+func+'.json','w') as w:
        json.dump(api_sole,w)#w是写入对象
                                  
num_all=0
path ='C:\Users\yhm\Desktop\class\classtodownload'
#files=['ENTERTAINMENT','COMMUNICATION','BUSINESS','TOOLS','COMICS','BOOKS_AND_REFERENCE','EDUCATION']
files=['SOCIAL','PHOTOGRAPHY','SHOPPING']
for i in range(len(files)):
    stastic(path,files[i])
print(num_all)