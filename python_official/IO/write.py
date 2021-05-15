#!/usr/bin/python3
# -*- coding: UTF-8 -*-
filename = 'workfile'
lines = ['azhe', 'keyi']
with open(filename, 'w') as f:
    print(f.writable())
    f.write('queshi\nrossetta\nyangliaoming\n')
