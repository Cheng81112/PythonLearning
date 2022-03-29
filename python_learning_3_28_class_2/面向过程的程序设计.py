'''
面向过程的程序设计

'''

def opendoor(name):
    print("{}打开门".format(name))
def bark(name, voice):
    print("{}发出{}的声音".format(name, voice))
def eat(name, food):
    print("{}吃{}" .format(name, food))

opendoor("小明")
bark("小狗","汪汪" )
bark("小猫","喵喵")
eat("小猫","猫粮")
eat("小狗","骨头")