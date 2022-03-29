"""
•创建一个ANIMAL类，包含
    •类变量
        •zhonglei（种类）、name（名字）
    •类函数
        •eat（吃）、jump（跳）
•再创建一个CAT类，继承ANIMAL类,并包含
    •类函数
        •miaomiaobark（喵喵叫）
•创建三个cat对象，“小白猫”，“小红猫”,”小蓝猫”,分别调用不同的类变量和类函数
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

# 对象
bai = Cat("小白猫","银渐层")
hong = Cat("小红猫","短毛")
lan = Cat("小蓝猫","无毛")

bai.eat()
bai.jump()
bai.miaomiaobark()

hong.jump()
hong.eat()
hong.miaomiaobark()

lan.eat()
lan.jump()
lan.miaomiaobark()
