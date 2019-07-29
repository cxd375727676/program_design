# -*- coding: utf-8 -*-
"""
三国演义词频统计——升级版
荆州出现425次！！！！！！！！！
出场人物统计升级版
"""


import jieba
txt = open(r"input\threekingdoms.txt", "r",encoding="utf=8").read()
excludes = {"将军","却说","荆州","二人","不可","不能","如此"}
words = jieba.lcut(txt)    #jieba能够滤掉标点
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        reword = "孔明"
    elif word == "关公" or word == "云长":
        reword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        reword = "刘备"
    elif word == "孟德" or word == "丞相":
        reword = "曹操"
    else:
        reword = word
    counts[reword] = counts.get(reword, 0) + 1

#人物频率排序
for word in excludes:
    del counts[word]
items = list(counts.items()) #将字典转化为列表，键值对以元组形式构成列表元素
items.sort(key=lambda x:x[1], reverse=True)
#前十词频排名
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))