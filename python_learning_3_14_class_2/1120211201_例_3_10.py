'''
打十次游戏
'''

import random
games=10
for i in range(games):
    print("进行第{}次游戏" .format(i+1))
    result = random.randint(0,1)
    if result == 1:# 获胜
        print("朋友圈炫耀")
    else:# result == 0 失败
        print("沉默、")
    print("*"*20)

