from urllib.parse import (parse_qs, parse_qsl, quote, unquote, urlencode,
                          urljoin, urlparse, urlsplit, urlunparse, urlunsplit)

# 1.urlparse()方法
# 利用urlparse对一个URL进行解析，得到了ParseResult的对象
print('1.urlparse方法的使用:')
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

# http://www.baidu.com/index.html;user?id=5#comment
# 协议  //     域名     /  路径    ;参数 ?查询条件#锚点

# scheme参数只有在url中不包含协议时才生效
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

result = urlparse(
    'http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

# 返回的ParseResult对象实际上是一个元祖，我们可以用索引顺序来获取，也可以用属性名获取
result = urlparse('http://www.baidu.com/index.html#comment',
                  allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')


# 2.urlunparse()方法, 给定一个长度为6的可迭代对象参数，反解析成网址
print('\n2.urlunparse方法的使用:')
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
tupledata = ('http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment')
print(urlunparse(data))
print(urlunparse(tupledata))


# 3.urlsplit()方法, 不再单独解析params而是合并到path, 得到一个元组类型对象SplitResult
print('\n3.urlsplit方法的使用:')
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.scheme, result[0])


# 4.urlunsplit()方法，与urlunparse类似，长度为5
print('\n4.urlunsplit方法的使用:')
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))


# 5.urljoin(),可以提供一个base_url，和一个新链接。分析base_url的scheme、netloc、path
# 并对新链接缺失的部分进行补充, 且只补充这三个部分
print('\n5.urljoin方法的使用:')

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html',
      'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))


# 6.urlencode() , 常用于构造GET请求时
print('\n6.urlencode方法的使用:')
params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)


# 7.parse_qs()方法，即urlencode()的反序列化，将GET请求参数转回字典
print('\n7.parse_qs方法的使用:')
url = 'https://www.baidu.com/index.html?id=5&wd=germey&age=22'
result = urlparse(url)
print(result.query)
print(parse_qs(result.query))


# 8.parse_qsl()方法，将参数转化为元组组成的列表
print('\n8.parse_qs方法的使用:')
query = 'name=germey&age=22'
print(parse_qsl(query))


# 9.quote()方法，将内容转为URL编码的格式，防止中文乱码
print('\n9.quote方法的使用:')
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)


# 10.unquote()方法，进行URL解码
print('\n10.unquote方法的使用:')
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
