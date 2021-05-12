#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import numpy as np 

a = np.arange(10) ** 3 
print(a)
print('a[2] = ', a[2])
print('a[2:5] = ', a[2:5])
a[:6:2] = -1000
print(a)  # equivalent to a[0:6:2]=-1000, from start to 
#positon 6, exclusive, set every 2nd element to -1000

print(a[ : :-1])  # reverse a

for i in a:
    print(i ** (1/3.))



print('\n')
def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
print(b[2, 3])
print(b[0:5], 1)    #第0-4行，1列
print(b[1:3, : ])    #第1-2行，所有列

