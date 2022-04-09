'''
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
'''

import pickle

d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)


# 写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 用pickle.load()方法从一个file-like Object中直接反序列化出对象

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

'''
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
'''