# for name in ["姓名","电话","QQ","邮箱"]:
#     print(name,end="")

#
# L = [1,2,3,4,5,6,7,8]
# print(L[0:1])


# L = [1,2,3,4,5,6,7,8]
# print(L[0:4:2])


# list=['hello','world']
# print('hello {0[0]}  i am {0[1]}'.format(list))


# print('圆周率是{:.2f}'.format(3.1415926))

# return可以返回一个函数的执行结果，下方的代码不会执行；如果return后没有任何内容，表示返回到调用函数的位置，并且不返回任何结果

# python中又两种多值参数
    # 参数名前增加一个*可以接收元组
    # 参数名前增加两个*可以接收字典

    # *args--存放元组参数    args是arguments的缩写，又变量的含义
    # **kwargs--存放字典参数     kw是keyword的缩写，kwargs可以记忆键值对参数
# def demo(num, *args, **kwargs):
#     print(num)
#     print(args)
#     print(kwargs)
#
#
# demo(1,2,3,4,5,name='小明',age=18,gender=True)

# 多值参数案例--计算任意多个数字的和
# 需求
# 1.定义一共sum_numbers，可以接收到任意多个数
# 2.功能需求：将传递的所有数字累加并且返回累加结果
# def sum_number(*args):  # * 调用多值参数
#     num=0
#     print(args)
#     # 循环遍历
#     for i in args:
#          num += i
#     return num
# result = sum_number(1,2,3)
# print(result)

# 元组和字典的拆包
# def demo(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# # 元组、字典变量
# gl_nums = (1,2,3,4)
# gl_dict = {"name": "小梦", "age": 18}
#
# #demo(gl_nums, gl_dict) # 会把gl_nums, gl_dict作为元组传递给args
#
# # demo(*gl_nums,**gl_dict) # 拆包语法，简化元组变量、字典变量的传递
# demo(1,2,3,4,name='小梦',age=18,)

# 函数递归
# 针对参数不同，处理的结果不同
# 当参数满足一个条件时，函数不再执行
# 函数的出口很重要，否则会出现死循环
# 递归案例--计算数字累加
# 需求
# 1.定义一个函数sum_numbers
# 2.能够接收一个num的整数参数
# 3.计算1+2+3+4+5+···+num的结果
# def sum_number(num):
#
#     # 1.出口
#     if num==1:
#         return 1
#     # 2.数字的累加
#
#     temp=sum_number(num-1)
#     # 两个数字相加
#     return num+temp
# result=sum_number(100)
# print(result)



# 面向对象
# 面向过程
# import numpy as np
#
# def distance(e1, e2):
#     return np.sqrt((e1[0]-e2[0])**2+(e1[1]-e2[1])**2)
#
# a_dict=[2,2]
# b_dict=[3,4]
# a = (1,23,5)
# b = [1,23,5]
# # print(name[0:3:2])
# name={'1':'完成','name':'曹玉洁','3':'仲秋萍'}
# # a[1]=0
# b[1]=15
# for a1 in b:
#     print(a1)

# m = 6
#
# for i in range(1,m - 1):
#     print(i)

import  math
# num=10.0
# a=math.sqrt(num)
# print(a)

#
# def demo():
#     print('测试函数')
# print(dir(2))

# class Cat:
#     def eat(self):
#         # 哪一个对象调用的方法，self就是哪一个对象的引用
#         print('%s 爱喝水' % self.name)
#     def drink(self):
#         print('%s 爱吃鱼' % self.name)
# #创建猫对象    对象有哪些属性封装在类中
# tom=Cat()
#
# # 添加属性 利用赋值语句即可

# # 调用方法
# tom.eat()
# tom.drink()


# class Cat:
#     '''这是一个猫类'''
#     def __init__(self):
#         print('这是一个初始化方法')
#
# # 使用类名（）创建对象的时候，会自动调用初始化方法__init__
# tom=Cat()

#
# class Cat:
#     '''这是一个猫类'''
#     def __init__(self):
#         print('这是一个初始化方法')
#         self.name='Tom'
#         # self.属性名=属性初始值
# # 使用类名（）创建对象的时候，会自动调用初始化方法__init__
#     def eat(self):
#         print('%s 爱吃鱼' % self.name)
# tom=Cat()
# tom.eat()

# class Cat:
#     '''这是一个猫类'''
#     def __init__(self,new_name):
#         print('这是一个初始化方法')
#         self.name = new_name
#         # self.属性名=属性初始值
# # 使用类名（）创建对象的时候，会自动调用初始化方法__init__
#     def eat(self):
#         print('%s 爱吃鱼' % self.name)
# tom=Cat('tom')
# tom.eat()
#
# lazy_cat=Cat('jack')
# lazy_cat.eat()

# class Cat:
#     def __init__(self,new_name):
#         self.name=new_name
#         print('%s 来了' % self.name)
#     def __del__(self):
#         print('%s 我去了' % self.name)
# tom=Cat('Tom')
# print(tom.name)
# # del 关键字可以删除一个对象
#
# del tom
#
# print('---')
#
# class Cat:
#     def __init__(self,new_name):
#         self.name=new_name
#         print('%s 来了' % self.name)
#     def __del__(self):
#         print('%s 我去了' % self.name)
#     def __str__(self):
#         # 必须返回字符串
#         return '我是小猫[%s]' %self.name
#
# # tom是一个全局变量
#
# tom=Cat('Tom')
#
# print(tom)


# 面向对象封装案例

# class Person:
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#         print('%s 体重75公斤' % self.name)
#     def run(self):
#         print('%s 每次跑步会减肥0.5公斤' % self.name)
#     def eat(self):
#         print('%s 每次吃东西会增加1公斤' % self.name)
#
# xiaoming=Person('小明',75.0)
#
# xiaoming.eat()
# xiaoming.run()

# class Person:
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#
#     def __str__(self):
#         return '我的名字是%s, 体重是%.2f公斤'%(self.name,self.weight)
#     def run(self):
#         print('%s 每次跑步会减肥0.5公斤' % self.name)
#         self.weight -= 0.5
#     def eat(self):
#         print('%s 每次吃东西会增加1公斤' % self.name)
#         self.weight += 1
#
# xiaoming=Person('小明',75.0)
#
# xiaoming.eat()
# xiaoming.run()
#
# print(xiaoming)

# class Person:
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#
#     def __str__(self):
#         return '我的名字是%s, 体重是%.2f公斤'%(self.name,self.weight)
#     def run(self):
#         print('%s 每次跑步会减肥0.5公斤' % self.name)
#         self.weight -= 0.5
#     def eat(self):
#         print('%s 每次吃东西会增加1公斤' % self.name)
#         self.weight += 1
#
# xiaoming=Person('小明',75.0)
#
# xiaoming.eat()
# xiaoming.run()
#
# print(xiaoming)
#
# xiaomei=Person('小美',45)
# xiaomei.eat()
# xiaomei.run()
# print(xiaomei)

# class HouseItem:
#     def __init__(self,name,area):
#         self.name=name
#         self.area=area
#     def __str__(self):
#         return '%s 占地 %.2f 平米' % (self.name,self.area)
#
#
# class House:
#     def __init__(self,house_type,area):
#         self.house_type=house_type
#         self.area=area
#         # 剩余面积
#         self.free_area=area
#         # 家具名称列表
#         self.item_list=[]
#
#     def __str__(self):
#         #自动将一对括号内部的代码连接在一起
#         return ('户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s'
#                 %(self.house_type,
#                   self.area,
#                   self.free_area,
#                   self.item_list))
#
#     def add_item(self,item):
#         print("要添加[%s]"%item)
#         # 1.判断家具面积
#         if item.area > self.free_area:
#             print('%s 面积太大了，无法添加' % self.item.name)
#             return
#         # 2.将家具添加到列表中
#         self.item_list.append(item.name)
#
#         # 3.计算剩余面积
#         self.free_area -= item.area
#
#
# # 1.创建家具
# bed=HouseItem('席梦思',4)
# chest=HouseItem('衣柜',2)
# table=HouseItem('餐桌',1.5)
#
# print(bed)
# print(chest)
# print(table)
#
# # 2.创建房子对象
# my_home=House("两室一厅",60)
# my_home.add_item(bed)
# my_home.add_item(chest)
# my_home.add_item(table)
#
# print(my_home)
# #
# class Gun:
#     def __init__(self,model):
#         # 1.枪的型号
#         self.model=model
#         # 2.枪的数量
#         self.bullet_count = 0
#     def add_bullet(self,count):
#         self.bullet_count += count
#     def shoot(self):
#         # 1.判断子弹数量
#         if self.bullet_count <=0:
#             print('[%s]没有子弹了。。。'%self.model)
#             return
#         # 2.发射子弹
#         self.bullet_count -= 1
#
#         # 3.提示发射信息
#         print('[%s]突突突,剩余子弹[%s]' %(self.model,self.bullet_count))
#
#
#
# class Soldier:
#     def __init__(self,name):
#         self.name=name
#         self.gun=None
#         print('士兵%s有一把AK47' %(self.name))
#     def fire(self):
#         # 1.判断士兵是否有枪
#         if self.gun is None:
#             print("[%s]还没有枪。。"% self.name)
#             return
#         # 2.高喊口号
#         print('冲啊...[%s]'%self.name)
#         # 3.让枪装填子弹
#         self.gun.add_bullet(50)
#         # 4.让枪发射子弹
#         self.gun.shoot()
#
#
# # 1.创建枪属性
# ak47=Gun("AK47")
#
# # 2.创建许三多
# shibing=Soldier('许三多')
# shibing.gun=ak47
# shibing.fire()
#
# print(shibing.gun)

# class Women:
#     def __init__(self,name):
#         self.name=name
#         self.__age=18
#
#     def __secret(self):
#         # 在对象的方法内部，是可以访问对象的私有属性的
#         print("%s的年龄是%d" %(self.name,self.__age))
#
# xiaofang=Women("小芳")
# # 私有属性在外界不能够被直接访问
# # print(xiaofang.__age)
# # 私有方法，同样不允许在外界直接访问
# xiaofang.__secret()


# class Women:
#     def __init__(self,name):
#         self.name=name
#         self.__age=18
#
#     def __secret(self):
#         # 在对象的方法内部，是可以访问对象的私有属性的
#         print("%s的年龄是%d" %(self.name,self.__age))
#
# xiaofang=Women("小芳")
# # 伪私有属性在外界不能够被直接访问
# print(xiaofang._Women__age)
# # 伪私有方法，同样不允许在外界直接访问
# # xiaofang.__secret()
# xiaofang._Women__secret()

# 继承

# class Animal:
#     def eat(self):
#         print("吃")
#     def drink(self):
#         print("喝")
#     def run(self):
#         print("跑")
#     def sleep(self):
#         print("睡")
#
#
# class Dog:
#     def eat(self):
#         print("吃")
#     def drink(self):
#         print("喝")
#     def run(self):
#         print("跑")
#     def sleep(self):
#         print("睡")
#     def bark(self):
#         print("汪汪叫")
# class XiaoTianDog:
#     def eat(self):
#         print("吃")
#     def drink(self):
#         print("喝")
#     def run(self):
#         print("跑")
#     def sleep(self):
#         print("睡")
#     def bark(self):
#         print("汪汪叫")
#     def fly(self):
#         print("飞")
#
# # 创建一个狗对象
# wangcai=Dog()
# wangcai.run()
# wangcai.sleep()
# wangcai.drink()
# wangcai.eat()
# wangcai.bark()


# class Animal:
#     def eat(self):
#         print("吃")
#
#     def drink(self):
#         print("喝")
#
#     def run(self):
#         print("跑")
#
#     def sleep(self):
#         print("睡")
#
# class Dog(Animal):
#     def bark(self):
#         print("汪汪叫")
#
#
# class XiaoTianDog(Animal):
#     def fly(self):
#         print("飞")
#
#
# class Cat(Animal):
#     def catch(self):
#         print("抓老鼠")
#
#
#
# # 创建一个狗对象
# wangcai = Dog()
# wangcai.run()
# wangcai.sleep()
# wangcai.drink()
# wangcai.eat()
# wangcai.bark()
#
# # 创建哮天犬对象
# feigou=XiaoTianDog()
# feigou.run()
# feigou.fly()
#
#
# # feigou.catch()
#
# # 专业术语，dog是animal 的派生类，animal类是dog类的基类，dog类从animal类派生



# dayup=pow(1+0.001,365)
# daydown=pow(1-0.001,365)
# print(dayup)
# print(daydown)

# x=[1,2,3,4,5,6]
# n=[1,2,3,4,6,5]
#
# c=(x in n)
# print(c)


# 星期的选取
# weekstr="星期一星期二星期三星期四星期五星期六星期日"
# weekid=input("请输入今天是星期几(1-7)：")
# wkid=eval(weekid)*3
# # print(wkid)
# # print(wkid-3)
# xq=weekstr[wkid-3:wkid]
# print(xq)

# shuzi="43215"
# print("千位数字是：%s"%shuzi[1])
# print("个位数字是：%s"%shuzi[4])





































