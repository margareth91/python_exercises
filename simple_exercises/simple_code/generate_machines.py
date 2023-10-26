# Stwórz klasę Maszyna
# # Niech Maszyna posiada metode pokaż_wyniki
#  metoda niech zwraca tablice z 20 wpisami przedstawiające wygenerowane przypadkowo temperatury
# # stwórz 3 instancje maszyn: maszyna_pom, maszyna_zpom, maszyna_kpom

import random


class Maszyna:

    def __init__(self, pokaz_wyniki=None):
        if pokaz_wyniki is None:
            pokaz_wyniki = []
        self.pokaz_wyniki = pokaz_wyniki

        while len(pokaz_wyniki) <= 20:
            wynik = random.randint(-40, 40)
            pokaz_wyniki.append(wynik)


def print_maszyna(maszyna):
    print(f"Maszyna ma zapis temperatur: {maszyna.pokaz_wyniki}")


def maszyny():
    maszyna_pom = Maszyna()
    print_maszyna(maszyna_pom)
    maszyna_zpom = Maszyna()
    print_maszyna(maszyna_zpom)
    maszyna_kpom = Maszyna()
    print_maszyna(maszyna_kpom)


if __name__ == '__main__':
    maszyny()





