import jieba
filename = "三国演义.txt"

f = open(filename,'r',encoding='utf-8')
txt = f.read()
words = jieba.lcut(txt)

# 定义字典存放词数
counts = {}
for word in words:
    # 排除单个字符的分词结果
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0)+1

# 讲字典转换为列表进行统计排序
items = list(counts.items())

# 按照列表第一列排序
count = 0

items.sort(key=lambda k:k[1],reverse=True)

for i in range(len(items)):
    word , count = items[i]
    print("{}===={}".format(word,count))

# print(txt)
