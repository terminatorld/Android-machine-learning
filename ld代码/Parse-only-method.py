# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 09:20:09 2019

@author: liudong
"""
import os
import re
from xml.dom.minidom import parse

    
def open_xml(path):#寻找Androidmanifest.xml文件路径,flag用于标记反编译失败的文件
    files=os.listdir(path)
    for f in files:
        if f.endswith('.xml'):
            p=os.path.join(path,f)
            return p

def w_in_txt(path,list1,k):#将permission列表和activity列表写入文件
    if k=='p':
        with open(os.path.join(path,'permissions.txt'),'w',encoding='utf-8') as f:
            for line in list1:
                f.write(line+'\n')
    elif k=='s':
        with open(os.path.join(path,'smali_parse.txt'),'w',encoding='utf-8') as f:
            for line in list1:
                f.write(str(line)+'\n')      
    elif k=='a':
        with open(os.path.join(path,'api_call.txt'),'w',encoding='utf-8') as f:
            for line in list1:
                f.write(str(line)+'\n')
               
def parse_xml(path,mpath,p,act):#解析xml文件,获取权限和activity信息
    #有的历史遗留文件夹由于文件名过长删不掉，里面没有manifest文件，导致报错
    try:#处理出现的InsexError，但出现原因不明
        doc=parse(mpath)
    except AttributeError:
        print('AttributeError happened...')
        with open(os.path.join(path.rsplit('\\',1)[0],'error.txt'),'a+')as w:#如果出现这种文件，把文件名记录下来
            w.write(path+'\n')
    else:        
        data = doc.documentElement
        e = data.childNodes
        for child in e:
            if child.nodeName =='uses-permission':#获取权限列表
                str1=str(child.getAttribute('android:name'))
                p.append(str1)
            elif child.nodeName=='application':#获取activity列表
                for c in child.childNodes:
                    if c.nodeName=='activity':
                        str2=str(c.getAttribute('android:name'))
                        act.append(str2)
   
def get_smali_list(path,smali_list):#把所有的smali文件路径读到列表中去
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path,f)):
            get_smali_list(os.path.join(path,f),smali_list)
        elif f.endswith('.smali'):
            smali_list.append(os.path.join(path,f))#保存每一个smali文件完整路径
    return smali_list      

def parse_smali(activity_list,smali_name_list,smali_parse_list,api_call_list):
    for p in smali_name_list:
        #判断smali文件路径在不在activity_list中，首先将完整路径前半部分去掉，4是去掉了E 淘宝反编译 淘宝 smali
        #得到结果后需要去掉结尾的.smali，之后将‘\’变为‘.’。
        if p.split('\\',9)[9].split('.')[0].replace('\\','.') in activity_list:
            with open(p,'r',encoding='utf-8') as f:
                lines=f.readlines()
                for line in lines:
                    if line.startswith('.method'):
                        #f.readlines()读取一次后就没了，所以要赋给lines，line的每一行后面带一个换行符需要去掉，然后获取这个
                        #smali文件的第一行，保留类对象部分，后面添加.method语句的函数部分
                        smali_parse_list.append(line.strip().rsplit(' ',1)[1])
                    elif 'invoke-' in line:
                        try:#处理出现的InsexError，但出现原因不明
                            line=line.strip().split('->')[1]
                            #去掉前面的'   invoke—...{...}, '以及最后的换行符,[:-1]用于去掉结尾的分号
                        except IndexError:
#                            print('IndexError happened...')
                            continue
                        else:
                            smali_parse_list.append(line)
                api_call(lines,api_call_list)
    if not smali_parse_list:
        print('smali_parse_list is empty!')
    

def api_call(lines,api_call_list):#获取api的二、三重调用序列
    i=0
    for line in lines:
        if line.startswith('.method'):
            head=line
            j=1
            while(lines[i+j].startswith('.end')!=True):
                if 'invoke-' in lines[i+j]:
                    try:#处理出现的InsexError，但出现原因不明
                        a=[head.strip().rsplit(' ',1)[1],lines[i+j].strip().split('->')[1]]
                    except IndexError:
#                        print('IndexError happened...')
                        continue
                    else:
                        api_call_list.append(a)
                j+=1
        i+=1
        #上边得到两重调用 下边获得三重调用
#    for i in range(len(api_call_list)):
#        for j in range(len(api_call_list)):
#            if api_call_list[i][-1]==api_call_list[j][0]:
#                api_call_list[i].append(api_call_list[j][1])
#    if not api_call_list:
#        print('api_call_list is empty!')

def statistic(list1,dic):#t统计apk中smali各个api出现频率
    for line in list1:
        if line not in dic.keys():
            dic[line]=1
        else:
            dic[line]+=1
                           
if __name__=='__main__':
    permissions=[]
    acts=[]
    smali_name_list=[]
    smali_parse_list=[]
    api_call_list=[]
    
    func=['FINANCE']
    path='C:\\Users\\yhm\\Desktop\\class\\classtodownload'
    pat=re.compile(r'\'(.*?)\'')
    for j in range(len(func)):
        p=os.path.join(path,func[j])
        i=1
        for f in os.listdir(p):
            if os.path.isdir(os.path.join(p,f)):#判断是否为空文件夹
                if not os.listdir(os.path.join(p,f)):
                    print("No.{num} is empty...".format(num=i))
                    i+=1
                    continue
    #            if 'permissions.txt' in os.listdir(os.path.join(path,f)):#判断是否之前已经完成
    #                print("No.{num} has done last time...".format(num=i))
    #                i+=1
    #                continue
    #            start_time = time.perf_counter()
#                if i<=220:
#                    print("No.{num} has done before".format(num=i))
#                    i+=1
#                    continue
                parse_xml(os.path.join(p,f),open_xml(os.path.join(p,f)),permissions,acts)
                get_smali_list(os.path.join(p,f),smali_name_list)
                parse_smali(acts,smali_name_list,smali_parse_list,api_call_list)
                w_in_txt(os.path.join(p,f),permissions,'p')
                w_in_txt(os.path.join(p,f),smali_parse_list,'s')
                w_in_txt(os.path.join(p,f),api_call_list,'a')
    #            cost = time.perf_counter() - start_time
                print("No.{num} done...".format(num=i))
                i+=1
                permissions=[]
                acts=[]
                smali_name_list=[]
                smali_parse_list=[]
                api_call_list=[]
    #    statistic(smali_parse_list,smali_counts)
