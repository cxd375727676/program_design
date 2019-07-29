# -*- coding: utf-8 -*-
# 政府工作报告形成词云
import jieba
import wordcloud


#with open("新时代中国特色社会主义.txt", "r", encoding="utf-8") as f:
with open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8") as f:
    t = f.read()

ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(width=1000, height=700, 
                        font_path="msyh.ttc", background_color="white")
w.generate(txt)
w.to_file("output\grwordcloud_1.png")