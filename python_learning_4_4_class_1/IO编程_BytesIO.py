'''
StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：

请注意，写入的不是str，而是经过UTF-8编码的bytes。

和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
'''
from io import BytesIO

# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO:
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())

#
# import re
# from collections import Counter
#
# # r = re.match(r'\w*\d{3}\-\d{3,8}','a010-12345')
#
# # r = re.split(r's+','a d  c')
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
#
# c = Counter()
# for ch in 'programing':
#     c[ch] = c[ch] + 1
# 
# print(c)
#
# print(m)