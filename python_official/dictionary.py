#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# (1) 关键字可以使字符串， 数字或不包含可变对象的元祖
tel = {
    'jack': 4098,
    'sape': 4139
}
tel['guido'] = 4127
print(tel)
del tel['sape']
print(tel)

# (2) 将字典存储为列表， 默认存储其键
tel['irv'] = 4127
tel_list = list(tel)
print(sorted(tel_list))

# (3) dict() 可以直接用键值对序列创造字典
dic = dict([('queshi', 4444), ('niubi', 3333)])
print(dic)

# (4) 列表解析for字典
dic = {str(x): x**2 for x in range(3)}
print(dic)
