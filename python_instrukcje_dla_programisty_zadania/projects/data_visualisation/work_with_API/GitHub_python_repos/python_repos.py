import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS

# Wykonanie wywolania API i zachowanie otrzymanej odpowiedzi
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url, timeout=(None, 30))
print(f"Kod stanu: {r.status_code}")
# Utworzenie odpowiedzi w zmiennej
response_dict = r.json()
print(response_dict.keys())
print(response_dict['incomplete_results'])
print(f"Zwrocona liczba repozytoriow Pythonowych: {response_dict['total_count']}")
# Przetworzenie informacji o repozytoriach
repo_dicts = response_dict["items"]
print(f"Liczba zwroconych repozytoriow: {len(repo_dicts)}")
# Przetworzenie repozytoriow
# names, stars = [], []
names, plot_dicts = [], []
# repo_dict = repo_dicts[0]
# print(f"\nIlosc kluczy: {len(repo_dict)}")
# print("Nazwy kluczy:")
# for key in sorted(repo_dict.keys()):
#     print(key)
# print(f"\nWybrane informacje o kazdym repozytorium:")
for repo_dict in repo_dicts:
    # print(f"\nNazwa: {repo_dict['name']}")
    # print(f"Wlasciciel: {repo_dict['owner']['login']}")
    # print(f"Gwiazdki: {repo_dict['stargazers_count']}")
    # print(f"Repozytorium: {repo_dict['html_url']}")
    # print(f"Utworzone: {repo_dict['created_at']}")
    # print(f"Uaktualnione: {repo_dict['updated_at']}")
    # print(f"Opis: {repo_dict['description']}")
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

my_style = LS(color='#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.force_uri_protocol = 'http'
chart.title = 'Zwrocone projekty Pythona z serwisu GitHub, posortowane wg najwiekszej ilosci gwiazdek'
chart.x_labels = names
# chart.add('', stars)
chart.add('', plot_dicts)
# chart.render_to_file('python_repos.svg')
chart.render_to_file('python_repos_with_descr.svg')
