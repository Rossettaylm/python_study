#!/usr/bin/python3
# -*- coding: UTF-8 -*-
a = input().split(' ')
list_number = int(a[0])
list_move = int(a[1])
input_list = list(input().split(' '))

for value in range(list_move % list_number):
    input_list.insert(0, input_list[-1])
    input_list.pop()

for value in input_list:
    print(value, end=' ')
