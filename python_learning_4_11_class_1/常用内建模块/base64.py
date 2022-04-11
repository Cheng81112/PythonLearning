'''
二进制到字符串的转换方法
base64适用于小段内容的编码，比如数字证书签名、Cookie内容等
常用于再URL、Cookie、网页中传输少量二进制数据
'''
import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)