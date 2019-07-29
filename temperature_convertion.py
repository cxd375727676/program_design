# -*- coding: utf-8 -*-
#温标转换
# 输入后缀F或C
temp=input("please input temperature with signal:")
if temp[-1].upper()=="F":#输入的是华氏温度
    temp_c=(eval(temp[0:-1])-32)/1.8 #eval函数将字符串外层引号去掉，执行相应命令
    print("转化后的温度是{0:.2f}C".format(temp_c))
elif temp[-1].upper()=="C":#输入的是摄氏温度
    temp_f=eval(temp[0:-1])*1.8+32
    print("转化后的温度是{0:.2f}F".format(temp_f))
else:
    print("输入格式错误")