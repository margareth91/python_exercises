def make_shirt(size, text):
    print(f"Potwierdzamy zamowienie koszulki w rozmiarze {size.upper()} z napisem '{text}'.")


make_shirt('m', 'kocham kotki miau miau miau!')
make_shirt(text='miau miau miau kotki miau', size='m')


def make_shirt(size='L', text='Uwielbiam Pythona'):
    print(f"Potwierdzamy zamowienie koszulki w rozmiarze {size.upper()} z napisem '{text}'.")


make_shirt()
make_shirt(size="m")
make_shirt(text="kotki miau miau", size='s')
