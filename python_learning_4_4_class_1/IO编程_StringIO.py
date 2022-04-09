'''
把str写入StringIO，需要先创建一个StringIO

'''

from io import StringIO


# 写入
s = StringIO()
s.write('hello')
s.write('')
s.write('world!')
print(s.getvalue())

# 读取
# 用一个str初始化StringIO，然后像文件读取
f = StringIO("Hello!\nHi!\nGoodbye!")
while True:
    a = f.readline()
    if a == '':
        break
    print(a.strip())
