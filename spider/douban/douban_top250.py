import json
import re
import time

import requests


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        return response.text


def parse_one_page(html):
    pattern = re.compile(
        '<li>.*?<em class="">(\d+)</em>.*?info">.*?title">(.*?)</span>.*?<p class="">.*?导演:(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>.*?(\d+)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\n.*?</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?content="10.0"></span>.*?<span>(\d+)人评价</span>.*?</div>', re.S
    )
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'title': item[1],
            'director': item[2],
            'actor': item[3],
            'release_time': item[4],
            'location': item[5],
            'label': item[6],
            'score': item[7],
            'users': item[8]
        }


def write_to_file(content):
    with open('douban/result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(start):
    url = 'https://movie.douban.com/top250?start='+str(start)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i * 25)
        time.sleep(1)
