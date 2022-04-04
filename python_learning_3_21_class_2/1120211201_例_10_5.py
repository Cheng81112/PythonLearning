'''
处理每行的内容
'''
filename = "wordcount.txt"
f = open(filename,'r')


for line1 in f.readlines():
    newline1 = line1.rstrip()
    print(newline1)

f.close()
