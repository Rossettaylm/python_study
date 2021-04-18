print("Please input some numbers you want to add, input 'q' to exit.")
sum = 0
while True:
    try:
        num = input("Please a number or 'q': ")
        if num == 'q':
            break
        else:
            sum += int(num)
    except ValueError:
        print("It's a text, please input a number.")

print("The sum is " + str(sum) + ".")
