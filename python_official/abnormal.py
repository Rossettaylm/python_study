#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# (1)raise关键字
raise ValueError('niubi')

# (2)异常链


def func():
    raise IOError


try:
    func()
except IOError as exc:
    raise RuntimeError('Failed to open database') from exc

# (3) finally
try:
    raise KeyboardInterrupt
finally:
    print("helloworld!")
