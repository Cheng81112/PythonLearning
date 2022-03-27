'''
读入score.txt文件，统计每个年级的平均成绩
'''

filename = 'score.txt'
f = open(filename, 'r', encoding='utf-8')
title = f.readline()
course_name1 = title[3:7]
course_name2 = title[-8:-4]

count_class2 = 0
count_class3 = 0
class2_sum_score1 = 0
class2_sum_score2 = 0
class3_sum_score1 = 0
class3_sum_score2 = 0
class2_avg_score1 = 0
class2_avg_score2 = 0
class3_avg_score1 = 0
class3_avg_score2 = 0

for line in f.readlines()[0:]:
    line = line.replace('\n','')
    class_num = int(line[-1:])
    if class_num == 2:
        count_class2 += 1
        class2_score1 = int(line[-7:-5])
        class2_score2 = int(line[-4:-2])
        class2_sum_score1 += class2_score1
        class2_sum_score2 += class2_score2
        class2_avg_score1 = class2_sum_score1 / count_class2
        class2_avg_score2 = class2_sum_score2 / count_class2
    else:
        count_class3 += 1
        class3_score1 = int(line[-7:-5])
        class3_score2 = int(line[-4:-2])
        class3_sum_score1 += class3_score1
        class3_sum_score2 += class3_score2
        class3_avg_score1 = class3_sum_score1 / count_class3
        class3_avg_score2 = class3_sum_score2 / count_class3
print("年级2的{}的平均成绩为：{:.2f}".format(course_name1, class2_avg_score1))
print("年级2的{}的平均成绩为：{:.2f}".format(course_name2, class2_avg_score2))
print("年级3的{}的平均成绩为：{:.2f}".format(course_name1, class3_avg_score1))
print("年级3的{}的平均成绩为：{:.2f}".format(course_name2, class3_avg_score2))
















