"""9.14. Kostki. Moduł random zawiera funkcje odpowiedzialne za generowanie losowych liczb na wiele różnych sposobów.
Wartością zwrotną funkcji randint() jest liczba całkowita z podanego przedziału. Dlatego też poniższy fragmentu
kodu zwraca liczbę z przedziału od 1 do 6:
from random import randint
x = randint(1, 6)
Przygotuj klasę Die z jednym atrybutem o nazwie sides, którego wartością domyślną będzie 6. Utwórz metodę o nazwie
roll_die(), wyświetlającą losowo wygenerowaną liczbę z zakresu od 1 do wartości określonej przez liczbę ścianek
na kostce. Utwórz kostkę zawierającą sześć ścianek i zasymuluj rzucenie nią 10 razy. Później utwórz kostki zawierające
10 i 20 ścianek. Każdą nową kostką rzuć 10 razy."""

import random


class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        result = random.randint(1, self.sides)
        print(f"Na kostce wyrzucono {result}.")
        # return result


die1 = Die(sides=6)
die1.roll_die()

die2 = Die(sides=10)
die2.roll_die()

die3 = Die(sides=20)
die3.roll_die()
