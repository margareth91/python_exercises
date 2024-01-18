import json

username = input("Jak masz na imie? ")

filename = "username.json"

with open(filename, "w") as f_obj:
    json.dump(username, f_obj)
    print(f"Twoje imie zostalo zapisane i bedzie uzywane pozniej, {username}!")
