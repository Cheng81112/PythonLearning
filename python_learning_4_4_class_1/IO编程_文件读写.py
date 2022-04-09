'''
文件读写
python内置open()函数，'r'读文件
如果文件不存在，抛出IOError错误
为保证是否出错都能正确关闭文件，使用try  finally来实现
后引入with语句自动调用close()方法


rb 二进制文件
open()函数传入encoding参数   字符串编码
w  f.write写文件
'''


# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()


# with open('/path/to/file', 'r') as f:
#     print(f.read())



from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)
