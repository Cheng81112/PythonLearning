'''使用pop方法删除元素，并获得该元素'''

friend_list = ["马云","马化腾","王健林","李彦宏"]

print("=========2022年生日=============")
print(friend_list)
print("=========2021年生日=============")
name1 = friend_list.pop()
print("{},再见！" .format(name1))
print(friend_list)

print("=========2020年生日================")

name2 = friend_list.pop()
print("{},再见！" .format(name2))
print(friend_list)