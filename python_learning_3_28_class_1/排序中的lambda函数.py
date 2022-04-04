'''
字典排序
'''

aaa_dict = {"a":100,"b":200,"c":120,"d":20}
print("字典为:{}" .format(aaa_dict))
# 字典转换为列表
aaa_list = list(aaa_dict.items())
print("字典转换为列表:{}" .format(aaa_list))

# 列表按照第1列排序
aaa_list.sort(key = lambda k:k[1], reverse = True)
print("列表按照第1列排序:{}".format(aaa_list))

# 列表按照第0列排序
aaa_list.sort(key = lambda k:k[0],reverse = True)
print("列表按照第0列排序:{}" .format(aaa_list))


