import re

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}

r = requests.get('https://www.zhihu.com/explore', headers=headers)
r.encoding = 'utf-8'
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

# r = requests.get('https://github.com/favicon.ico')
# with open('requests_/favicon.ico', 'wb') as f:
#     f.write(r.content)
