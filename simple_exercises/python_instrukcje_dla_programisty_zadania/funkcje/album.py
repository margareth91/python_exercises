def make_album(band_artist_name, title, songs_number=''):
    album = {'band_or_artist_name': band_artist_name, 'title': title}
    if songs_number:
        album['songs_number'] = int(songs_number)
    return album


album1 = make_album('Ed Sheeran', '-', songs_number='14')
print(album1)
album2 = make_album('Taylor Swift', '1989')
print(album2)
album3 = make_album('dziobaki', 'bobaki')
print(album3)
album4 = make_album('Ed Sheeran', '=', songs_number='18')
print(album4)

while True:
    print("Program umozliwiajacy dodanie posiadanych albumow do listy")
    print("(Aby zakonczyc dzialanie programu w dowolnym momencie, wpisz 'exit'.)")

    band_or_artist_name = input("Podaj nazwe zespolu lub imie i nazwisko artysty: ")
    if band_or_artist_name == 'exit':
        break

    album_title = input("Podaj nazwe tytulu albumu: ")
    if album_title == 'exit':
        break

    new_album = make_album(band_or_artist_name.title(), album_title.title())
    print(f"Ddales do listy swoich albumow album artysty/zespolu {band_or_artist_name.title()} o tytule "
          f"{album_title.title()}.")
