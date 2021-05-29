#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# (1) 元组可以由多个逗号隔开的值组成
# 元组打包
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)

# 序列解包
x, y, z = t
print(x, y, z)
t = list(t)
print(t)
x, y, z = t
print(x, y, z)

# (2) 元组不支持直接赋值, tuple is immutable
# t[0] = 8888 is wrong

# (3) 构造0个或1个元素的元组, 后接逗号表示是单元素的元组
empty = ()
singleton = ('hello',)
print(len(empty), len(singleton))
print(empty, singleton)
