'''
同学们的一天
'''
def eat(name, place):
    print("{}在{}吃饭".format(name, place))
def sleep(name, place):
    print("{}在{}睡觉".format(name, place))
def gotoclass(name, place, class_name):
    print("{}在{}上{}课".format(name, place, class_name))
def dosport(name, place, sport_name):
    print("{}在{}{}".format(name, place, sport_name))
def study(name, place):
    print("{}在{}自习".format(name, place))
def makeup(name, place):
    print("{}在{}化妆".format(name, place))
def playgame(name, place, game_name):
    print("{}在{}玩{}".format(name, place, game_name))
def watchvideo(name, video):
    print("{}在看{}".format(name, video))


#小明的一天
student1 = "小明"
print(" ======{}的一天===== =".format(student1))
eat(student1,"食堂")
gotoclass(student1,"一教","Python")
dosport(student1, "操场","打篮球")
study(student1, "图书馆")
sleep(student1, "2号楼")
#小红的一天
student2 = "小红"
print("====={}的一天======".format(student2))
eat(student2, "-食堂")
gotoclass(student2, "二教", "马列")
makeup(student2, "3号楼")
study(student2, "图书馆")
sleep(student2,"2号楼")
#小刚的一天
student3 = "小刚"
print("===={}的一天=====".format(student3))
eat(student3, "二食堂")
gotoclass(student3, "一教","微积分")
playgame(student3, "学生活动中心","数独")
watchvideo(student3, "Python程序设计")
