import socket
from urllib import error, request

# URLError是error模块的基类，具有一个属性reason，返回错误的原因
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)


# HTTPError是URLError的子类，专门用来处理HTTP请求处理错误
# 属性：code、reason、headers
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print('\n')
    print(e.reason, e.code, e.headers, sep='\n')


# 因为URLError是HTTPError的父类，所以可以先选择捕获子类的错误，再去捕获父类的错误，所以上述代码更好的写法如下：
try:
    response = request.urlopen('https://www.baidu.com')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')


# reason属性返回的可能不是字符串而是一个对象
try:
    response = request.urlopen('https://www.baidu.com', timeout=0.01)
except error.URLError as e:
    print('\n')
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
