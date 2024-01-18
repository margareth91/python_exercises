filename = "alice.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"Przepraszamy, ale plik '{filename}' nie istnieje."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print(f"Plik '{filename}' zawiera {num_words} slow.")
