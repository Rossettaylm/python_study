import requests

# 上传文件要以字典形式传入
filepath = 'requests_/favicon.ico'
files = {'file': open(filepath, 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)
