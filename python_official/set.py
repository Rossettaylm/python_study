#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 集合是由不重复元素构成的无序容器
# (1) 创建集合用{}或者set（）函数， 创建空集合只能用set

basket = {'apple', 'orange', 'apple', 'pear', 'orange'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)
for i in sorted(basket):
    print(i)

a = set('abracadabra')
b = set('alacazam')
# a ^ b : letters in a or b but not both
print(a, b, a - b, a | b, a & b, a ^ b)

# (2) 推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print('\n', a)
