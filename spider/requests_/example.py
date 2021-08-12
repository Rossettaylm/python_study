import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
print(type(r.content))


html = r.content
with open('requests_/test.html', 'wb') as f:
    f.write(html)
