'''
自然数之和（for+range）
编写程序，使用for语句计算1～10000的自然数之和。
'''

total = 0
for iNum in range(1,101):
    total += iNum
print("1~10001的总和为：{}" .format(total))
