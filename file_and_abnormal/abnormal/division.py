#如果 try 代码块中的代码运行起来没有问题,Python将跳过 except 代码块;如果 try 代码块中的代码导致了错误
#Python将查找这样的 except 代码块,并运行其中的代码
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

