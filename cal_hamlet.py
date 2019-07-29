# -*- coding: utf-8 -*-
#哈姆雷特词频统计


def gettext():
    """获取英文文本"""
    txt=open(r"input\hamlet.txt","r").read()
    txt=txt.lower()
    #将文本中特殊符号替换为空格
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt=txt.replace(ch," ")
    return txt

hamlet_txt=gettext()
words=hamlet_txt.split() #默认空格为分隔符
counts={}
for word  in words:
    counts[word]=counts.get(word,0)+1
    """也可写为如下代码，上述更简练
    if word not in counts.keys():
        counts[word]=1
    else:
        counts[word]+=1
    """
#词频排序
items=list(counts.items()) #将字典转化为列表，键值对以元组形式构成列表元素
items.sort(key=lambda x:x[1], reverse=True)
#前十词频排名
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))