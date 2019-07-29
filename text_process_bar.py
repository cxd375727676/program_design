# -*- coding: utf-8 -*-
#文本进度条
import time
scale=10
print("------执行开始------")
for i in range(scale+1):
    a="*" * i
    b="." * (scale-i)
    c=int((i/scale)*100)
    print("{2:^3}%[{0}->{1}]".format(a,b,c))
    time.sleep(0.1)
print("------执行结束------\n\n")


#进度条单行刷新
import time
scale=50
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a="*" * i
    b="." * (scale-i)
    c=int((i/scale)*100)
    dur=time.perf_counter()-start
    print("\r{2:^3}%[{0}->{1}]{3:.2f}s".format(a,b,c,dur),end="")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,"-"))