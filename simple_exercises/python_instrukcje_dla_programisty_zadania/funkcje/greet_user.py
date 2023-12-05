def greet_user():
    """Wyswietla proste powitanie"""
    print("Witaj!")


greet_user()


def greet_user(username):
    """(zmienna) username --> parametr
    --> informacja wymagana przez funkcje, aby mogla spelnic swoje zadanie"""
    print(f"Witaj, {username}!")


greet_user("Dziosia")
""" "Dziosia" --> argument umieszczany w zmiennej, ktora jest parametrem funkcji"""
greet_user("Dziusio")


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nProsze podac imie i nazwisko: ")
    print("(wpisz 'exit', aby zakonczyc prace programu w dowolnym momencie.)")

    f_name = input("Imie: ")
    if f_name == 'exit':
        break

    l_name = input("Nazwisko: ")
    if l_name == 'exit':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nWitaj, {formatted_name}!")

