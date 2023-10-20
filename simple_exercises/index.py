
example = "dziobdziaki"

for index, letter in enumerate(example):
    print(letter)

print(f"Litera 'd' w slowie '{example}' wystepuje {example.count("d")} razy")

example2 = input("Podaj dowolne slowo: ")
count = 0

for letter in example2:
    if letter == "d":
        count += 1
print(f"Litera 'd' wystepuje w slowie '{example2}' {count} razy")
