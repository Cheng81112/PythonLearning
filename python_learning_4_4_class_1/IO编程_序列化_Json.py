'''

'''
import json
# Python对象变成一个JSON
# dumps()方法返回一个str，内容就是标准的JSON
# s = dict(name='Bob', age=20, score=88)
# print(json.dumps(s))

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，
# 后者从file-like Object中读取字符串并反序列化
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str))



d = dict(name='Bob', age=20, score=88)
# 序列化为json
data = json.dumps(d)
print('JSON Data is a str:', data)
# 反序列化
reborn = json.loads(data)
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)

std_data = json.dumps(s, default=lambda obj: obj.__dict__)

print('Dump Student:', std_data)

rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)