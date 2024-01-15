def build_person(first_name, last_name):
    """Zwraca slownik informacji o danej osobie"""
    person = {"first": first_name, "last": last_name}
    return person


miau = build_person("kotek", "miau")
print(miau)


def build_person(first_name, last_name, age=""):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = int(age)
    return person


miau = build_person("kotek", "miau", age="18")
print(miau)
