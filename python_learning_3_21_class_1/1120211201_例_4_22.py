'''击鼓传花
击鼓传花，也称彩球。
中国民间游戏，流行于中国各地。数人、十数人或数十人围成一个圆圈席地而坐，
另外一个人背对着人圈以锤击鼓。鼓响时，开始传花，花游一个人手里传。
'''
import random

import time

player_list = ["Carol","David","Ann","Bob","Eve","Grace","Monica","Frank","Heidi","Judy"]
print("游戏开始，共有玩家{}个！".format(len(player_list)))
print("他们分别是:{}" .format(",".join(player_list)))
print("请大家按顺序占成一圈！")
player_list.sort()
print("ok, 排好序了。{}\n" .format(player_list))

count = 0
while ( len(player_list) > 1 ):
    count += 1
    print("第{}轮游戏开始，花在{}手上。" .format(count,player_list))
    print("开始击鼓咯！")
    bad_luck_bumber = random.randint(0,len(player_list)-1)

    print("咚"*bad_luck_bumber)
    bad_gay_name = player_list.pop(bad_luck_bumber)
    print("鼓声停了，一共敲了{}下，花到了{}手上，可怜的{}被淘汰啦！" .format(count,bad_gay_name,bad_gay_name))
    print("剩下{}名玩家，分别有：{}".format(len(player_list),player_list))
    time.sleep(3)
else:
    luck_guy_name = player_list.pop()
    print("最后的胜利者是{}，让我们恭喜他。".format(luck_guy_name))



