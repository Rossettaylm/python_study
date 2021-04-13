favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
        }
#遍历字典中的键和值
for key,value in favorite_languages.items():
    print("\n"+key.title()+" favorite language is "+value.title())

#遍历字典中的键
for key in favorite_languages.keys():
    print("\n"+key.title())

#遍历字典中的所有值
for value in set(favorite_languages.values()):  #set()集合--集合内的值不会重复      list()列表 
    print("\n"+value.title())

#遍历中的if条件判断
print("\n")
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is "
                + favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, Please take your poll!")

names = list(favorite_languages.keys())
print("\n")
print(names)

#对排序后的键进行遍历
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking this poll.")
