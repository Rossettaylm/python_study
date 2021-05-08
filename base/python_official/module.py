#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys


# Fibonacci numbers module
# (1) 作导入模块使用
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# python module.py 50
# >>> 0 1 1 2 3 5 8 13 21 34
# if __name__ == "__main__":
#    import sys
#    fib(int(sys.argv[1]))


# (2) 模块搜索路径
# first: 内置模块  >>>  second: sys.path变量中的目录列表
# sys.path 包含：
# 1 输入脚本的目录（当前目录）
# 2 PYTHONPATH
# 3 默认安装目录


print(sys.path)
