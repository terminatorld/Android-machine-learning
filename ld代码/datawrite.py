# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import nltk
import numpy
import re
import os
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


#英文停止词，set()集合函数消除重复项
list_stopWords=list(set(stopwords.words('english')))
f=os.listdir('C://liudongtestdata//')#遍历数据
all_word_dict={}#记录所有出现的词汇
for scan in f:
    if os.path.isdir('C://liudongtestdata//'+scan):
        ff=os.listdir('C://liudongtestdata//'+scan)
        for scan1 in ff:          
            with open('C:\\liudongtestdata\\'+scan+'\\'+scan1,'r') as fr:#读取每一个描述文件
                 text=fr.read()
            text = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', text)
            text=re.sub('[^a-zA-Z]',' ',text)#只保留英文字符
            text.replace('\n',' ').replace('  ',' ').lower().split(' ')
            #将文本拆分成句子列表
            sens = nltk.sent_tokenize(text)#
            #将句子进行分词,nltk的分词是句子级的,因此要先分句,再逐句分词,否则效果会很差.
            words=nltk.word_tokenize(str(sens))
            #去停止词
            words=[w for w in words if not w in list_stopWords]
            #词频计数
            for word in words:#统计每一个出现的词汇的出现次数
                if word in all_word_dict.keys():
                    all_word_dict[word]+=1
                else:
                    all_word_dict[word]=1
                 #word_count_dict = {}
                 #for word in words:
                 #    if word in word_count_dict.keys():
                 #        word_count_dict[word]+=1
                 #    else:
                 #        word_count_dict[word]=1
                 #word_count_dict = sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True)
                 #输出到文件
                 #with open('C:\\liudongoutcome\\'+scan, 'w')as f1:
                 #    for i in word_count_dict:
                 #        f1.write("%s\t%s\n" %(i[0],str(i[1])))
for word in all_word_dict.keys():#去掉出现次数小于3的数据
    if all_word_dict[word]>20:
        continue
    else:
        all_word_dict.pop(word)

        
#读取训练数据
all_words=all_word_dict.keys()
vectorizer = CountVectorizer()
transformer= TfidfTransformer()
transformer.fit_transform(vectorizer.fit_transform(all_words))#将统计数据向量化
for scan in f:
    ff=os.listdir('C://liudongtestdata//'+scan)
    for scan1 in ff:
        with open ('C:/liudongtestdata/'+scan+'//'+scan1,'r') as fr:
            str1=[fr.read()]
        tf = vectorizer.transform(str1)
        tfidf=transformer.transform(tf)
        data =[float(x) for x in tfidf.toarray()[0]]#将字符转为float
        with open('C:/liudongoutcome/'+scan+'//'+scan1,'w') as fw:
            numpy.save(fw,data)#结果写入文件
        print(tfidf.toarray())
print('写入完毕' )




all_word_dict = sorted(all_word_dict.items(), key=lambda x:x[1], reverse=True)#将统计的所有词汇写入到文件中
with open('C:\\liudongoutcome\\all_words.txt','w')as f2:
    for i in all_word_dict:
        if i[1]>1:
             f2.write("%s\t%s\n" %(i[0],str(i[1])))
