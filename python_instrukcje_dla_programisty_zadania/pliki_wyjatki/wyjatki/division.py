try:
    print(5 / 0)
except ZeroDivisionError:
    print("Nie mozna dzielic przez zero!")


print("Podaj dwie liczby, ktore zostana podzielione.")
print("Wpisz 'q', aby zakonczyc dzialanie programu.")

while True:
    first_number = input("\nPierwsza liczba: ")
    if first_number == "q":
        break
    second_number = input("Druga liczba: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Nie mozna dzielic przez zero!")
    else:
        print(answer)
