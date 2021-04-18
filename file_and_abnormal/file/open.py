filename = 'test'
with open('test') as file_object:   #表示路径为./test, with函数表示返回的open（）对象只在with代码块内可用
    contents = file_object.read()
    print(contents.rstrip())

file_path = '/home/rossetta/python_works/file_operation/test'
#用变量表示绝对路径
with open(file_path) as file_object_abs:
    contents = file_object_abs.read()
    print(contents.rstrip())

#逐行读取
with open(file_path) as file_object_hang:
    for line in file_object_hang:   #自动按行遍历文本
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines() #.readlines()方法每读取一行则保存到列表
pi_string = ''
for line in lines:
    print(line.rstrip())
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
    
