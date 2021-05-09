#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 1.read
# mode = ('r', 'w', 'r+', 'a', 'rb',....)
# 'b' 表示以binary mode打开文件，此时，数据以(字节)方式读写,适用于所有不包含文本的文件
# ！！！JPEG、exe等文件一定要用'b'模式读写
# (1)f.read(size)方法
size = 8
filename = 'workfile'
with open('workfile') as f:
    read_data = f.read(size)  # size个字符或者size个字节
    print(read_data)
    read_data2 = f.read(size)
    print(read_data2)       # 接续read

with open('workfile') as f:
    read_line = f.readline()  # 读取单行，字符串末尾保留'\n'
    # 若readline返回空字符串，证明到达文件末尾

# (2)文件中读取多行时，可以用循环遍历整个文件对象。
with open(filename) as f:
    for line in f:
        print(line, end='')  # 每行结尾自带换行符，不需要print换行

# (3)以列表方式读取文件中的所有行
with open(filename) as f:
    a = list(f)
    print(a)

with open(filename) as f:
    a = f.readlines()
    print(a)


# 2.write
# (1) f.write(string),返回写入的字符数,需先将写入值转为字符串或者字节对象
value = ('the answer', 42)
s = str(value)
with open(filename, 'r+') as f:
    f.write(s)

# (2) f.tell(), f.seek(offset, whence)
# f.tell() 返回整数，给出文件对象在文件中的当前位置，表示为二进制模式下时从文件开始的字节数，以及文本模式下的意义不明的数字。
#
# f.seek(offset, whence) 可以改变文件对象的位置。通过向参考点添加 offset 计算位置, seek后位置为当前位置+offset；参考点由 whence 参数指定。 whence 值为 0 时，表示从文件开头计算，1 表示使用当前文件位置，2 表示使用文件末尾作为参考点。省略 whence 时，其默认值为 0，即使用文件开头作为参考点。
# 在文本文件（模式字符串未使用 b 时打开的文件）中，只允许相对于文件开头搜索（使用 seek(0, 2) 搜索到文件末尾是个例外），唯一有效的 offset 值是能从 f.tell() 中返回的，或 0。其他 offset 值都会产生未定义的行为, 例如f.seek(-2, 2)报错。
