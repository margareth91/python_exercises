"""8.13. Profil użytkownika. Pracę rozpocznij od kopii programu user_profile.py utworzonego nieco wcześniej w tym
rozdziale. Przygotuj własny profil przez wywołanie funkcji build_profile(), podaj imię, nazwisko oraz trzy inne pary
klucz-wartość, które Cię opisują."""


def build_profile(first, last, **user_info):
    """Budowa slownika zawierajacego wszelkie informacje o uzytkowniku"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    "kitku", "miau", location="koci domek", hobbys="paczenie na ptaszki za oknem"
)
print(user_profile)
user_profile2 = build_profile("kroli", "czek", hobbys="tupanie")
print(user_profile2)

user_profile3 = build_profile(
    "stasiu", "jasiu", hobbys="lego", favorite_pet="kitki", wife="olcia"
)
print(user_profile3)
