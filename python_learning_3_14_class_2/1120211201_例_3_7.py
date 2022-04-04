'''
计算π的近似值
编写程序，用下列公式计算π的近似值，直到最后一项的绝对值小于10-6为止

'''

import math

n = 1 # 变量自增值
t = 1 # 每项值
total = 0 # 1/4π的值
flag = 1 # 标记位

count = 0 # 循环次数

while math.fabs(t) >= 1e-6: # 当每一项的绝对值大于1e-6时进行计算
    total += t
    flag = -flag
    n += 2
    t = flag * 1.0 / n
    count += 1
    print("count={},Π={}" .format(count,total*4))
