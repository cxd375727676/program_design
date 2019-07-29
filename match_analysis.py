# -*- coding: utf-8 -*-
# 比赛模拟
from random import random


def print_info():
    """打印项目介绍信息"""
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0到1之间的小数表示)")


def get_inputs():
    """获得用户输入选手能力值，比赛常数，返回数值元组""" 
    a=eval(input("请输入选手A的能力值(0-1): "))
    b=eval(input("请输入选手B的能力值(0-1): "))
    n=eval(input("模拟比赛的场次: "))
    return a, b, n


def sim_onegame(probA, probB):
    """输入能力值，输出在一场比赛结束后双方得分情况。率先得到15分者赢得该场比赛"""
    scoreA, scoreB = 0, 0
    serving = "A"     # A先发球
    # 在各自发球回合赢球才能得分，否则仅仅是获得球权
    while not (scoreA == 15 or scoreB == 15):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

              
def sim_ngames(n, probA, probB):
    """输入总场次与能力值，输出各自获胜场次""" 
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = sim_onegame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def print_summary(winsA,winsB):
    """根据双方获胜场次打印获胜比率等信息"""
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛, 占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛, 占比{:0.1%}".format(winsB,winsB/n))


def main():
    print_info()
    probA, probB, n = get_inputs()
    winsA, winsB = sim_ngames(n, probA, probB)
    print_summary(winsA, winsB)
    

if __name__ == '__main__':
    main()