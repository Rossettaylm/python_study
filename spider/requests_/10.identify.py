import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1

# r = requests.get('http://localhost:5000',
#                  auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)

# 使用OAuth1认证
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)
