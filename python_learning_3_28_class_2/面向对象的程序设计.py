'''
面向对象的程序设计
'''
class Person:
    def __init__ (self, name):
        self.name = name
    def opendoor(self):
        print("{}打开门".format(self.name))
class Dog:
    def __init__ (self, name):
        self.name = name
    def bark(self):
        print("{}发出汪汪的声音" .format(self.name))
    def eat(self):
        print("{}吃骨头".format(self.name))
class Cat:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print("{}发出瞄瞄的声音".format(self.name))
    def eat(self):
        print("{}吃猫粮".format(self.name))
p1 = Person("小明")
d1 = Dog("小狼")
c1 = Cat("小虎")
p1.opendoor()
d1.bark()
c1.bark()
c1.eat()
d1.eat()
