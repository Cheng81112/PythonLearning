'''
类的调用
'''
class MyClass:
    """A simple example class"""
    i = 1234
    def f(self):
        return "hello world"

# 对象
myclass = MyClass()

print(myclass.i)
print(myclass.f())