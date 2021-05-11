#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import numpy as np
from numpy import pi

#  (1) 算术运算
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a - b
print('a = ', a)
print('b = ', b)
print('a - b = ', c)
print('b ** 2 = ', b ** 2)
print('10 * sin(a) = ', 10 * np.sin(a))

#  (2) 矩阵乘积用@或者dot函数或方法执行
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print('\n')
print('elementwise product = ', A * B)
print('matrix product = ', A @ B)
print('or matrix product = ', A.dot(B))

# (3) += , *= 操作直接更改被操作的数组，不会创建新数组
print('\n')
a = np.ones((2, 3), dtype=int)
b = np.random.random((2, 3))

print(a)
a *= 3
print(a)

print(b)
b += a
print(b)

# (4) 当使用不同类型的数组进行操作时，结果数组的类型对应于更精确的数组（称为向上转换的行为）
print('\n')
a = np.ones((2, 3), dtype=np.int32)
b = np.linspace(0, pi, 3)
c = a + b
print(c)
print(c.dtype)
d = np.exp(c * 1j)  # 以e为底的指数运算
print(d)
print(d.dtype)

# (5) ndarray的一元操作, 通过指定axis参数，可以沿指定轴操作
a = np.random.random((2, 3))
print('\nrandom(2, 3) = ', a)
print('sum = ', a.sum())
print('min = ', a.min())
print('max = ', a.max())
b = np.arange(12).reshape(3, 4)
print('\nrange(12).reshape(2, 3) = ', b)
# sum of each column, first axis
print('\nsum of each column = ', b.sum(axis=0))
print('\nmin of each row', b.min(axis=1))  # min of each row, second axis
print('\ncumulative sum of each row = ', b.cumsum(
    axis=1))  # cumulative sum along each row
