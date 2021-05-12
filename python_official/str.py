# (1) """......""" 表示连续跨行输入
#  \ 表示不需要回车换行，默认首行尾行回车换行
print("""
        name: yangliaoming
        school: xidian
        age: 21
        """)

print("""\
        name: yangliaoming
        school: xidian
        age: 21\
        """)

# (2) 字符串用×或者+都可以
print('\n' + 3 * 'niubi' + 'queshi')
# (3) 相邻字符串自动合并
print('\nPut several strings within parentheses '
      'to have them joined together')
# (4) 合并多个变量或合并变量与字符串，用'+'
prefix = 'Py'
print('\n' + prefix + 'thon')

# (5) 字符串支持索引, 切片, 但不能直接复制赋值
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
## -6  -5  -4  -3  -2  -1
word = 'Python'
print('\n' + word[0], word[-1])
print(word[0:2])  # included : excluded
print(word[2:5])
print(word[:2] + word[2:])  # word = word[:i] + word[i:]
print('J' + word[1:])


"""
File: str.py
Author: Rossetta
Email: 2441197035ylm@gmail.com
Github: https://github.com/Rossettaylm
Description: kaishijequeshi zheshiwod
"""
