# -*- coding: utf-8 -*-
# 圆周率计算：蒙特卡罗方法
from random import random
from time import perf_counter


n = 1000000
hits = 0
start = perf_counter()
for i in range(n):
    x = random()
    y = random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits += 1

pi = 4 * hits / n
print("圆周率值是: {}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter() - start))