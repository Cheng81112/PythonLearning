'''
itertool提供非常有用的英语操作迭代对象的函数

'''
import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 10:
        break

cs = itertools.cycle("ABC")
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break
a = itertools.repeat('A',3)
for n in a:
    print(n)

ns = itertools.chain("ABC","XYZ")
for ns in itertools.chain(ns):
    print(ns)

# takenwhile()根据条件判断来截取出一个有限序列
s = itertools.count(1)
s = itertools.takewhile(lambda x: x <= 10, s)
print(list(s))


for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))