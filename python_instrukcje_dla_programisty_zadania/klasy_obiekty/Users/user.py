"""9.3. Użytkownicy. Przygotuj klasę o nazwie User. Zdefiniuj w niej dwa atrybuty (first_name i last_name),
a następnie utwórz kilka innych atrybutów, które zwykle są przechowywane w profilu użytkownika. Zdefiniuj metodę
o nazwie describe_user(), wyświetlającą podsumowanie informacji zebranych o użytkowniku. Utwórz jeszcze drugą metodę
o nazwie greet_user(), która będzie wyświetlała użytkownikowi spersonalizowane powitanie. Utwórz kilka egzemplarzy
reprezentujących różnych użytkowników, a następnie dla każdego z nich wywołaj obie metody.

9.5. Próby logowania. Pracę rozpocznij od programu utworzonego w ćwiczeniu 9.3. Do klasy User dodaj metodę
o nazwie increment_login_attempts(), pozwalający na inkrementację wartości login_attempts o 1. Utwórz drugą
metodę o nazwie reset_login_attempts(), która będzie zerowała wartość login_attempts. Utwórz egzemplarz klasy User
i kilkukrotnie wywołaj metodę increment_login_attempts(). Wyświetl wartość login_attempts, aby mieć pewność o jej
prawidłowej inkrementacji. Następnie wywołaj metodę reset_login_attempts(). Ponownie wyświetl wartość login_attempts
i sprawdź, czy na pewno wynosi 0."""


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


user1 = User("Fiodus", "Miodus", "miau@miau.miau", "123456987")
user2 = User("Miodus", "Fiodus", "miauu@miau.miau", "789654123")
user3 = User("Jasiu", "Stasiu", "kotki@miau.miau", "741258963")
user4 = User("Stasiu", "Jasiu", "nie-kotki@nie-miau.nie-miau", "963258741")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user4.describe_user()
user4.greet_user()
user1.increment_login_attempts()
user1.read_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.read_login_attempts()
user1.reset_login_attempts()
user1.read_login_attempts()
