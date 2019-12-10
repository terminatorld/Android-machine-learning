# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 22:37:10 2019

@author: liudong
"""

import os
num=0
path ='C:\Users\yhm\Desktop\class\classtodownload\LIBRARIES_AND_DEMO'
for f in os.listdir(path):
    if os.path.isdir(os.path.join(path,f)):
        if os.path.exists(os.path.join(path,f,'smali_parse.txt')) and os.path.getsize(os.path.join(path,f,'smali_parse.txt'))==0:
            num+=1
print(num)
            
