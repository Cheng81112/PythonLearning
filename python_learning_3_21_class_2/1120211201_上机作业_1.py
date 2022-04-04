'''
读入score.txt文件，统计每个班级一共多少人数
'''
filename = 'score.txt'

f = open(filename,'r',encoding='utf-8')
count = 0
for line in f.readlines()[1:]:
    newline = line.rstrip()
    count += 1
    print(newline)

print(count)



