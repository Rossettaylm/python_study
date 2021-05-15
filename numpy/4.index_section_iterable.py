#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import numpy as np

a = np.arange(10) ** 3
print(a)
print('a[2] = ', a[2])
print('a[2:5] = ', a[2:5])
a[:6:2] = -1000
print(a)  # equivalent to a[0:6:2]=-1000, from start to
# positon 6, exclusive, set every 2nd element to -1000

print(a[::-1])  # reverse a

for i in a:
    print(i ** (1/3.))


# 切片表示
print('\n')


def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int) # 按函数f生成shape=（5,4）的数组
print('\nb = ', b)
print(b[2, 3])
print(b[0:5, 1])  # 第0-4行，1列
print(b[1:3, :])  # 第1-2行，所有列
print(b[:3, :3])  # 前三行，前三列
# 下列三种方式表示同一种情况：缺失的索引被认为是完整的切片
print(b[-1], b[-1, :], b[-1, ...])


# 对多维数组进行迭代(iterating)时对于第一个轴完成的，即row
print('\n')
for row in b:
    print(row)

# 对数组中的每个元素执行操作，使用flat属性,是数组内所有元素的迭代器
print('\n')
for element in b.flat:
    print(element)

