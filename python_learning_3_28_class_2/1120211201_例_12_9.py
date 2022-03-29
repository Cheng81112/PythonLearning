'''
继承单个父类
'''
class Person:
    def eat(self,name, place):
        print("{}在{}吃饭".format(name, place))

    def sleep(self,name, place):
        print("{}在{}睡觉".format(name, place))


    def dosport(self,name, place, sport_name):
        print("{}在{}{}".format(name, place, sport_name))

    def makeup(self,name, place):
        print("{}在{}化妆".format(name, place))

    def playgame(self,name, place, game_name):
        print("{}在{}玩{}".format(name, place, game_name))

    def watchvideo(self,name, video):
        print("{}在看{}".format(name, video))

class Student(Person):
    def gotoclass(self,name, place, class_name):
        print("{}在{}上{}课".format(name, place, class_name))

    def study(self,name, place):
        print("{}在{}自习".format(name, place))
if __name__ == "__main__":
    # 小明的一天
    student_name = "小明"
    student = Student()
    print(" ======{}的一天======".format(student_name))
    student.eat(student_name, "食堂")
    student.gotoclass(student_name, "一教", "Python")
    student.dosport(student_name, "操场", "打篮球")
    student.study(student_name, "图书馆")
    student.sleep(student_name, "2号楼")