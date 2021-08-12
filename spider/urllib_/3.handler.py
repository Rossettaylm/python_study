from urllib.error import URLError
from urllib.request import (HTTPBasicAuthHandler,
                            HTTPPasswordMgrWithDefaultRealm, build_opener)

username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)  # 处理验证的Handler
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)  # 发送请求相当于验证成功

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
