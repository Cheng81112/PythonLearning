'''
调用类属性
'''
class Dog:
    kind = '藏獒'  # 所有实例取值相同的类变量

    def __init__(self, name):
        self.name = name  # 每个实例取值独立的类变量

d = Dog("Fido")
e = Dog("Buddy")

print("小狗1的种类是: {}" .format(d.kind))
print("小狗2的种类是: {}" .format(e.kind))

print("小狗1的名字是: {}" .format(d.name))
print("小狗2的名字是: {}" .format(e.name))





