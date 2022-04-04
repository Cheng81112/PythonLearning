'''
利用python的print()函数写一篇作文
要求必须覆盖以下列表操作
1.索引2.切片3.序列相加4.序列乘法5.成员资格6.长度7.最大值8.最小值9.计数10.修改11.增加12.删除13.排序
评分标准：文字优美，包含知识点越多越好
举例：记一次有趣的生日派对
今天，是我的生日。
我在一个星期前就和我的好朋友们说好了，让他们来我家参加我的生日派对。
我的好朋友有{}个，第1个好朋友是{}，第2个好朋友是{}，剩下的好朋友们是{}。
当然，如果按名字排序的话，那就是{}了。
但是，昨天，{}告诉我说，他不能来参加我的生日派对了，因为{}
那我只能把他从我的嘉宾名单中删除咯。现在，能来的就剩下这些{}了。
人数好像有些不够啊，那我再叫一些人来吧。对了，把{}和{}给叫过来好了，这些的话，就有这些人来了{}。
'''


print("记一次有趣的生日会")
friend = ["Lily","Lucy","Bob","Tom","Jerry","John","Kity"]
print("今天，是我的生日。")
print("我在一个星期前就和我的好朋友们说好了，让他们来我家参加我的生日派对。")
count_friend = len(friend)
print("我有{}个好朋友,第一个好朋友是{}，第二给好朋友是{}，剩下的好朋友分别是{}。".format(count_friend,friend[0],friend[1],friend[2:]))
# friend.sort()
print("当然，如果按名字排序的话，那就是{}了。".format(sorted(friend))) # 临时排序


print("但是，昨天，{}告诉我说，他不能来参加我的生日派对了，因为排名最靠前的{}把他踢出了邀请名单。".format(friend[1],max(friend)))

del friend[1]

print("那我只能把他从我的嘉宾名单中删除咯。现在，能来的就剩下这些{}了。".format(friend))

friend1 = ["Dage","Xiaodi"]
friend2 = ["Zhangsan","Lisi"]
print(friend1 in friend)
print(friend2 in friend)

print("人数好像有些不够啊，那我再叫一些人来吧。对了，把{}和{}给叫过来好了，这些的话，就有这些人来了{}。".format(friend1,friend2,friend+friend1+friend2))





