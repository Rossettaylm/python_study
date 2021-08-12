import requests

url = 'https://www.taobao.com'
# timeout = (connect, read) => (5, 11)
r = requests.get(url, timeout=1)
print(r.status_code)
