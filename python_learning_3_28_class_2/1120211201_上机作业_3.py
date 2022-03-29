"""
•创建一个ANIMAL类，包含
    •类变量
        •zhonglei（种类）、name（名字）
    •类函数
        •eat（吃）、jump（跳）
•再创建一个CAT类，继承ANIMAL类,并包含
    •类函数
        •miaomiaobark（喵喵叫）
•再创建一个DOG类，继承ANIMAL类,并包含
    •类函数
        •wangwangbark（汪汪叫）
•创建一个cat对象 “小黑猫”和一个DOG对象“小黄狗”,分别调用不同的类变量和类函数
"""
class Animal:
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind
    def eat(self):
        print("{}{}在吃毛条".format(self.kind,self.name))
    def jump(self):
        print("{}{}在蹦蹦跳跳".format(self.kind,self.name))
class Cat(Animal):

    def miaomiaobark(self):
        print("{}{}在喵喵叫".format(self.kind,self.name))
class Dog(Animal):
    def wangwangbark(self):
        print("{}{}在汪汪叫".format(self.kind,self.name))

# 猫对象
cat = Cat("小黑猫","银渐层")
cat.eat()
cat.jump()
cat.miaomiaobark()

# 狗对象
dog = Dog("小黄狗","拉布拉多")
dog.jump()
dog.eat()
dog.wangwangbark()
