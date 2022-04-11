'''
摘要算法
摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，
不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
'''


import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())