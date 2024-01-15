import json

from pygal_maps_world.maps import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code

# Wczytanie danych i umieszczenie ich na liscie
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)


# Utworzenie slownika danych populacji
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Podzielenie populacji na grupy wedlug liczebnosci
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.force_uri_protocol = "http"
wm.title = "Populacja na swiecie w 2010 roku"
# wm.add("2010", cc_populations)
wm.add("0 - 10 mln", cc_pops1)
wm.add("10 mln - 1 mld", cc_pops2)
wm.add("> 1 mld", cc_pops3)

wm.render_to_file("world_population_pops_groups.svg")
