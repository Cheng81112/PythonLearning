'''
读入全部文本内容，返回结果为一个列表
列表中每一个元素为一行文本字符串

'''

filename = "wordcount.txt"
f = open(filename,'r')
content = f.readlines()
print(content)
f.close()
