import numpy as np

a = np.floor(10 * np.random.random((3, 4)))
print(a)
# a.shape() = (3, 4)

# 以下三种方法都不会改变a的形状
# (1)解成一维数组
print(a.ravel())

# (2)reshape形状, 将其中一个改成-1,则自动计算其size
print(a.reshape(6, 2))
print(a.reshape(3, -1))

# (3)转置矩阵
print(a.T)

# 修改数组本身的方法resize
print('\n')
a.resize((2, 6))
print(a)
