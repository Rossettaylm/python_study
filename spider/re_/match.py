import re

# match()方法进行正则匹配, 从字符串的起始位置开始匹配, 一旦开头不匹配则整个匹配失败
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print('matched: ' + result.group())
print(result.span())

# 将需要匹配的子字符串用括号括起来，即(\d+)
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('Hello\s(\d+)\sWorld', content)
print()
print(result)
print('matched: ' + result.group())
print('matched substring: ' + result.group(1))  # 得到1234567
print(result.span())

# 通用匹配
# .* 表示匹配任意字符无限次（除了换行符）的贪婪匹配，即尽可能的匹配更多字符
# .*? 表示匹配任意字符无限次的非贪婪写法，即尽可能的匹配少的字符
# 尽可能的使用.*?非贪婪匹配来代替.*  以免出现匹配结果缺失
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print()
print(result)
print('matched: ' + result.group())
print(result.span())

# 贪婪匹配和非贪婪匹配的区别
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
result1 = re.match('^He.*?(\d+).*Demo$', content)
print()
print(result)
print('贪婪匹配: ' + result.group(1))
print('非贪婪匹配: ' + result1.group(1))

# 值得注意的是，在字符串结尾.*?可能会匹配不到内容
content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http://.*?comment/(.*?)', content)
result2 = re.match('http://.*?comment/(.*)', content)
print()
print('非贪婪匹配: ' + result1.group(1))
print('贪婪匹配:' + result2.group(1))

# re.S 修饰符，使.匹配到包括换行符在内的所有字符
content = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print()
print('修饰符匹配: ' + result.group(1))

# 转义匹配
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)  # 将特殊字符进行转义处理
print()
print(result)
print(result.group())
