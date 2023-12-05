def build_person(first_name, last_name):
    """Zwraca slownik informacji o danej osobie"""
    person = {'first': first_name, 'last': last_name}
    return person


dziosiaki = build_person('dziosia', 'brzosia')
print(dziosiaki)


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = int(age)
    return person


dziosiaki = build_person('dziosia', 'brzosia', age='18')
print(dziosiaki)


