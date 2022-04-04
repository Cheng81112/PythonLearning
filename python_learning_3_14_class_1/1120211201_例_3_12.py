'''
猜数字（random+分支）
编写程序，调用随机函数生成一个1～10之间的随机整数，
从键盘输入数字进行猜谜，
给出猜测结果（太大、太小、成功）的提示。
'''

import random
randnumber = random.randint(1,10)

guess = int(input("请输入您的猜测："))
print("随机数字为{}" .format(randnumber))

if guess > randnumber:
    print("您的猜测太大了")
elif guess <randnumber:
    print("您猜测的太小了")
else:
    print("恭喜你，猜对了")

# 方式一引用random库
import random

# 方式二引用random库
from random import random
from random import randint
from random import uniform

print("随机1个[0,1)的小数：{}" .format(random()))
print("随机1个[1,10)的整数：{}" .format(randint(1,10)))
print("随机1个[1,10)的小数：{}" .format(uniform(1,10)))



from random import * # 通过第二种方式引用第三方库

