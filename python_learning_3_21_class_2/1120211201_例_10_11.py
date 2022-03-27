
'''
设计一个字典，对每个单词进行计数。
'''

filename = 'wordcount.txt'
f = open(filename,"r",encoding="utf-8")
content = f.read()# 读取文件内容，返回一个字符
content = content.lower()# 将字符串中所有的字母小写

for ch in [",",".",":"]:
    content = content.replace(ch," ")# 将文本中特殊字符替换为空格
words = content.split() #  不加参数，默认参数为按照空格和换行符进行分割

# print(words)
# print(len(words))
counts = {}  #定义空字典

# 计数
for word in words:
    counts[word] = counts.get(word , 0) + 1

# 排序

items = []

print(list(counts.items()))
items = list(counts.items())# 将字典转化为列表

items.sort(key=lambda x:x[1] , reverse = True)# 按照元素的第1列进行永久降序排列
for i in range(len(items)):
    word,count = items[i]
    print("{}==={}".format(word,count))









