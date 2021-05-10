#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# (1) 循环技巧
import math

dic = dict([('queshi', 4444), ('niubi', 3333), ('azhe', 11)])
for key, value in dic.items():
    pass

for key in dic.keys():
    pass

for value in dic.values():
    pass

for index, key in enumerate(dic):
    print(index, key)

for index, value in enumerate(list(range(10))):
    pass

# (2) 同时循环两个或多个序列时， 用zip（）可一一匹配
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
# 见tuple.py 中 x, y, z = t
for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}.".format(q, a))


# (3) 利用函数改变循环顺序
print('\n')
basket = ['apple', 'orange', 'apple', 'pear',
          'orange', 'banana']
for i in sorted(basket):
    print(i)

print('\n')
for i in sorted(set(basket)):
    print(i)


# (4) 在循环中修改列表的内容时，创建新列表比较简单安全
raw_data = [56.2, float('NaN'), 51.7, 55.3,
            52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    # isnan()测试是否为非数值,若是非数则为真
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

# (5) 循环中比较的关键字
# 1.比较运算符优先级一样且低于数值运算符
# in / not in
# is / is not

# 2.逻辑比较运算符优先级低于比较运算符
# and / or / not  其中优先级not > and > or
# a and not b or c == (a and (not b)) or c
