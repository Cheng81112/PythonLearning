'''
多分支+嵌套
编写程序，
开发一个小型计算器，
从键盘输入两个数字和一个运算符，根据运算符（+、-、*、/）
进行相应的数学运算，
如果不是这4种运算符，则给出错误提示。
'''

first = eval(input("请输入第一个数字："))
second = eval(input("请输入第二个数字："))
sign = input("请输入运算符号：")
if sign == "+":
    print("两数字之和为：{}" .format(first + second))
elif sign == "-":
    print("两数字之差为：{}" .format(first - second))
elif sign == "*":
    print("两数字之积为：{}" .format(first * second))
elif sign == "/":
    if second == 0:
        print("除数不能为0")
    else:
        print("两数之商为：{}" .format(first/second))

else:
    print("符号有误")


