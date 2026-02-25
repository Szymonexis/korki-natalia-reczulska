"""
========================================
ZADANIE 1 - Funkcja print i jej parametry
========================================
Za pomoca funkcji print oraz jej parametrow sep i end wypisz nastepujacy tekst
DOKLADNIE w takiej formie (lacznie z nowa linia na koncu):

poniedziałek -> wtorek -> środa -> czwartek -> piątek!

Uzyj jednego wywolania funkcji print i przekaz nazwy dni tygodnia jako osobne argumenty.
Twoje rozwiazanie:
"""

print("poniedziałek", "wtorek", "sroda", "czwartek", "piatek", sep=" -> ", end="!\n")


"""
========================================
ZADANIE 2 - Zmienne i print
========================================
Stworz zmienne przechowujace nastepujace informacje o sobie:
  - imie
  - nazwisko
  - ulubiony kolor
  - ulubiona liczba (jako tekst, np. "7")

Nastepnie uzywajac TYLKO tych zmiennych (bez wpisywania tekstu bezposrednio do printa)
wypisz zdanie w formacie:

Nazywam sie [imie] [nazwisko], moj ulubiony kolor to [kolor], a ulubiona liczba to [liczba].

Do tego zadania mozesz uzyc dowolnej liczby wywolan funkcji print.

Twoje rozwiazanie:
"""

imie = "Natalia"
nazwisko = "Reczulska"
kolor = "niebieski"
liczba = "7"

zdanie = (
    "Nazywam sie "
    + imie
    + " "
    + nazwisko
    + ", moj ulubiony kolor to "
    + kolor
    + ", a ulubiona liczba to "
    + liczba
    + "."
)
print(zdanie)

"""
========================================
ZADANIE 3 - Funkcja input i zmienne
========================================
Napisz program, ktory:
1. Pyta uzytkownika o jego imie
2. Pyta uzytkownika o jego ulubione miasto
3. Wypisuje wiadomosc w formacie:

Czesc [imie]! Twoje ulubione miasto to [miasto].

Twoje rozwiazanie:
"""

imie = input("Podaj swoje imie:\n")
miasto = input("Podaj swoje ulubione miasto:\n")

zdanie = "Czesc " + imie + "! Twoje ulubione miast to " + miasto + "."
print(zdanie)


"""
========================================
ZADANIE 4 - Tabelka
========================================
Za pomoca funkcji print oraz znakow specjalnych \t i \n wypisz nastepujaca tabelke
DOKLADNIE w takiej formie:

Imie       |   Wiek    |   Miasto
Anna       |   25      |   Warszawa
Bartek     |   30      |   Krakow
Celina     |   22      |   Gdansk

Mozesz uzyc wiecej niz jednego wywolania funkcji print.
Uzyj parametru sep funkcji print.

Twoje rozwiazanie:
"""

print("Imie", "Wiek", "Miasto", sep="\t|\t")
print("Anna", "25", "Warszawa", sep="\t|\t")
print("Bartek", "30", "Krakow", sep="\t|\t")
print("Celina", "22", "Gdansk", sep="\t|\t")
