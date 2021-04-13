#while循环方便遍历列表并同时进行修改

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title() + "...")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)
    
#删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#使用用户输入来填充字典
responses = {}
active = True   #设置一个标志
prompt = "Would you like to let another person respond?(yes/no) "
while active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response      #name代表的是输入的字符串变量，不需要加''
    repeat = input(prompt)
    while repeat != 'yes' and repeat != 'no':
        repeat = input(prompt)
    if repeat == 'no':
        active = False
print(responses)

print("\n--- Poll Result ---")
for name,response in responses.items():
    print(name.title() + " would like to climb " + response.title() + '.')
