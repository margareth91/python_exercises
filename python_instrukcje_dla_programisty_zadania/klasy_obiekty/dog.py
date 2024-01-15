class Dog:
    """Prosta proba modelowania psa"""

    def __init__(self, name, age):
        """Inicjalizacja atrybutow name i age"""
        self.name = name
        self.age = age

    def sit(self):
        """Symulacja, ze pies siada po otrzymaniu polecenia"""
        print(self.name.title() + " teraz siedzi.")

    def roll_over(self):
        """Symulacja, ze pies kladzie sie na plecy po otrzymaniu polecenia"""
        print(self.name.title() + " teraz polozyl sie na plecy.")


my_dog = Dog("bubciak", 8)

print("moj pies ma na imie " + my_dog.name.title())
print("moj pies ma " + str(my_dog.age) + " lat")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("lolek", 5)

print("twoj pies ma na imie " + your_dog.name.title())
print("twoj pies ma " + str(your_dog.age) + " lat")
your_dog.sit()
your_dog.roll_over()
