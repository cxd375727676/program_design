﻿# -*- coding: utf-8 -*-
"""
数字脚本
前进像素，0向左转1向右转，角度，RGB小数颜色
利用input\plot_data.txt 数据画图
"""

import turtle as t


t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

#数据读取
datals=[]
with open(r"input\plot_data.txt") as f:
    for line in f:
        line=line.replace("\n","")
        datals.append(list(map(eval,line.split(","))))
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])