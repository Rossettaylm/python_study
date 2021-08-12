from urllib import parse, request

#response = request.urlopen('https://python.org')

data = bytes(parse.urlencode({'name': 'Rossetta'}), encoding='utf8')
response = request.urlopen('http://httpbin.org/post', data=data)

with open('record.txt', 'w') as f:
    f.write(response.read().decode('utf8'))
