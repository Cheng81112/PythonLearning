'''
将数据写入文件 a操作
f.write(string)
将字符串string的内容追加写到新文件f对应的文件中
'''
filename = "students.txt"
f = open(filename,'a')
f.write("4,Candy\n")
f.close()
