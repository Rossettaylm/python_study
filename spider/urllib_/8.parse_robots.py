# Robots协议也是爬虫协议，规定了哪些页面可以被爬虫抓取
# 一般情况网站会有robots.txt文件放在根目录下

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://jianshu.com/robots.txt')  # 或者直接将网址传入rp中
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch(useragent='*',
      url='http://www.jianshu.com/search?q=python&page=1&type=note'))
