# 作业3

'''
编写程序，从键盘输入a,b,c的值，
计算一元二次方程ax^2+bx+c=0的根，
根据b^2−4ac的值大于0、等于0及小于0分别进行讨论

'''
a=int(input("请输入a的值："))
b=int(input("请输入b的值："))
c=int(input("请输入c的值："))

if b*2-4*a*c>0:
    print("方程'ax*x+bx+c=0'有两个解")
elif b*2-4*a*c==0:
    print("方程'ax*x+bx+c=0'有一个解")
else:
    print("方程'ax*x+bx+c=0'无解")