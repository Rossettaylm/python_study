# python标准库模块的导入
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'java'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())
