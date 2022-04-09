'''
操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
'''

import os
# # 查看当前目录的绝对路径:
# os.path.abspath('.')
# '/Users/michael'
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# # 然后创建一个目录:
# os.mkdir('/Users/michael/testdir')
# # 删掉一个目录:
# os.rmdir('/Users/michael/testdir')

'''
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
'''

'''
编写一个程序，
能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
并打印出相对路径。
'''
from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
