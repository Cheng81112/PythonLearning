'''
python內建集和模块
'''

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)


# deque是为了高效实现插入和删除操作的双向列表适用于队列和栈

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以使用defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1']) # key存在
print('dd[\'key2\'] =', dd['key2']) # key2不存在，返回默认值

from collections import Counter
# counter是一个简单的计数器
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)

from collections import OrderedDict
# 使用dict时，Key是无序的。再对dict迭代时，我们无法确定Key的顺序。
d = dict([('a',1),('b',2),('c',3)]) # dict的Key是无序的
od = OrderedDict([('a',1),('b',2),('c',3)]) # OrderedDict的Key是有序的
print(d)
print(od)

