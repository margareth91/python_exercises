"""9.7. Admin. Administrator to specjalny rodzaj użytkownika. Zdefiniuj klasę o nazwie Admin dziedziczącą po klasie
User utworzonej w ćwiczeniu 9.3 lub 9.5. Dodaj atrybut privileges przechowujący listę ciągów tekstowych takich jak
„może dodać post”, „może usunąć post” czy „może zbanować użytkownika”. Zdefiniuj metodę o nazwie show_privileges(),
wyświetlającą listę uprawnień administratora. Utwórz egzemplarz klasy Admin i wywołaj nową metodę."""


class User:

    def __init__(self, first_name, last_name, email_address, phone_number):
        self.phone_number = phone_number
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{"=" * 20} \nInformacje o uzytkowniku: \n Imie: {self.first_name} \n Nazwisko: {self.last_name} "
              f"\n Adres email: {self.email_address} \n Numer telefonu: {self.phone_number} \n{"=" * 20}")

    def greet_user(self):
        print(f"Witaj, {self.first_name} {self.last_name}")

    def read_login_attempts(self):
        print(f"Uzytkownik {self.first_name} {self.last_name}: ilosc prob logowania: {self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, email_address, phone_number):
        super().__init__(first_name, last_name, email_address, phone_number)
        self.privileges = ['moze dodac post', 'moze usunac post', 'moze zbanowac uzytkownika',
                           'akceptuje posty', 'dodaje uprawnienia nowym adminom']

    def show_privileges(self):
        print(f"Admin posiada nastepujace uprawnienia: {self.privileges}.")

