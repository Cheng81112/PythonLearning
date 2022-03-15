'''
编写程序，从键盘输入语文、数学、英语三门功课的成绩，
计算并输出平均成绩，
要求平均成绩小数点后保留1位。
'''

chinese = float(input("请输入您的语文成绩："))
math = float(input("请输入您的数学成绩："))
english = float(input("请输入您的英语成绩："))

average = (chinese + math + english)/3

print("您的平均成绩为：{:.1f}" .format(average))
