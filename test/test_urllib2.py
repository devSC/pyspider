#coding:utf8

from urllib import request
from http import cookiejar


url = 'http://baike.baidu.com/item/Python'

print('第一种方法:')
response1 = request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))



print('第二种方法(添加 user-agent 模拟真实用户): ')
requester = request.Request(url)
requester.add_header('user-agent', 'Mozilla/5.0')
response2 = request.urlopen(requester)
print(response2.getcode())
print(len(response2.read()))


print('第三种方法(添加Cookie处理):')
cj = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())
