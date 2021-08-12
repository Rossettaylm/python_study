import http.cookiejar
import urllib.request

# 生成cookies文件
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)

# 生成cookies并保存
filename = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)  # 或LWPCookieJar格式的cookie
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 从文件中读取并利用
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookies.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))
