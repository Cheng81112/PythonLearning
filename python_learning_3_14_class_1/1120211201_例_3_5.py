'''
去网吧2
二分支结构

'''

name = input("请输入您的姓名：")
age = int(input("请输入您的年龄："))

if age >= 18:
    print("{}已经成年" .format(name))
    print("欢迎上网")
else:
    print("{}还未成年" .format(name))
    print("回去吧，回到最初的美好")
