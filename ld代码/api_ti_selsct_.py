# -*- coding: utf-8 -*-
"""
Created on Thu Nov 07 17:10:30 2019

@author: liudong
"""
#筛选api，看有多少api最终被各个类别筛选出来
import os
import json
import re

def api_ti_statistic(path,outcome):#统计tf-idf最终筛选了多少不同的api，outcome列表用来存储结果
    for f in os.listdir(path):
        if f.endswith('-ti.json'):#读取了每一个类别tf-idf值最高的api，汇总到一起，但是显然有大量重复，很多所谓有代表性的api在每个类别中都出现
            api_f={}
            with open(os.path.join(path,f),'r')as r:
               api_f=json.load(r)
            for i in api_f:
                if i not in outcome:
                    outcome.append(i)
                    
def api_call_statistic(pat,all_call):#进行api集合拓展，用于后续hits算法
    p="C:\Users\yhm\Desktop\ld代码\tf-idf=700"#去读取每个类别选出来的初始api集合
    for f in os.listdir(p):
        with open(os.path.join(p,f),'r')as r:
            ini_api=json.load(r)
        k=f.split('-')[0]#读取类别名
        if k =='WEATHER':
            continue
        for f in os.listdir(os.path.join('C:\Users\yhm\Desktop\class\classtodownload',k)):#去遍历每个类别的apk反编译文件
            if os.path.isdir(os.path.join('C:\Users\yhm\Desktop\class\classtodownload',k,f)):
                with open(os.path.join('C:\Users\yhm\Desktop\class\classtodownload',k,f,'api_call.txt'),'r')as r:
                    for line in r.readlines():#如果在当前调用关系中找到了被筛选出来的api，就将该调用关系添加到记录列表中
                        l1=re.findall(pat,line)
                        if l1[0] in ini_api.keys() or l1[1] in ini_api.keys():
                            all_call.append(l1)
    return all_call
                                    
                
                    
path=unicode('C:\Users\yhm\Desktop\ld代码\\tf-idf=500','utf-8')
api_ti=[]
pat=re.compile(r'\'(\S+)\'')#用于匹配api_call.txt中的api
print(len(api_ti))