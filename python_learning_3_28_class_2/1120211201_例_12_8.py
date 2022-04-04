'''
针对classSTUDENT2的调用
'''


class Student2:
    student_name = ""

    def __init__(self, name):
        self.student_name = name

    def eat(self, place):
        print("{}在{}吃饭".format(self.student_name, place))

    def sleep(self, place):
        print("{}在{}睡觉".format(self.student_name, place))

    def gotoclass(self, place, class_name):
        print("{}在{}上{}课".format(self.student_name,  place, class_name))

    def dosport(self, place, sport_name):
        print("{}在{}{}".format(self.student_name,  place, sport_name))

    def study(self, place):
        print("{}在{}自习".format(self.student_name,  place))

    def makeup(self, place):
        print("{}在{}化妆".format(self.student_name,  place))

    def playgame(self, place, game_name):
        print("{}在{}玩{}".format(self.student_name,  place, game_name))

    def watchvideo(self, video):
        print("{}在看{}".format(self.student_name,  video))


if __name__ == "__main__":
    # 小明的一天
    student_name = "小明"
    student = Student2(student_name)
    print(" ======{}的一天======".format(student.student_name))
    student.eat("食堂")
    student.gotoclass("一教", "Python")
    student.dosport("操场", "打篮球")
    student.study("图书馆")
    student.sleep("2号楼")