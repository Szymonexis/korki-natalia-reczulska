"""
PRACA DOMOWA - 25.02.2026
Temat: f-stringi, input, print, konwersja typów

Pamiętaj:
- f-string tworzymy pisząc f przed cudzysłowem: f"tekst {zmienna}"
- input() zawsze zwraca str, więc liczby trzeba konwertować: int(...), float(...)
- kolejność działań w Pythonie jest taka sama jak w matematyce!
"""

"""
========================================================================
ZADANIE 1 - Wizytówka
========================================================================
Zapytaj użytkownika o:
  - imię
  - nazwisko
  - wiek
  - miasto zamieszkania

Następnie wypisz wizytówkę używając f-stringa w formacie:

========================
Imię i nazwisko: [imię] [nazwisko]
Wiek:            [wiek] lat
Miasto:          [miasto]
========================

Twoje rozwiązanie:
"""


"""
========================================================================
ZADANIE 2 - Kalkulator z opisem
========================================================================
Zapytaj użytkownika o dwie liczby CAŁKOWITE: a oraz b.
Pamiętaj o konwersji typów!

Następnie wypisz wyniki czterech działań, każdy w osobnej linii,
używając f-stringów w formacie:

[a] + [b] = [wynik]
[a] - [b] = [wynik]
[a] * [b] = [wynik]
[a] / [b] = [wynik]

Przykład dla a=10, b=4:
10 + 4 = 14
10 - 4 = 6
10 * 4 = 40
10 / 4 = 2.5

Twoje rozwiązanie:
"""

"""
========================================================================
ZADANIE 3 - Generator historyjki
========================================================================
Zapytaj użytkownika o:
  - imię bohatera
  - nazwę zawodu bohatera
  - nazwę miasta
  - liczbę lat (całkowita)

Następnie używając f-stringa wielolinijkowego wypisz historyjkę:

Dawno, dawno temu w mieście [miasto] żył pewien [zawód] o imieniu [imię].
Przez [lata] lat doskonalił swoje umiejętności.
Po [lata * 2] latach stał się najlepszym [zawód] w całym królestwie.

Wskazówka: wewnątrz f-stringa możesz wykonywać obliczenia: {lata * 2}

Twoje rozwiązanie:
"""


"""
========================================================================
ZADANIE 4 - Pułapka na typy
========================================================================
Poniżej masz fragment kodu. Przeanalizuj go i sprobuj go naprawic.
"""

a_str = input("Podaj liczbę a:\n")
b_str = input("Podaj liczbę b:\n")

wynik_stringow = a_str + b_str
print(f"Wynik dodawania stringów: {a_str} + {b_str} = {wynik_stringow}")
