#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 更复杂的输出格式
# (1)用f'...{}'来格式化字符串
import math
year = 2016
event = 'Referendum'
print(f'\nResults of the {year} {event}')
# 冒号后输入整数，为该字段设置最小字符宽度，常用于列对齐
print(f'\nThe value of pi is approximately {math.pi:.3f}')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
print()
for name, phone in table.items():
    print(f'{name:10} >>> {phone:10d}')

# 以修饰符使在格式化前转换值
# '!a' 应用 ascii() ，'!s' 应用 str()，'!r' 应用 repr()
animals = 'eels'
print(f'\nMy hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}')


# (2)str.format()方法来格式化字符串
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('\n{:-9d} YES votes  {:2.2%}'.format(yes_votes, percentage))

# 1.位置参数
print('\n{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# 2.关键字参数--不用加''
print('This {food} is {adjective}.'.format(food='spam',
                                           adjective='absolutely horrible'))

# 3.字典参数
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# 其中位置参数0表示table
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# 解包字典
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# (3)把值转换为字符串
# 1.str() 适合人读取
# 2.repr() 适合机器读取
s = 'hello world.'
print()
print(str(s))
print(repr(s))


print()
# 格式化的几种方法
# 1.format
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))

print()
# 2.manual
# rjust(x)往左侧填充空格,向右对齐.同类方法还有ljust(),center().
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x**2).rjust(3), end=' ')
    print(repr(x**3).rjust(4))

# 补充zfill(), 在数字字符串左边填0,并能识别正负号
print('\n', '12'.zfill(5))
print('-3.14'.zfill(7))
