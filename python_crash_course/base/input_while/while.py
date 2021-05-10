#在要求很多条件都满足才能继续运行的程序中，可以定义一个标志。当标志为True时，程序才能继续运行。
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you! "
prompt += "\nEnter 'quit' to end the program. "
message = ""
#while message != "quit":
    #message = input(prompt)
    #if message != 'quit':
        #print(message)

active = True    #标志
while active:
    message = input(prompt)
    if message == 'quit':
        #active = False
        break   #break直接退出整个循环
    else:
        print(message)

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue    #continue直接退出这次循环
    print(number)

