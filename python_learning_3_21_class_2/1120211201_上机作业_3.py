'''
读入score.txt文件，统计每个班级的不及格人数
假设专业课1成绩低于80算不及格，专业课2成绩低于80算不及格
'''
filename = 'score.txt'
f = open(filename, 'r', encoding='utf-8')
class2_count1 = 0
class2_count2 = 0
class3_count1 = 0
class3_count2 = 0

for line in f.readlines()[1:]:
    line = line.replace('\n','')
    class_num = int(line[-1:])
    if class_num == 2:
        class2_score1 = int(line[-7:-5])
        class2_score2 = int(line[-4:-2])
        if class2_score1 < 80:
            class2_count1 += 1
        elif class2_score2 <80:
            class2_count2 += 1
        class2_count = class2_count1 + class2_count2
    elif class_num == 3:
        class3_score1 = int(line[-7:-5])
        class3_score2 = int(line[-4:-2])
        if class3_score1 < 80:
            class3_count1 += 1
        elif class3_score2 < 80:
            class3_count2 += 1
        class3_count = class3_count1 + class3_count2

print("年级2的不及格人数为：{}".format(class2_count))
print("年级3的不及格人数为：{}".format(class3_count))