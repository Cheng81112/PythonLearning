'''
统计字符出现次数
统计“山”出现次数
'''
word = "山羊上山山上碰见山羊"
sum = 0
for letter in word:
    if letter == "山":
        sum += 1
print(sum)



