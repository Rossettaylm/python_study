import json

filename = 'num.json'
def get_stored_number():
    try:
        with open(filename) as file_obj:
            favorite_num = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_num

def get_new_number():
    with open(filename, 'w') as file_obj:
        while True:
            try:
                favorite_num = input("What is your favorite number? ")
                favorite_num = int(favorite_num)
            except ValueError:
                print("It's not a number.")
            else:
                json.dump(favorite_num, file_obj)
                break
    return favorite_num

def remember_num():
    favorite_num = get_stored_number()
    if favorite_num:
        print("I know your favorite number! It's " + str(favorite_num) + ".")
    else:
        favorite_num = get_new_number()
        print("I will remember your favorite number.")

remember_num()

