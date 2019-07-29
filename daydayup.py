# -*- coding: utf-8 -*-
# 累积的力量！

dayfactor = 0.001
up = pow(1+dayfactor,365)
down=pow(1-dayfactor,365)
print("up:{0:.2f} down:{1:.2f}".format(up,down))

#计算思维，工作日提升0.01，双休日退步0.01
result=1.0
dayfactor=0.01
for i in range(365):
    if i % 7 in [6,0]:
        result=result*(1-dayfactor)
    else:
        result=result*(1+dayfactor)
print("工作的力量：{:.2f}".format(result))

#A君每天进步0.01，累积效果37.78；B君双休日退步0.01，B君在工作日进步多少才能与A君持平？——试错法
def dayup(dayup_factor):
    """B君工作日进步dayup_factor，双休日退步0.01的最终结果"""
    result=1.0
    for i in range(365):
        if i % 7 in [6,0]:
            result=result*(1-0.01)
        else:
            result=result*(1+dayup_factor)
    return result

x=0.01
while dayup(x)<37.78:
    x+=0.001
print("需要在工作日努力：{:.3f}".format(x))