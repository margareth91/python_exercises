"""8.3. T-shirt. Utwórz funkcję o nazwie make_shirt(), akceptującą wielkość koszulki oraz tekst, który ma zostać na
niej nadrukowany. Funkcja powinna wyświetlić zdanie zawierające informacje dotyczące zamówionej koszulki: jej
rozmiar i tekst do wydrukowania na niej.

W trakcie pierwszego wywołania funkcji do przygotowania koszulki zastosuj argumenty pozycyjne. Natomiast w trakcie
drugiego wywołania użyj argumentów w postaci słów kluczowych.

8.4. Duże koszulki. Zmodyfikuj funkcję make_shirt() tak, aby domyślnie były przygotowywane duże koszulki z nadrukowanym
tekstem „Uwielbiam Pythona”. Utwórz koszulki w rozmiarze dużym i średnim (obie z domyślnym tekstem) oraz
koszulkę w dowolnym rozmiarze i z innym tekstem nadrukowanym na niej."""


def make_shirt(size, text):
    print(
        f"Potwierdzamy zamowienie koszulki w rozmiarze {size.upper()} z napisem '{text}'."
    )


make_shirt("m", "kocham kotki miau miau miau!")
make_shirt(text="miau miau miau kotki miau", size="m")


def make_shirt(size="L", text="Uwielbiam Pythona"):
    print(
        f"Potwierdzamy zamowienie koszulki w rozmiarze {size.upper()} z napisem '{text}'."
    )


make_shirt()
make_shirt(size="m")
make_shirt(text="kotki miau miau", size="s")
