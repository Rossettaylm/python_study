# (1) 列表支持合并操作
cubes = [1, 4, 9]
cubes = cubes + [16, 25]
print(cubes)

# (2) 为切片赋值可以改变列表大小，甚至清空整个列表
letters = ['a', 'b', 'c', 'd']
print(len(letters))

letters[1:3] = ['B', 'C']  # replace
print(letters)

letters[1:3] = []  # delete
print(letters)

letters[:] = []  # clear
print(letters)

# (3) 关键字参数 end 可以取消输出后面的换行, 或用另一个字符串结尾
a, b = 0, 1
while a < 1000:
    if b < 1000:
        print(a, end=',')  # 取消换行改用逗号
    else:
        print(a)
    a, b = b, a + b
