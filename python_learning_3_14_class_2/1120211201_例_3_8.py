'''
九九乘法表
编写程序，使用双重循环输出九九乘法表

'''

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}" .format(i,j,i*j),end="\t")
    print("\n")