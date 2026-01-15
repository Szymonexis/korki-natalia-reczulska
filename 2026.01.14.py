# 4. Stringi w pythonie (ciagi tekstowe)
maly_tekst = "lorem ipsum at dolor et sit amet"

#                  01234567890
imie_i_nazwisko = "Agata Galka"
pierwsza_listera = imie_i_nazwisko[0]
imie = imie_i_nazwisko[0:5]
nazwisko = imie_i_nazwisko[6:11]
print(f"imie = {imie}")
print(f"nazwisko = {nazwisko}")

imie_i_nazwisko = "Szymon Kaszuba-Gałka"
podzielone_imie_i_nazwisko = imie_i_nazwisko.split(" ")
print(type(podzielone_imie_i_nazwisko), podzielone_imie_i_nazwisko)

# 5. Listy w pythonie
moja_lista = []
moja_lista = list()

tekst_ale_to_lista = ["S", "z", "y", ...]
lista_z_tekstu = list(imie_i_nazwisko)

pierwszy_element_listy = lista_z_tekstu[0]
pierwsze_piec_elementow_listy = lista_z_tekstu[0:5]
print(f"pierwszy_element_listy = {pierwszy_element_listy}")
print(f"pierwsze_piec_elementow_listy = {pierwsze_piec_elementow_listy}")

# ---

maly_tekst = "lorem ipsum at dolor et sit amet"
duzy_tekst = "AAAAAAAAAAAAAAAAA"
chaotyczny_tekst = "Byc Albo Nie Byc"
print(maly_tekst.upper())
print(duzy_tekst.lower())
print(maly_tekst.capitalize())
print(duzy_tekst.capitalize())
print(maly_tekst.title())
print(duzy_tekst.title())
print(chaotyczny_tekst.swapcase())


