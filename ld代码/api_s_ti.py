# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:26:50 2019

@author: yhm
"""

import os
import json
import re
#tf-idf中存在大量代码混淆的方法，使用正则匹配去除掉
def api_ti_statistic(path,outcome):#统计tf-idf最终筛选了多少不同的api，outcome列表用来存储结果
    pat=re.compile('[a-z]\(\)V')
    for f in os.listdir(path):
        if f.endswith('100-ti.json'):#读取了每一个类别tf-idf值最高的api，汇总到一起，但是显然有大量重复，很多所谓有代表性的api在每个类别中都出现
            api_f={}
            with open(os.path.join(path,f),'r')as r:
               api_f=json.load(r)
            for i in api_f:
                if i not in outcome:
                    if pat.match(i)!=None:
                        continue
                    outcome.append(i)
    with open(unicode('C:\Users\yhm\Desktop\ld代码\\api_ti_sec.txt','utf-8'),'w')as w: 
        json.dump(outcome,w)
path=unicode('C:\Users\yhm\Desktop\ld代码\\tf-idf','utf-8')
api_ti=[]#tf-idf筛选出来的api
api_ti_statistic(path,api_ti)
print('tf-idf select api: '+str(len(api_ti)))