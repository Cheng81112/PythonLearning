'''
读取全部文本内容
'''
filename = "wordcount.txt"
f = open(filename,'r')
content = f.read()
print(content)
f.close()
