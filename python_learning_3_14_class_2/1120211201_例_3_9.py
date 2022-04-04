'''
三角形图案
编写程序，使用双重循环输出所示三角形图案

'''

for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print("\n")
