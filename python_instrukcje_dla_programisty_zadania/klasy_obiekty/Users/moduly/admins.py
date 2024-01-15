"""9.12. Wiele modułów. Klasę User umieść w jednym module, natomiast Privileges i Admin w oddzielnym. Następnie
w innym pliku utwórz egzemplarz klasy Admin i wywołaj metodę show_privileges(), aby sprawdzić, czy wszystko
działa prawidłowo."""

from admin_privileges import Admin


admin1 = Admin("Jasiu", "Stasiu", "jasiu@stas.iu", "0800jasiu")
admin1.describe_user()
admin1.privileges.show_privileges()
