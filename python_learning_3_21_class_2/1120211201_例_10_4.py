'''
for循环+文件
每次循环读取文件的一行
'''

filename = "wordcount.txt"
f = open(filename,'r')

for line1 in f.readlines():
    print(line1)

f.close()
