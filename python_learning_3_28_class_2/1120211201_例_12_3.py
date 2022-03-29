'''
创建类
增加类变量student_name
增加初始化函数__init__()
'''


class Student2:
    student_name = ""
    def __init__(self,name):
        self.student_name = name

    def eat(self, name, place):
        print("{}在{}吃饭".format(name, place))

    def sleep(self, name, place):
        print("{}在{}睡觉".format(name, place))

    def gotoclass(self, name, place, class_name):
        print("{}在{}上{}课".format(name, place, class_name))

    def dosport(self, name, place, sport_name):
        print("{}在{}{}".format(name, place, sport_name))

    def study(self, name, place):
        print("{}在{}自习".format(name, place))

    def makeup(self, name, place):
        print("{}在{}化妆".format(name, place))

    def playgame(self, name, place, game_name):
        print("{}在{}玩{}".format(name, place, game_name))

    def watchvideo(self, name, video):
        print("{}在看{}".format(name, video))

