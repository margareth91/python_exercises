from pygal_maps_world.maps import World

wm = World()
wm.force_uri_protocol = "http"
wm.title = "Ameryka Polnocna, Srodkowa i Poludniowa"

wm.add("Ameryka Polnocna", ["ca", "mx", "us"])
wm.add("Ameryka Srodkowa", ["bz", "cr", "gt", "hn", "ni", "pa", "sv"])
wm.add(
    "Ameryka Poludniowa",
    ["ar", "bo", "br", "cl", "co", "ec", "gf", "gy", "pe", "py", "sr", "uy", "ve"],
)

wm.render_to_file("americas.svg")
