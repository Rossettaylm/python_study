import re

# sub方法可以修改文本
content = '37au68yy58ds'
content = re.sub('\d+', '', content)  # 删掉文本中的数字
print(content)

html = '''<div id="songs-list">
<h2 class>="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

html = re.sub('<a.*?>|</a>', '', html)  # 先删除a节点只留下文本
results = re.findall('<li.*?>(.*?)</li>', html, re.S)  # 利用findall提取简化正则表达式
for result in results:
    print(result.strip())
