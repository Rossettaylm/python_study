import json

filename = 'username.json'
def get_stored_username():
    """如果存储了用户名，就获取它"""
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入新用户名"""
    username = input("What is your name? ")
    with open(filename, 'w') as file_obj:
        json.dump(username,file_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
