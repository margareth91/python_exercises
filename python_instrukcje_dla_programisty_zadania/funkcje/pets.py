def describe_animal(animal_type, pet_name):
    """Wyswietla informacje o zwierzeciu"""
    print(f"\nMoje zwierze to {animal_type}.")
    print(f"Moj {animal_type} ma na imie {pet_name.title()}.")


describe_animal("kitku", "kotel")
describe_animal("kroliczek", "rybka")
describe_animal(pet_name="kotel", animal_type="kitku")
describe_animal(pet_name="rybka", animal_type="rybka")


def describe_animal(pet_name, animal_type="kitku"):
    print(f"\nMoje zwierze to {animal_type}.")
    print(f"Moj {animal_type} ma na imie {pet_name.title()}.")


describe_animal("fiodus")
describe_animal("pycka", animal_type="krolik")
