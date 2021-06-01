#!/usr/bin/python3
# -*- coding: UTF-8 -*-
class Dog:
    # 类属性
    kind = 'canine' # class variable shared by all instances

    def __init__(self, name):
        # 实例属性
        self.name = name # class variable need to input, 优先于类属性


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind, d.name)
print(e.kind, e.name)
