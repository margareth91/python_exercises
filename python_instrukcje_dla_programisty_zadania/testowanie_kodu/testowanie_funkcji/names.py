from name_function import get_formatted_name

print("Wpisz 'q', aby zakonczyc dzialanie programu.")
while True:
    first = input("\nPodaj imie: ")
    if first == "q":
        break
    last = input("Podaj nazwisko: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tSformatowane pelne imie i nazwisko: {formatted_name}.")
