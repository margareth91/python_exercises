"""8.9. Magicy. Przygotuj listę imion magików, a następnie przekaż ją do funkcji o nazwie show_magicians(), która
powinna wyświetlić imię każdego magika umieszczonego na tej liście.

8.10. Doskonali magicy. Pracę rozpocznij od kopii programu z ćwiczenia 8.9. Następnie utwórz funkcję o nazwie
make_great(), której zadaniem będzie zmodyfikowanie listy magików przez dodanie słowa Doskonały na początku
imienia każdego z nich. Wywołaj funkcję show_magicians() i upewnij się, że lista faktycznie została zmodyfikowana.

8.11. Niezmienieni magicy. Pracę rozpocznij od kodu utworzonego w ćwiczeniu 8.10. Wywołaj funkcję make_great() wraz
z kopią listy imion magików. Ponieważ lista pierwotna pozostała nietknięta, wartością zwrotną funkcji
powinna być nowa lista przechowywana w nowej zmiennej. Wywołaj funkcję show_magicians() wraz z każdą listą, aby
pokazać istnienie pierwotnej listy jedynie z imionami magików oraz nowej z dodanym słowem Doskonały przed
każdym imieniem magika."""

magicians = ["dziosia", "dziusio", "fiodus", "pycka"]
great_magicians = []


def show_magicians(magicians):
    for magician in magicians:
        print(
            f"\nWitaj, {magician.title()}, milo Cie poznac! \nCzekamy na Twoje sztuczki!"
        )


show_magicians(magicians)


def make_great(magicians, great_magicians):
    for magician in magicians:
        great_magician = f"Doskonaly magik {magician}"
        great_magicians.append(great_magician)


make_great(magicians[:], great_magicians)
make_great(magicians, great_magicians)
print(great_magicians)
print(magicians)

show_magicians(magicians)
show_magicians(magicians=great_magicians)
