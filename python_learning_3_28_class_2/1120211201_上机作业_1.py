"""
•创建一个CAT类，包含
    •类变量
        •zhonglei（种类）
        •name（名字）
    •类函数
        •miaomiaobark（喵喵叫）
        •eat（吃）
        •jump（跳）
•创建三个CAT对象，“小白猫”，“小红猫”,”小蓝猫”,分别调用不同的类变量和类函数
"""
class Cat:
    kind = ["小白猫","小红猫","小蓝猫"]

    def __init__(self,name,kind):
        self.name = name
        self.kind = kind

    def miaomiaobark(self):
        print("{}{}在喵喵叫".format(self.kind,self.name))
    def eat(self):
        print("{}{}在吃毛条".format(self.kind,self.name))
    def jump(self):
        print("{}{}在蹦蹦跳跳".format(self.kind,self.name))
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




