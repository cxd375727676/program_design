# -*- coding: utf-8 -*-
# 递归的例子

def adverse_string(string):
    """ 字符串反转递归实现（尽管可用切片操作）"""
    if len(string) == 1:
        return string
    else:
        return string[-1] + adverse_string(string[:-1])
    

def fbnq(n):
    """ 斐波那契数列 """
    if n in [1,2]:
        return 1
    else:
        return fbnq(n-1)+fbnq(n-2)


#汉诺塔问题
count = 0
def hanoi(n, origin, goal, asist):
    """n个圆盘，从小到大编号1-n，从原柱子origin由辅助柱子assit挪到目标柱子goal，
    输出最小步骤数及移动方法"""
    global count
    if n == 1:
        print("圆盘1：{0}->{1}".format(origin, goal))
        count += 1
    else:
        hanoi(n - 1, origin, asist, goal)
        count += 1
        print("圆盘{0}： {1}->{2}".format(n, origin, goal))
        hanoi(n - 1, asist, goal, origin)

hanoi(3, "a", "c", "b")
print("总步骤：{}".format(count))


import turtle
def koch_curve(size,n):
    """n阶长度为size的科赫分形曲线"""
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch_curve(size/3, n-1)
def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)
    koch_curve(600,3)
    turtle.hideturtle()
main()


#科赫雪花        
def koch(size,n):
    """n阶长度为size的分形曲线"""
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main(n):
    """n阶科赫雪花"""
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.speed(10)
    turtle.pendown()
    turtle.pensize(2)
    for i in range(3):
        koch(400,n)
        turtle.right(120)
    turtle.hideturtle()
    turtle.done()
main(int(input("please input level: ")))