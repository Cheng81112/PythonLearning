# 作业2
'''
编写程序，从键盘输入一个年份值，
判断该年是否是闰年并输出判断结果。
（提示：若该年份值能被4整除且不能被100整除或者该年份值能被400整除，
则该年是闰年，否则不是）


'''
year = int(input("输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print("{0} 不是闰年".format(year))