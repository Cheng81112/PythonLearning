'''
编写程序，
从键盘输入数字n，
通过循环计算1~n的乘积

'''
total =1
n = int(input("请输入数字n："))
for i in range(1,n+1):
    total *= i
print(total)
