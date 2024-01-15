"""9.8. Uprawnienia. Zdefiniuj oddzielną klasę Privileges. Ta klasa powinna mieć jeden atrybut (privileges),
przechowujący listę ciągów tekstowych, tak jak przedstawiłem to w poprzednim ćwiczeniu. Metodę show_privileges()
przenieś do nowej klasy. Utwórz egzemplarz klasy Privileges jako atrybut w klasie Admin. Następnie utwórz nowy
egzemplarz klasy Admin i użyj metody show_privileges() do wyświetlenia uprawnień."""


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


class Privileges:

    def __init__(self):
        self.privileges = ['moze dodac post', 'moze usunac post', 'moze zbanowac uzytkownika',
                           'akceptuje posty', 'dodaje uprawnienia nowym adminom']

    def show_privileges(self):
        print(f"Admin posiada nastepujace uprawnienia: {self.privileges}.")


class Admin(User):

    def __init__(self, first_name, last_name, email_address, phone_number):
        super().__init__(first_name, last_name, email_address, phone_number)
        self.privileges = Privileges()


admin1 = Admin('jasia', "stasia", "kotki@miau.czom", "987456321")
admin1.privileges.show_privileges()
admin1.describe_user()
admin1.read_login_attempts()
admin1.increment_login_attempts()
admin1.read_login_attempts()
