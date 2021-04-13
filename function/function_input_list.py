# 函数传输变量为默认值，空，*（任意数量参数）时应该放最后面
#1.向函数传递列表
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#2.修改列表
print('\n')
def print_models(unprinted_designs, completed_models = []):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design + "...")
        completed_models.append(current_design)

def show_completed_models(completed_models = []):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#print_models(unprinted_designs[:], completed_models)
#传递unprinted_designs的切片，可以保持原列表不变


# 3.*toppings的星号让python创建一个空元组，并将所有的值都封装到这个元祖当中
print('\n')
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 4.**use_info 表示创建一个空字典，并将所收到的键-值对封装到这个字典
print("\n")
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location = 'princeton',
        field = 'physics')
print(user_profile)
