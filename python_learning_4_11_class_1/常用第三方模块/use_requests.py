'''
用requests获取URL资源
'''
import requests

import requests
r = requests.get('https://www.douban.com/') # 豆瓣首页
print(r.status_code)
print(r.text)
