'''
避免外部模块的干扰
'''

class MyClass:
    """A simple example class"""
    i = 1234
    def f(self):
        return "hello world"

if __name__ == "__main__":
    # 对象
    myclass = MyClass()

    print(myclass.i)
    print(myclass.f())