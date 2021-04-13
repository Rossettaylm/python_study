def make_shirt(size,word = 'I love python'):
    print("\nThe T-shirt's size is " + size.upper() + ".")
    print("These words would be print: " + word.title())

make_shirt('l')
make_shirt('m')
make_shirt('l', 'nashizhendeniubi')


def describe_city(city_name, country = 'Iceland'):
    print('\n' + city_name.title() + " is in " + country.title() + ".")
describe_city('reykjavik')
describe_city('jiangle', 'china')
describe_city(city_name = 'xian', country = 'china')


