"""8.15. Wydruk modeli. Funkcje z programu print_models.py umieść w oddzielnym pliku o nazwie printing_functions.py.
Na początku pliku print_models.py umieść polecenie import i zmodyfikuj plik w taki sposób, aby używać zaimportowanych
funkcji."""

from printing_functions import print_models, show_completed_models


unprinted_designs = ["kotek", "drugi kotek", "trzeci kotek"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
