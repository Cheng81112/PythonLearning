'''
字典排序列子
首先准换为列表进行排序
'''



aaa_dict = {"a":100,"b":20,"c":120,"d":10}

print("字典为：{}".format(aaa_dict))

# 字典准换为列表
aaa_list = list(aaa_dict.items())

print("字典转换的列表为：{}".format(aaa_list))


# 按照列表第一列排序
aaa_list.sort(key=lambda k:k[1],reverse=True)
print("列表按照第1列排序结果为：{}".format(aaa_list))
# 按照列表第0列排序
aaa_list.sort(key=lambda k:k[0])

print("列表按照第0列排序结果为：{}".format(aaa_list))
