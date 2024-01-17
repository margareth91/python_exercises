"""11.3. Pracownik. Przygotuj klasę o nazwie Employee. Metoda __init__() powinna pobierać imię, nazwisko
i roczne wynagrodzenie, a następnie zapisywać te informacje w postaci atrybutów. Utwórz metodę o nazwie give_raise(),
która spowoduje zwiększenie wynagrodzenia domyślnie o 5000 zł, choć zaakceptuje także inną kwotę.

Przygotuj zestaw testów dla klasy Employee. Utwórz dwie metody testowe test_give_default_raise()
i test_give_custom_raise(). Wykorzystaj metodę setUp(), aby uniknąć konieczności tworzenia nowego egzemplarza klasy
Employee w każdej metodzie testowej. Wykonaj zestaw testów i upewnij się, że oba testy zostaną zaliczone."""


class Employee:
    def __init__(self, first_name, last_name, annual_compensation):
        self.annual_compensation = annual_compensation
        self.last_name = last_name
        self.first_name = first_name

    def give_raise(self, compensation_raise=5000):
        raised_annual_compensation = int(self.annual_compensation + compensation_raise)
        return raised_annual_compensation
