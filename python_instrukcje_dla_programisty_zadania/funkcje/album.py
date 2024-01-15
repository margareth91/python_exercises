"""8.7. Album. Utwórz funkcję o nazwie make_album() odpowiedzialną za zbudowanie słownika reprezentującego album
muzyczny. Funkcja powinna pobrać nazwę zespołu lub artysty oraz tytuł albumu. Wartością zwrotną funkcji powinien
być słownik zawierający te dwa fragmenty informacji. Za pomocą przygotowanej funkcji utwórz trzy słowniki
przedstawiające różne albumy. Wyświetl każdą wartość zwrotną, aby pokazać, że słowniki prawidłowo przechowują
informacje o albumach.

Do funkcji make_album() dodaj opcjonalny parametr pozwalający na przechowywanie liczby utworów znajdujących się na
płycie. Jeżeli wywołanie funkcji będzie zawierało wartość dla liczby utworów, należy ją dodać do słownika
informacji o albumie. Zdefiniuj co najmniej jedno nowe wywołanie funkcji obejmujące także liczbę utworów na płycie.

8.8. Albumy użytkowników. Pracę rozpocznij od programu utworzonego w ćwiczeniu 8.7. Dodaj pętlę while pozwalającą
użytkownikom na wprowadzenie artysty i tytułu płyty. Po zebraniu tych informacji wywołaj funkcję make_album() wraz
z podanymi przez użytkownika danymi wejściowymi oraz wyświetl słownik utworzony przez program. Upewnij się, że
zdefiniowałeś wartość pozwalającą opuścić pętlę while."""


def make_album(band_artist_name, title, songs_number=""):
    album = {"band_or_artist_name": band_artist_name, "title": title}
    if songs_number:
        album["songs_number"] = int(songs_number)
    return album


album1 = make_album("Ed Sheeran", "-", songs_number="14")
print(album1)
album2 = make_album("Taylor Swift", "1989")
print(album2)
album3 = make_album("Imagine Dragons", "Evolve")
print(album3)
album4 = make_album("Ed Sheeran", "=", songs_number="18")
print(album4)

while True:
    print("Program umozliwiajacy dodanie posiadanych albumow do listy")
    print("(Aby zakonczyc dzialanie programu w dowolnym momencie, wpisz 'exit'.)")

    band_or_artist_name = input("Podaj nazwe zespolu lub imie i nazwisko artysty: ")
    if band_or_artist_name == "exit":
        break

    album_title = input("Podaj nazwe tytulu albumu: ")
    if album_title == "exit":
        break

    new_album = make_album(band_or_artist_name.title(), album_title.title())
    print(
        f"Ddales do listy swoich albumow album artysty/zespolu {band_or_artist_name.title()} o tytule "
        f"{album_title.title()}."
    )
