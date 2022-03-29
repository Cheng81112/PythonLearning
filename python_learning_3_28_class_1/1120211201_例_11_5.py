'''
多个返回值
'''

import random

def zhufuyu2():
    word_list= ["万事如意", "事事顺心", "福寿安康", "笑口常开", "恭喜发财", "步步高升", "笑口常开"]
    word1,word2 = random.sample(word_list,2)
    return word1,word2
zhufu1,zhufu2 = zhufuyu2()
print("过年好，祝您{}，{}".format(zhufu1,zhufu2))