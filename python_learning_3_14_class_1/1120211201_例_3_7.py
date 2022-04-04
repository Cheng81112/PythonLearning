'''
判断三角形
多条件判断
编写程序，从键盘输入三条边，
判断是否能够构成一个三角形。
如果能，
则提示可以构成三角形；
如果不能，
则提示不能构成三角形。
'''


side1 = float(input("请输入三角形第一条边："))
side2 = float(input("请输入三角形第二条边："))
side3 = float(input("请输入三角形第三条边："))

if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print("{} {} {} 可以构成三角形" .format(side1,side2,side3))
else:
    print("{} {} {} 不可以构成三角形" .format(side1,side2,side3))
