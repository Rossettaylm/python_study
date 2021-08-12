import requests

data = {
    'name': 'germey',
    'age': 22
}

r = requests.get('http://httpbin.org/get', params=data)
# 返回的r.text是字符串类型的数据，json方法将其转变为字典
print(type(r.text))
print(r.json())
print(type(r.json()))
