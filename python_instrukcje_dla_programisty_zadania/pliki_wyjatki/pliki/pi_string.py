filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print(f"{pi_string[:52]}...")

birthday = input("Podaj swoja date urodzenia w formacie ddmmrr: ")
if birthday in pi_string:
    print("Twoja data urodzenia znajduje sie wsrod miliona pierwszych cyfr liczby pi!")
else:
    print(
        "Twoja data urodzenia nie znajduje sie wsrod miliona pierwszych cyfr liczby pi."
    )
