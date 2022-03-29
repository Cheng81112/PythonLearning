'''
星座运势
使用函数实现一个“星座今日运势”程序。实现输入“星座”，返回五大运势的得分（0~5）。
•	输入：星座，年，月，日
•	输出：
•	整体运势：{}
•	爱情运势：{}
•	事业运势：{}
•	财富运势：{}
•	健康运势：{}
提示：将星座，年，月，日转化为随机数的seed
'''

import random

def jinriyunshi(xingzuo,year, month, day):
    count = year * 11 + month * 7 + day * 5
    for C in xingzuo:
        count += ord(C)
    random.seed(count)
    a = random.randint(1,5)
    b = random.randint(1,5)
    c = random.randint(1,5)
    d = random.randint(1,5)
    e = random.randint(1,5)
    print(a, b, c, d, e)
    return a, b, c, d, e

while True:
    xingzuo = input("请输入您的星座:")
    a,b,c,d,e = jinriyunshi(xingzuo, 2018, 4, 26)
    print("星座: {}" .format(xingzuo))
    print("整体运势: {}".format('*'*a))
    print("爱情运势: {}".format('*'*b))
    print("事业运势: {}".format('*'*c))
    print("财富运势: {}".format('*'*d))
    print("健康运势: {}".format('*'*e))






# # 只要固定seed函数的参数，随机函数的结果也固定
# count = 100
# for i in range  (10):
#     random.seed(count)
#     a = random.randint(1,5)
#     b = random.randint(1,5)
#     c = random.randint(1,5)
#     d = random.randint(1,5)
#     e = random.randint(1,5)
#
# print("a:{},b{},c{},d{},e{}".format(a,b,c,d,e))

