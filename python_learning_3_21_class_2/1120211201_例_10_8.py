'''
将数据写入文件 w操作
f.write(string)
将字符串string的内容写到新文件f对应的文件中
'''

filename = "students.txt"
f = open(filename,'w')

f.write("5,")
f.write("Alice")
f.write("\n")
f.write("6,Bob\n")

f.close()
