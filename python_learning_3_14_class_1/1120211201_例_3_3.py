'''编写程序，从键盘输入年份，输出当年的年历'''

import calendar
year = int(input("请输入年份："))
table = calendar.calendar(year)
print(table)