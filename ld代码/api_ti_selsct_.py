# -*- coding: utf-8 -*-
"""
Created on Thu Nov 07 17:10:30 2019

@author: liudong
"""
#筛选api，看有多少api最终被各个类别筛选出来
import os
import json
import re
import io

def api_ti_statistic(path,outcome):#统计tf-idf最终筛选了多少不同的api，outcome列表用来存储结果
    for f in os.listdir(path):
        if f.endswith('-ti.json'):#读取了每一个类别tf-idf值最高的api，汇总到一起，但是显然有大量重复，很多所谓有代表性的api在每个类别中都出现
            api_f={}
            with open(os.path.join(path,f),'r')as r:
               api_f=json.load(r)
            for i in api_f:
                if i not in outcome:
                    outcome.append(i)
                    
def api_call_statistic(path,all_call):#进行api集合拓展，用于后续hits算法
    #去读取每个类别选出来的初始api集合
    for f in os.listdir(path):
        with open(os.path.join(path,f),'r')as r:
            ini_api=json.load(r)
        for v in ini_api.values():
            v=0
        k=f.split('-')[0]#读取类别名
        if k =='WEATHER':
            continue
        print(k+' is scaning...')
        for ff in os.listdir(os.path.join('C:\Users\yhm\Desktop\class\classtodownload',k)):#去遍历每个类别的apk反编译文件
            if os.path.isdir(os.path.join('C:\Users\yhm\Desktop\class\classtodownload',k,ff)):
                if os.path.exists(os.path.join('C:\Users\yhm\Desktop\class\classtodownload',k,ff,'api_call.txt')):
                    with io.open(os.path.join('C:\Users\yhm\Desktop\class\classtodownload',k,ff,'api_call.txt'),'r',encoding='utf-8')as r:
                        for line in r.readlines():#如果在当前调用关系中找到了被筛选出来的api，就将该调用关系添加到记录列表all_call中
                            l1=re.findall(r'\'(\S+)\'',line)
#                            if l1[0]+'\n' in ini_api.keys() and ini_api[l1[0]+'\n']<30:#限定最大链接数，不然最后api数量过多
                            if l1[0]+'\n' in ini_api.keys():
                                ini_api[l1[0]+'\n']+=1
                                #如果调用关系中有被筛选出来的api，则保存这条调用关系
                                #这样的方法导致87个api拓展出了25万条链接关系（不包含weather），因此需要对关系进行筛选和限制
                                all_call.append(str(l1))#之所以存为string，是因为去重操作中，list转set不允许list[list]转set
#                            elif l1[1]+'\n' in ini_api.keys() and ini_api[l1[1]+'\n']<30:
                            elif l1[1]+'\n' in ini_api.keys():
                                ini_api[l1[1]+'\n']+=1
                                all_call.append(str(l1))
                    
path=unicode('C:\Users\yhm\Desktop\ld代码\\tf-idf','utf-8')
api_ti=[]#tf-idf筛选出来的api
api_add=set()#拓展之后的api集合，set用于去重
all_api_call=[]#所有api的调用关系，存在大量重复，使用的是string存储
api_ti_statistic(path,api_ti)
print('tf-idf select api: '+str(len(api_ti)))
api_call_statistic(path,all_api_call)
res=list(set(all_api_call))#存为string的原因；对all_api_call[]去重，保留去重结果
for c in res:
    l2=re.findall(r'\'(\S+)\'',c)
    api_add.add(l2[0])
    api_add.add(l2[1])
with open(unicode('C:\Users\yhm\Desktop\ld代码\\all_api_ti_select.txt','utf-8'),'w')as w:#将筛选去重之后的api存入txt
        for a in api_add:
            w.write(a+'\n')        
print('There are '+str(len(api_add))+' apis.')#统计集合中一共有多少api
with open(unicode('C:\Users\yhm\Desktop\ld代码\\all_api_call.txt','utf-8'),'w')as w:#将去重之后的链接关系存入txt
        for c in res:
            w.write(c+'\n')
print('There are '+str(len(res))+' links.')#统计集合中有多少链接,存储在all_api_call.txt中