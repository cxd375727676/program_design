# -*- coding: utf-8 -*-
#三国演义词频统计——初级版
import jieba


txt = open(r"input\threekingdoms.txt", "r", encoding = "utf = 8").read()
words = jieba.lcut(txt)    #jieba能够滤掉标点
counts = {}
for word  in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

#词频排序
items = list(counts.items())    #将字典转化为列表，键值对以元组形式构成列表元素
items.sort(key=lambda x: x[1], reverse=True)
#前十词频排名
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))