"""
Docstring for 2026.02.18

Na zajeciach:

1. funkcja print
2. czym jest funkcja a czym zmienna - tworzenie zmiennych
3. funkcja input
4. typy proste:
    - str
    - int
    - float
5. zamiana typow:
    - float -> str
    - str -> float
    - int -> str
    - str -> int
    - int -> float
    - float -> int
"""

# ----------------------------------------------------------------------------------------
# 1. funkcja print

# print("kurczak", "smietana")

# print("kurczak", "smietana", sep=" ", end="\n")

# ----------------------------------------------------------------------------------------
# Funkcja `print` i jej parametry
# ----------------------------------------------------------------------------------------
# parametr sep (od ang. separator)
# - ustawiamy tekst ktory bedzie oddzielal poszczegolne argumenty od siebie
# - domyslnie ustawiony na " " - spacje
# parametr end
# - ustawiamy tekst ktory bedzie na samym koncu
# - domyslnie ustawiony na "\n" (znak nowej linii)
# - UWAGA: znak nowej linii musi byc zawsze na koncu printa
# ----------------------------------------------------------------------------------------
# print("kurczak", "smietana", "imbir", sep="xd", end=" || ")
# print("kurczak", "smietana", "imbir", sep=" | ", end="\n")
# ----------------------------------------------------------------------------------------


"""
Cwiczenie 1

Za pomoca print oraz jego parametrow wypisz liste czterech nazw
sklepow z ciuchami odzielonymi tekstem ", " i zakonczone " - to moje ulubione marki!"
nie zapomnij dac nowej linii na koniec
kompletny tekst powinien wygladac nastepujaco:

"house, hm, cropp, zara - to moje ulubione marki"
"""
print("house", "hm", "cropp", "zara", sep=", ", end=" - to moje ulubione marki\n")


"""
Cwiczenie 2

Za pomca print oraz jego parametrow wypisz liste wypunktowana swoich
czterech ulubionych drogerii (sephora, rossman, yves rocher, douglas)
Kompletny tekst ma wygladac tak:
- sephora
- rossman
- yves rocher
- douglas
"""
print("- sephora", "- rossman", "- yves rocher", "- douglas", sep="\n")


"""
Cwiczenie 3

Za pomoca print oraz jego parametrow wypisz cztery nazwy aplikacji.
Uzyj znakow `\t` oraz `\n` w taki sposob zebysmy otrzymali mini tabelke.
Do wykonania zadania mozesz uzyc wiecej niz jednego wywolania funkcji `print`.

Tekst ktory chcemy zobaczyc to:

Numer   |   Nazwa
0       |   Instagram
1       |   Facebook
2       |   TikTok
3       |   Snapchat
"""
print("Numer", "Nazwa", sep="\t|\t")
print("0", "Instagram", sep="\t|\t")
print("1", "Facebook", sep="\t|\t")
print("2", "TikTok", sep="\t|\t")
print("3", "Snapchat", sep="\t|\t")

# ----------------------------------------------------------------------------------------
print("-" * 40)
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# 2. czym jest funkcja a czym zmienna - tworzenie zmiennych
# 3. funkcja input
"""
Czym jest zmienna?

To takie pudelko do ktorego mozna wkladac rozne rzeczy np. tekst
"""


"""
pojawia sie nowa funkcja `input`
Jej zadaniem jest zbieranie wartosci tekstowej od uzytkowanika (z tak zwanego wejscia standardowego)

Jak wykonywac `input`?
- input()
- input(wiadomosc_do_uzytkownika)
"""
# wartosc_od_uzytkownika = input()
# wartosc_od_uzytkownika = input("Podaj ulubiona liczbe: ")
# print(wartosc_od_uzytkownika)


"""
Cwiczenie 4

zapisz tekst "Witaj swiecie!" do zmiennej i uzyj tej zmiennej w funkcji print.
"""
wiadomosc = "Witaj swiecie!"
print(wiadomosc)


"""
Cwiczenie 5

Za pomoca print oraz jego parametrow wypisz liste czterech nazw
sklepow z ciuchami odzielonymi tekstem ", " i zakonczone " - to moje ulubione marki!"
nie zapomnij dac nowej linii na koniec.

Wolno ci uzywac tylko i wylacznie zmiennych

kompletny tekst powinien wygladac nastepujaco:

"house, hm, cropp, zara - to moje ulubione marki"
"""
marka_1 = "house"
marka_2 = "hm"
marka_3 = "cropp"
marka_4 = "zara"
separator = ", "
koniec = " - to moje ulubione marki\n"
print(marka_1, marka_2, marka_3, marka_4, sep=separator, end=koniec)


"""
Cwiczenie 6

Za pomoca print oraz jego parametrow wypisz liste czterech nazw
sklepow z ciuchami ktore poda uzytkownik.
Oddzielonymi tekstem jaki poda uzytkownik.
Zakonczone tym co poda uzytkownik.

Wolno ci uzywac tylko i wylacznie zmiennych oraz funkcji print i input

kompletny tekst powinien wygladac nastepujaco:

"<marka_1><separator><marka_2><separator><marka_3><separator><marka_4><koniec>"
"""
# marka_1 = input("Podaj nazwe pierwszej marki:\n")
# marka_2 = input("Podaj nazwe drugiej marki:\n")
# marka_3 = input("Podaj nazwe trzeciej marki:\n")
# marka_4 = input("Podaj nazwe czwartej marki:\n")
# separator = input("Podaj separator tekstu:\n")
# koniec = input("Podaj zakonczenie tekstu:\n")
# print(marka_1, marka_2, marka_3, marka_4, sep=separator, end=koniec + "\n")


# input         > "Podaj zakonczenie tekstu:\n"
# uzytkownik    > "\n"
# input zwraca  > ""

# input         > "Podaj zakonczenie tekstu:\n"
# uzytkownik    > " - to moje ulubione marki\n"
# input zwraca  > " - to moje ulubione marki"
# koniec        = " - to moje ulubione marki"
# end           = " - to moje ulubione marki\n"


# print("-" * 100)
# text = input("Podaj tekst:\n")
# separator = input("Podaj separator tekstu:\n")
# print(text, text, sep=separator)


# ----------------------------------------------------------------------------------------
# 4. typy proste - str
# ----------------------------------------------------------------------------------------
"""
str - (eng. string - string of characters - ciąg znaków)
"""
print("-" * 100)

moj_str = "To jest moj tekst!"

tekst_z_cudzyslowiem_w_srodku = 'Moja ulubiona ksiazka\' to "Dune"'
tekst_z_apostrofem_w_srodku = "Moje ulubion ksiazka\" to 'Dune'"

tekst_z_mieszanka_cudzyslowia_i_apostrofu = (
    "Moje ulubione ksiazki to 'Dune' i \"Marsjanin\""
)

print(moj_str)
print(tekst_z_cudzyslowiem_w_srodku)
print(tekst_z_apostrofem_w_srodku)
print(tekst_z_mieszanka_cudzyslowia_i_apostrofu)

# TODO: Temat bedzie kontynuowany na przyszlych zajeciach
