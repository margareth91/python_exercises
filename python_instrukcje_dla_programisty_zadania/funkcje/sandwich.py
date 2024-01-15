"""8.12. Kanapki. Utwórz funkcję akceptującą listę składników, które klient chce umieścić w zamawianej kanapce.
Funkcja powinna zawierać jeden parametr przechowujący dowolną liczbę argumentów przekazanych w wywołaniu
funkcji oraz wyświetlać podsumowanie dotyczące zamówionej kanapki. Przygotowaną funkcję wywołaj trzykrotnie, za każdym
razem z inną liczbą argumentów.
"""


def make_sandwich(*additives):
    print(f"\nPrzygotujemy kanapke z ponizszymi dodatkami:")
    for additive in additives:
        print(f"- {additive}")


make_sandwich("serek almette")
make_sandwich("losos wedzony", "serek almette")
make_sandwich("losos wedzony", "serek almette", "ogorek")
make_sandwich("losos wedzony", "serek almette", "ogorek", "ziola")
make_sandwich("losos wedzony", "serek almette", "ogorek", "ziola", "salata")
