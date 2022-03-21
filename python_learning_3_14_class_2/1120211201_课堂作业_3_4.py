'''
编写程序，开发一个循环5次计算的小游戏，
每次随机产生两个100以内的数字，
让用户计算两个数字之和并输入结果，
如果计算结果正确则加一分，
如果计算结果错误则不加分。
如果正确率大于等于80%，则闯关成功
'''

'''
编写程序，开发一个循环5次计算的小游戏，
每次随机产生两个100以内的数字，
让用户计算两个数字之和并输入结果，
如果计算结果正确则加一分，
如果计算结果错误则不加分。
如果正确率大于等于80%，则闯关成功
'''
import random


times = 5

# a = num1 + num2

count = 0
for i in range(times):
    num1 = random.randint(1, 101)
    num2 = random.randint(1, 101)
    res = int(input("请输入{}和{}两个数之和:" .format(num1,num2)))
    if res == num1 + num2 :
        print("恭喜你答对一题，得一分")
        count += 1
    elif res != num1 + num2:
        print("很遗憾本题答错")
if count >= 4:
    print("恭喜你，正确率高于80%，闯关成功")
else:
    print("正确率低于80%，闯关失败，再接再厉。")




# import random


# times = 5

# num1 = random.randint(1,101)
# num2 = random.randint(1,101)

# a = num1 + num2
# print(a)
# count = 0 # 分数


# for i in range(times):
#     res = int(input("请输入您猜测的数字："))


#     if res > a:
#         print("您猜的结果偏大，请继续猜测")
#     elif res < a:
#         print("您猜的结果偏小，请继续猜测")

#     count += 1
#     print(count)
# if res == a and count <= 4:
#     print("恭喜你，正确率大于80%，得分为：{},闯关成功" .format(count))
# elif res == a and count == 5:
#     print("结果正确，得分为：{}".format(count))
# else:
#     print("五次机会用完，闯关失败")








