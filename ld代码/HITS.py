# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:28:29 2019

@author: yhm
"""
import numpy as np
import re
from math import sqrt
import json
import collections
#将链接关系存为0-1矩阵
#为每个api赋初值
#进行hits迭代

def lmatrix(apipath,linkpath,apis,links):#将链接关系转换为二维矩阵
    with open(apipath,'r')as r:#读取api
        for api in r.readlines():
            apis.append(api.strip())
    with open(linkpath,'r')as r:#读取链接关系
        for link in r.readlines():
            links.append(re.findall(r'\'(\S+)\'',link))
    l_m=np.zeros((len(apis),len(apis)))#定义链接矩阵
    #链接矩阵初始化
    for link in links:
        row=apis.index(link[0])
        column=apis.index(link[1])
        l_m[row][column]=1
    return l_m

#进行hits迭代，（链接关系矩阵、最大迭代轮数、迭代限制参数,authority最高的top_k个api）
def hits(matrix,max_iterations,in_delta,top_k):
    flag=False#标记迭代是否结束
    hub=np.ones(np.shape(matrix)[0])#list用于存储每个api的hub值
    authority=np.ones(np.shape(matrix)[0])#list用于存储每个api的authority值
    for k in range(max_iterations):#迭代轮数
        norm=0#标准化系数
        change = 0.0  # 记录每轮的变化值
        #更新authority值
        tmp=authority.copy()
        for i in range(np.size(authority)):
            authority[i]=0
            for j in range(np.size(hub)):
                if matrix[j][i]==1:
                    authority[i]+=hub[j]
                    norm+=pow(authority[i],2)
        norm = sqrt(norm)#将结果标准化
        for node in range(np.size(authority)):
            authority[node] /= norm
            change += abs(tmp[node] - authority[node])#记录迭代变化
        #更新hub值
        norm=0
        tmp=hub.copy()
        for i in range(np.size(hub)):
            hub[i]=0
            for j in range(np.size(authority)):
                if matrix[j][i]==1:
                    hub[i]+=authority[j]
                    norm+=pow(hub[i],2)
        norm = sqrt(norm)#将结果标准化
        for node in range(np.size(hub)):
            hub[node] /= norm
            change += abs(tmp[node] - hub[node])#记录迭代变化
        #判断是否结束迭代
        if change<in_delta:
            flag=True
            break
    if flag:
        print('共计经过{}轮迭代'.format(k))
    else:
        print('共计经过{}轮迭代'.format(max_iterations))
    outcome=authority.argsort()[::-1][0:top_k]#返回authority中值最大的前n个api
    top={}#用于存储authority最大api的位置和authority值
    top=collections.OrderedDict()#将无序字典变为有序字典
    for i in outcome:
        top[i]=authority[i]
    return top

if __name__ == '__main__':
    #apis=[]存储api
    #links=[]存储链接关系
    apis=[]
    links=[]
    api_selsct={}
    api_selsct=collections.OrderedDict()#将无序字典变为有序字典
    apipath=unicode('C:\Users\yhm\Desktop\ld代码\\all_api_ti_select.txt','utf-8')
    linkpath=unicode('C:\Users\yhm\Desktop\ld代码\\all_api_call.txt','utf-8')
    for key,value in hits(lmatrix(apipath,linkpath,apis,links),50,0.0001,500).items():
        api_selsct[apis[key]]=value
    with open(unicode('C:\Users\yhm\Desktop\ld代码\\api_hits_select.txt','utf-8'),'w')as w: 
        json.dump(api_selsct,w)