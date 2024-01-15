from user import User


class Privileges:
    def __init__(self):
        self.privileges = [
            "moze dodac post",
            "moze usunac post",
            "moze zbanowac uzytkownika",
            "akceptuje posty",
            "dodaje uprawnienia nowym adminom",
        ]

    def show_privileges(self):
        print(f"Admin posiada nastepujace uprawnienia: {self.privileges}.")


class Admin(User):
    def __init__(self, first_name, last_name, email_address, phone_number):
        super().__init__(first_name, last_name, email_address, phone_number)
        self.privileges = Privileges()
