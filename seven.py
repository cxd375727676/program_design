# -*- coding: utf-8 -*-
# 用七段数码管画当前系统时间
import turtle, time


def drawgap():
    """绘制数码管间隔"""
    turtle.penup()
    turtle.fd(5)
 
    
def drawsingleline(draw):
    """根据draw来确定是实画一笔还是在空中虚画一笔"""
    drawgap()
    if draw:
        turtle.pendown()
    else:
        turtle.penup()   
    turtle.fd(40)
    drawgap()
    turtle.right(90)
    

def drawdigit(digit):
    """根据输入数字画数码管，主要思路是确定7笔哪些数字是实画的"""
    if digit in range(2,10) and digit != 7:
        drawsingleline(True)
    else:
        drawsingleline(False)
    
    if digit in [0,1] or digit in range(3,10):
        drawsingleline(True)
    else:
        drawsingleline(False)
        
    if digit in [0,2,3,5,6,8,9] :
        drawsingleline(True)
    else:
        drawsingleline(False)
        
    if digit in [0,2,6,8]:
        drawsingleline(True)
    else:
        drawsingleline(False) 
    #编号1-4数码管路径完成
    turtle.left(90)
        
    if digit in [0,4,5,6,8,9]:
        drawsingleline(True)
    else:
        drawsingleline(False)
        
    if digit in [0,2,3] or digit in range(5,10):
        drawsingleline(True)
    else:
        drawsingleline(False)
        
    if digit in range(0,5) or digit in range(7,10):
        drawsingleline(True)
    else:
        drawsingleline(False)
    
    turtle.left(180)
    #进入下个数字绘制起点位置
    turtle.penup()
    turtle.fd(20)

    
def drawdate(date):
    """输入给定字符串形式的日期，画出相应数码管.输入格式为%Y-%m=%d+"""
    turtle.pencolor("red")
    for i in date:
        if i == "-":
            turtle.write("年",font=("Arial", 18, "normal"))
            turtle.fd(40)
            turtle.pencolor("green")
        elif i == "=":
            turtle.write("月",font=("Arial", 18, "normal"))
            turtle.fd(40)
            turtle.pencolor("blue")
        elif i == "+":
            turtle.write("日",font=("Arial", 18, "normal"))
            turtle.fd(40)
        else:
            drawdigit(eval(i))


def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate(time.strftime("%Y-%m=%d+",time.localtime()))
    turtle.hideturtle()
    turtle.done()



if __name__ == '__main__':
    main()