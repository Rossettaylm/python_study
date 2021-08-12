# 通过session可以做到模拟同一个会话而不用担心cookies的问题
# 常用于模拟登录成功后在进行下一步的操作
import requests

# 通过测试网址设置一个cookie，名称为number，内容是123456789
requests.get('http://httpbin.org/cookies/set/number/123456789')

# 请求cookies以获取先前设置好的cookies
r = requests.get('http://httpbin.org/cookies')
print(r.text)

# 发现cookies为空，因为需要用session保持会话

s = requests.session()  # 定义一个session类
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
