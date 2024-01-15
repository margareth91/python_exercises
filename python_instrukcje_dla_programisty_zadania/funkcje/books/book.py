"""8.2. Ulubiona książka. Utwórz funkcję o nazwie favorite_book(), która akceptuje jeden parametr title.
Ta funkcja powinna wyświetlać komunikat w stylu:
„Jedną z moich ulubionych książek jest Alicja w krainie czarów”. Wywołaj tę funkcję i upewnij się, że podałeś tytuł
książki jako argument."""


def favorite_book(title):
    print(f"Jedna z moich ulubionych ksiazek jest ksiazka o tytule '{title.title()}'.")
