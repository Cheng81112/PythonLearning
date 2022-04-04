'''
处理每行的内容
根据分隔符进行分割，返回值为列表

'''
filename = "wordcount.txt"
f = open(filename,'r')

for line1 in f.readlines():
    newline1 = line1.rstrip()
    newline2 =newline1.split(",")
    print(newline2)

f.close()
