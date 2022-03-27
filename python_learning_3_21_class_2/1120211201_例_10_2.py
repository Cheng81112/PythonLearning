'''
读入一行文本内容，返回结果为一个字符串
'''
filename = "wordcount.txt"
f = open(filename,'r')
content = f.readline()
print(content)
f.close()
