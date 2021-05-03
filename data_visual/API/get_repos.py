import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()
repo_dicts = response_dict['items']

filename = 'repos.data'
with open(filename, 'w') as f:
    for repo_dict in repo_dicts:
        f.write('\nName:')
        f.write(repo_dict['name'])
        f.write('\n')
        f.write('Repository:')
        f.write(repo_dict['html_url'])
        f.write('\n')
    
