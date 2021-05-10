age = input("How old are you? ")
age = int(age)   #将input输入的字符串转换为int类型
if age > 18:
    print(age)

number = input("Please input a number: ")
number = int(number)
if number % 10 == 0:
    print("这个数是10的整数倍！")
else:
    print("这个数不是10的整数倍！")


