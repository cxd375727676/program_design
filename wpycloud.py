import jieba
import wordcloud
#中文需先用jieba分词，再用空格连接成字符串
txt="程序设计语言是计算机能够理解和\
识别用户操作意图的一种交互体系，它按照\
特定规则组织计算机指令，使计算机能够自\
动进行各种运算处理。"
w=wordcloud.WordCloud(width=1000,height=700,font_path="msyh.ttc")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywcloud.png")