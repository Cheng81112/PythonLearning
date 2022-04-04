'''
带可变数量参数的函数
在函数定义时，可以设计可变数量参数，通过参数前增加星号（*）实现
'''
def vfunc(a, *b):
    print(type(b),len(b))
    for n in b:
        a += n
    return a
result = vfunc(1, 2,3,4,5)

print(result)

