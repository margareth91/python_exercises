def get_formatted_name(first_name, last_name):
    """Zwraca elegancko sformatowane pelne imie i nazwisko"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


dziosiaki = get_formatted_name('dziosia', 'brzosia')
print(dziosiaki)


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


dziosiaki = get_formatted_name('dziosia', 'brzosia')
print(dziosiaki)
dziosiaki2 = get_formatted_name('dziosia', 'brzosia', 'dziosiaczki')
print(dziosiaki2)
