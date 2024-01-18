filename = "programming.txt"

with open(filename, "w") as file_object:
    file_object.write("Uwielbiam programowac.\n")
    file_object.write("Uwielbiam tworzyc nowe gry.\n")

with open(filename, 'a') as file_object:
    file_object.write("Uwielbiam tworzyc aplikacje uruchamiane w przegladarce internetowej.\n")
