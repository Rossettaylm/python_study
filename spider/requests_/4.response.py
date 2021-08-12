import requests

r = requests.get('https://www.jianshu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)

if not r.status_code == requests.codes.ok:
    print('forbidden')
else:
    print('request successfully')
