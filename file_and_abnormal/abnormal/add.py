# 当输入不是数字时提示TypeError
print("Input a 'q' anytime if you want to exit.")
while True:
    try:
        a = input("Please input first number: ")
        if a == 'q':
            break
        b = input("Please input another number: ")
        if b == 'q':
            break
        a = int(a)
        b = int(b)
    except ValueError:
        print("It's a text, please input a number.")
    else:
        sum = a + b
        print("The sum is " + str(sum) + ".")
    
