#1.列表中嵌套字典
aliens = []
for alien_number in range(30):
    #new_alien = alien_0  无效--改变new_alien即改变alien
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens:
    print(alien)

#修改列表
print("\n")
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print("...")

#2.字典中嵌套列表
favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell']
        }

for name,languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite language is "
                +languages[0].title())

#3.字典中嵌套字典
users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
            },
        }

for username,userinfo in users.items():
    print("\nUsername:" + username.title())
    full_name = userinfo['first'].title() + ' ' +  userinfo['last'].title()
    location = userinfo['location'].title()
    print("\tFull name:" + full_name)
    print("\tLocation:" + location)

