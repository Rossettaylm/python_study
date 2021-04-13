def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()    #返回一个字符串
fullname = get_formatted_name('jimi', 'hendrix')
print(fullname)

#可选实参--赋予空的默认字符串并放在最后
def getformattedname(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
fullname = getformattedname('walt','white')
print(fullname)
fullname = getformattedname('walt','white','junior')
print(fullname)

#返回list/dictionary
def build_person(first_name, last_name, age = ''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age = 27)
print(musician)

#结合函数和while循环
while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' anytime if you want to quit.")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    fullname = get_formatted_name(f_name,l_name)
    print("\nHello! " + fullname + '.')
