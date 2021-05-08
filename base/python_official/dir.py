#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 内置函数 dir() 用于查找模块定义的名称。返回结果是经过排序的字符串列表

import matplotlib

print(dir(matplotlib))

# 注意，该函数列出所有类型的名称：变量、模块、函数等。
# 参数为空时，列出当前定义的所有名称。dir() 不会列出内置函数和变量的名称。
print(dir())
