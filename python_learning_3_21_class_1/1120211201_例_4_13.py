'''在列表中添加元素'''

friend_list = ["马云","马化腾","王健林","李彦宏"]

print("=========2022年生日=============")
for friend in friend_list:
    print("{}，好哥们，谢谢你来帮我过生日" .format(friend))

print()

print("=========2021年生日================")

friend_list.insert(0,"许家印")
print(friend_list)
for friend in friend_list:
    print("{}，好哥们，谢谢你来帮我过生日" .format(friend))