'''
用户登录（嵌套分支语句）
编写程序，从键盘输入用户名和密码，
要求先判断用户名再判断密码，
如果用户名不正确，
则直接提示用户名输入有误；
如果用户名正确，
则进一步判断密码，
并给出判断结果的提示
'''

username = input("请输入您的用户名：")
password = input("请输入您的密码：")
if username == "admin":
    if password == "12345":
        print("输入正确，请进入！")
    else:
        print("输入错误，请重试！")
else:
    print("用户名错误，请重试！")
