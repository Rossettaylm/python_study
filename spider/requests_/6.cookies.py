import requests

# r = requests.get("https://www.baidu.com")
# print(r.cookies)

# for key, value in r.cookies.items():
#     print(key + '=' + value)

headers = {
    'Cookie': '_zap=38344c92-a63e-4731-9778-51ddd3595728; d_c0="AGBaUUKbwBKPTht4LGRbirJans-a9nepV7o=|1614943247"; __snaker__id=xdgCVqT3yaqlZKdp; gdxidpyhxdE=udsa4C6krOucVzdadhfLWht/7fVmveoyNn+nVT1izjwkZ+Z0P3+kMBb30Q71xfeh41y78WtNP3+IE8DjHwfYbJ4EvrO1IyEOyHTxhsh\pNe0vnmQsl1r7BGkLfuxssTzGkpPT4w9sxCCtz0ox/7ZEBAwf+9O6/gvrHlL17QYXYeBu3yS:1620736733648; _9755xjdesxxd_=32; YD00517437729195:WM_NI=i5lBPP+jxMLg/S+ohOuBhHf+AvRvPA/m4PPbdU6tHG05cOPYTy5V9JjNmODQljY/0R5aEEn5GBwTbWoSu2Py7xLsXIhH43q5NXZHQQusZYPpaRo2JjvIrfLHP/cJZ+U7UnE=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eebbd54893f5bb87e53a9cb08eb6c85e839b8ebbf13bbbbb8182d46494befbabbb2af0fea7c3b92aabeba4a3d35ce9b6b8aecf6ded8de590eb45b79ea8a9e52183aa9e97d34bedb3fcb1d36aa88bfa95cb4df4ebadb0d35398a7fbb7bc42aa92a3b0c75bb0b697d0b35af7bf8ba6ed3f859eb9b5e15dad8dbbd3d373f5a88494db43ac98fcd4f43f8e8896a9d45bb7ad96bad37ca38ea1d3c962b697be87cf4494f1adabd92197e99b8fc837e2a3; YD00517437729195:WM_TID=a8J/rbaZqyJEUEUQBEd+1zKPPFkbapY8; z_c0=Mi4xczU2SkNnQUFBQUFBWUZwUlFwdkFFaGNBQUFCaEFsVk5kTVdIWVFDaVp1T3YxYmM0S2xWbWtnNUoxNk56QlBKZG1n|1620735860|da3f7171191d7f10fb7279b93ecff159f8216d46; _xsrf=edd85de0-1cfc-4234-b7cd-3cdd18b1e142; tst=r; KLBRSID=fb3eda1aa35a9ed9f88f346a7a3ebe83|1628585093|1628583529; SESSIONID=fqFsCMgCXbsH6LupHwiVFdh2gwJaLqO8j5KVx16nRGW',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
