'''
编写程序，从键盘输入密码，
如果密码长度小于6，
则要求重新输入。
如果长度等于6，
则判断密码是否正确，
如果正确则中断循环，
否则提示错误并要求继续输入。
'''
while 1:
    password = input("请输入密码：")
    if len(password) <6:
        print("长度为6位，请重新输入！")
        continue
    if password == "123456":
        print("密码正确！")
        break
    else:
        print("密码错误，请重试！")