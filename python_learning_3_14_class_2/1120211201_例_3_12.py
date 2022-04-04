'''
猜颜色
编写程序，随机产生色子的一面（数字1～6），
给用户三次猜测机会，
程序给出猜测提示（偏大或偏小）。
如果某次猜测正确，则提示正确并中断循环；
如果三次均猜错，则提示机会用完
'''
import random
point = random.randint(1,7)
count=1
while count <= 3:
    guess = int(input("请输入您的猜测："))
    if guess>point:
        print("您猜测的太大了")
    elif guess<point:
        print("您猜测的偏小")
    else:
        print("恭喜你猜对了")
        break
    count += 1
else:
    print("很遗憾，三次全错了!")

