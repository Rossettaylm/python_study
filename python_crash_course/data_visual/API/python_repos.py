import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import requests


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

# 状态码200表示请求成功
#print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()

# 处理结果
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

print(plot_dicts)
# 可视化
my_style = LS('#336699', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45  # type: ignore
my_config.show_legend = False  # type: ignore
my_config.title_font_size = 24  # type: ignore
my_config.label_font_size = 14  # type: ignore
my_config.major_label_font_size = 20  # type: ignore
my_config.truncate_label = 15  # type: ignore
my_config.show_y_guides = False  # type: ignore
my_config.width = 1000  # type: ignore

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
