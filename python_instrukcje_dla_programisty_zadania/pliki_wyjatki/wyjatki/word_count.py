def count_words(filename):
    """Obliczanie przyblizonej liczby slow w danym pliku"""
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


filename = "alice.txt"
count_words(filename)

filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]
for filename in filenames:
    count_words(filename)
