from pygal_maps_world.maps import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = "Wielkosc populacji w krajach Ameryki Polnocnej"
wm.add('Ameryka Polnocna',  {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')