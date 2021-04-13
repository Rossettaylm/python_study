filename = 'test'
# 注意！若test文件已经存在，write（）会先清空test内的数据
with open(filename, 'w') as file_object:
    #'w'表示以可写模式打开文件，且只能写入字符串
    file_object.write("Yangliaoming 17020310023.")

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.") #write（）并不会自动换行


filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n") #添加换行符来换行

filename = 'programming.txt'
with open(filename, 'a') as file_object:    # 'a'表示附加模式，到文章末尾
    file_object.write("I also love programming.\n")
    file_object.write("I also love creating apps that can run in a browser.\n") 

#'r+' 表示可读可写模式
