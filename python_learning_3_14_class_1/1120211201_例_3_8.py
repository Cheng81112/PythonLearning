'''
合法结婚年龄（嵌套分支语句）
我国的婚姻法规定，
男性22岁为合法结婚年龄，
女性20岁为合法结婚年龄。
因此如果要判断一个人是否到了合法结婚年龄，
首先需要使用双分支结构判断性别，
再用递进的双分支结构判断年龄，
并输出判断结果。
'''

sex = input("请输入您的性别（M或者F）：")
age = int(input("请输入您的年龄（1-120）："))
if sex == 'M':
    if age >= 22:
        print("到达合法结婚年龄")
    else:
        print("未到合法结婚年龄")
else:
    if age >= 20:
        print("到达合法结婚年龄")
    else:
        print("未到合法结婚年龄")