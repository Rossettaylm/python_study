from random import randint

count = 0
while True:
    answer = input("\nwould you like to pick a random?  Enter 'q' anytime if you want to quit.")
    if answer == 'q':
        break
    else:
        x = randint(1,6)
        if x >= 4:
            print("Your number is big!")
        else:
            print("Your number is small! Good luck next time!")
    count += 1

print("The count is " + str(count))
