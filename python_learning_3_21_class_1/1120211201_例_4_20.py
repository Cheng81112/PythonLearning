'''
一次input获得多个值
str.split(seq=None)
返回一个列表，由str根据seq被分割的部分构成
'''

student_names = input("请输入学生列表，用英文逗号（,）分割！:")
print(student_names)
student_list = student_names.split(",")
print(student_list)
