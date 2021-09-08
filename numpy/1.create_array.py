"""
create array
"""

from matplotlib import pyplot as plt

import numpy as np
from numpy import pi

a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.itemsize)
print(a.data)
print(a.size)
print(type(a))


# 数组创建
# (1) 用array从常规python列表或元组中创建
a = np.array([2, 3, 4])
b = np.array((1., 2.5, 3))
c = np.array([[1, 3, 4], [2., 3, 4], [3, 3, 3]])
d = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
              [[1, 2, 3], [2, 2, 2], [3, 3, 3]],
              [[1, 1, 1], [2, 2, 2], [3, 3, 3]]])
print('\n')
print(a)
print(b)
print(c)
print(d)
print(a.dtype, b.dtype, c.dtype, d.dtype)
print(a.ndim, b.ndim, c.ndim, d.ndim)

#  (2) 指定数组的类型
e = np.array([[1, 2], [3, 4]], dtype=complex)
print('\n')
print(e)

#  (3) 创建包含初始占位符的数组, 默认dtype为float64
a = np.zeros((3, 4))
b = np.ones((2, 3, 4), dtype=np.int16)
c = np.empty((2, 3))  # empty内容随机，取决于内存状态
print('\n')
print(a)
print(b)
print(c)
print(a.dtype, b.dtype, c.dtype)

# (4) arange函数，返回数组而不是列表
a = np.arange(10, 30, 5)
b = np.arange(0, 2, 0.3)
print('\n')
print(a)
print(b)
print(a.reshape(2, 2))

# (5) 当arange与浮点参数一起使用时，由于有限的浮点精度，通常不可能预测所获得的元素的数量。
# 出于这个原因，通常最好使用linspace函数来接收我们想要的元素数量的函数，而不是步长（step）
a = np.linspace(0, 2, 9)  # 9 numbers from 0 to 2, included 2
x = np.linspace(0, 2*pi, 100)
f = np.sin(x)
print('\n')
print(a)
plt.plot(x, f, linewidth=3, c='blue')
#  plt.show()


#  (6) array的打印
#  np.set_printoptions(threshold=sys.maxsize) # 设置全部打印不省略
print('\n')
print(np.arange(10000))
#  print(np.arange(10000).reshape(100, 100))
#  print(np.arange(10000).reshape(10, 10, 100))
#  print(np.arange(10000).reshape(10, 10, 10, 10))
