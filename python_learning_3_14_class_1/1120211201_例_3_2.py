'''
编写程序，从键盘输入圆的半径，
计算并输出圆的周长和面积
'''

import math

p = math.pi

radius = float(input("请输入圆的半径："))
circumference = 2 * p * radius
area = p * radius ** 2

print("圆的周长为：{:.2f}" .format(circumference))
print("圆的面积为：{:.2f}" .format(area))
