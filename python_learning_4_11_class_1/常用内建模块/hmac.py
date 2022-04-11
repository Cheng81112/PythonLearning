'''
hamc模块
'''
import hmac
message = b'Hello,world!'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())

# hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。
# 需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
