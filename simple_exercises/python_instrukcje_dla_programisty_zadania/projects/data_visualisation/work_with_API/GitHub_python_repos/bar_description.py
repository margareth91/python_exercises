import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS

my_style = LS(color="#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.force_uri_protocol = "http"
chart.title = "Projekty Pythona"
chart.x_labels = ["HelloGitHub", "django", "pytorch"]

plot_dicts = [
    {"value": 79325, "label": "Opis projektu HelloGitHub"},
    {"value": 74413, "label": "Opis projektu django"},
    {"value": 73311, "label": "Opis projektu pytorch"},
]

chart.add("", plot_dicts)
chart.render_to_file("bar_descriptions.svg")
