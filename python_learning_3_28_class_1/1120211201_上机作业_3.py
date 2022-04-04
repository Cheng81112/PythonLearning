"""
3.姓名缘分。
•	输入：你的姓名，恋人姓名
•	输出：缘分情况
分值	缘分情况
[0,60)	萍水相逢
[60,70)	点赞之交
[70,80)	点头之交
[80,90)	无话不谈
[90,100)	最佳闺蜜
100	赶快结婚

"""
import random
randomSeed = 0
maleName = input("男方姓名>>:")
femaleName = input("女方姓名>>:")
for everyChar in maleName:
    randomSeed += ord(everyChar)
for everyChar in femaleName:
    randomSeed += ord(everyChar)
random.seed(randomSeed-1000)
score = random.randint(0,100)
if score in range(60):
    print("萍水相逢")
elif score in range(60,70):
    print("点赞之交")
elif score in range(70,80):
    print("点头之交")
elif score in range(80,90):
    print("无话不谈")
elif score in range(90,100):
    print("最佳闺蜜")
else:
    print("赶快结婚")
