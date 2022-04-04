'''
创建类
面向对象实现
'''
class Student:
    def eat(self,name, place):
        print("{}在{}吃饭".format(name, place))

    def sleep(self,name, place):
        print("{}在{}睡觉".format(name, place))

    def gotoclass(self,name, place, class_name):
        print("{}在{}上{}课".format(name, place, class_name))

    def dosport(self,name, place, sport_name):
        print("{}在{}{}".format(name, place, sport_name))

    def study(self,name, place):
        print("{}在{}自习".format(name, place))

    def makeup(self,name, place):
        print("{}在{}化妆".format(name, place))

    def playgame(self,name, place, game_name):
        print("{}在{}玩{}".format(name, place, game_name))

    def watchvideo(self,name, video):
        print("{}在看{}".format(name, video))
