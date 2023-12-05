magicians = ['dziosia', 'dziusio', 'fiodus', 'pycka']
great_magicians = []


def show_magicians(magicians):
    for magician in magicians:
        print(f"\nWitaj, {magician.title()}, milo Cie poznac! \nCzekamy na Twoje sztuczki!")


show_magicians(magicians)


def make_great(magicians, great_magicians):
    for magician in magicians:
        great_magician = f"Doskonaly magik {magician}"
        great_magicians.append(great_magician)


make_great(magicians[:], great_magicians)
make_great(magicians, great_magicians)
print(great_magicians)
print(magicians)

show_magicians(magicians)
show_magicians(magicians=great_magicians) 


