#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Please execute 'python *.py n', n is up to you!

import numpy as np
import sys
from datetime import datetime


def pythonsum(n):
    a = [value ** 2 for value in range(n)]
    b = [value ** 3 for value in range(n)]
    c = []

    for i in range(n):
        c.append(a[i] + b[i])

    return c


def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c


size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("Pythonsum elapsed time in microseconds", delta.microseconds)

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print("\nThe last 2 elements of the sum", c[-2:])
print("Numpysum elapsed time in microseconds", delta.microseconds)
