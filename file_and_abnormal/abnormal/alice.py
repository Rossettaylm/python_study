# try-except-else 结构
# 当try出现类型错误，执行except的内容，否则对try的结果进行else处理
def count_words(filename):
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        #pass
        #失败时什么都不做
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
                " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)
