# 作业一
'''
编写程序，产生两个10以内的随机整数，
以第一个随机整数为半径，
第二个随机整数为高，
计算并输出圆锥体的体积

'''
import random
import math


a=random.randint(1,10)
b=random.randint(1,10)

print(a)
print(b)
p=math.pi

v=(1/3)*p*a*a*b
print(v)








