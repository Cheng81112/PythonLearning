'''
学生名单
编程实现
读入学生名单保存为字典
并实现输入学生学号，返回学生姓名

'''

filename = "students.txt"
student_dict = {}

# 读取学生名单，并保存在字典student_dict中
# 取其key为学生学号，value为学生姓名

f = open(filename,'r',encoding='utf-8')
for line1 in f.readlines():
    newline1 = line1.rstrip()
    newwords = newline1.split(",")
    sid,sname = newwords
    student_dict[sid] = sname

f.close()

# 实现输入学生学号，返回学生姓名

while True:
    newsid = input("请输入学号：")
    if newsid in student_dict:
        print("学生姓名为：{}".format(student_dict[newsid]))
    else:
        print("该学号不存在")