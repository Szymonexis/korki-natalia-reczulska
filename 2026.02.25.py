"""
Docstring for 2026.02.25

Na zajeciach:

1. typy proste:
    - str
    - int
    - float
2. zamiana typow:
    - float -> str
    - str -> float
    - int -> str
    - str -> int
    - int -> float
    - float -> int
"""

# ========================================================================================================================================
# Stringi - wartosci tekstowe / ciagi znakowe
# ========================================================================================================================================

# \ (backslash) - jest specjalnym znakiem ktory mowi pythonowi "nastepny znak jest doslownie tekstem"
# \n - to jest znak enter albo inaczej znak nowej linii
# \t - to jest znak tabulatury
# \" - ta kambinacja znakow pozwoli ci wstawic " do tekstu
# \' - ta kombinacja znakow pozwoli ci wstawic ' do tekstu
# \\ - ta kombinacja znakow pozwoli ci wstawic \ do tekstu
# \{ - ta kombinacja znakow pozwoli ci wstawic { do tekstu
# \} - ta kombinacja znakow pozwoli ci wstawic } do tekstu
# -------- mniej populare
# \r - tzw. "carriage return" - uzywany do tekstow na widnowsie wraz ze znakiem \n -> \n\r (ta kombinacja
# jest wymagana w specyficznych kodowaniach tekstu)

# \Dune\ to calkiem dobra ksiazka
moj_tekst = "\\Dune\\ to calkiem dobra ksiazka"
print(moj_tekst)

"""
"Dune" to calkiem dobra ksiazka.
Przeczytalem ja dwa razy. 
"""
moj_wielolinijkowy_tekst = '"Dune" to calkiem dobra ksiazka.\nPrzeczytalem ja dwa razy.'
print(moj_wielolinijkowy_tekst)


# multiline string - ciag znakow jako wilolinijkowa wartosc - uzywamy """..."""
moj_wielolinijkowy_tekst = """\"Dune\" to calkiem dobra ksiazka.
Przeczytalem ja dwa razy."""
print(moj_wielolinijkowy_tekst)

# ========================================================================================================================================
# f - stringi
# ========================================================================================================================================
przymiotnik = "ulubiona"

moj_normalny_string = '"Dune" to moja\t{} ksiazka.'.format(przymiotnik)

moj_konkatowany_string = '"Dune" to moja\t' + przymiotnik + " ksiazka."

moj_f_string = f'"Dune" to moja\t{przymiotnik} ksiazka.'

print(moj_normalny_string)
print(moj_f_string)

moj_wielolinijkowy_f_string = f"""BBBBB
AAAAAAA
{przymiotnik}
DDDDD"""

print(moj_wielolinijkowy_f_string)

# ========================================================================================================================================

"""
Cwiczenie 1

Zdobadz od uzytkownika imie oraz jego wiek.
Uzywajac f stringa, wypisz komunikat:

Hej, {imie}!
Milo cie widziec - ja tez mam {lat} lat!
"""
# imie = input("Jak masz na imie:\n")
# wiek = input("Ile masz lat:\n")

# tekst = f"""Hej, {imie}!
# Milo cie widziec - ja tez mam {wiek} lat!"""

# print(tekst)


"""
Cwiczenie 2

Najpierw spytaj uzytkownika o co mamy go odpytac. 

Tzn.:
1. Uzywajac input, wypisz komunikat "Podaj o co program ma cie zapytac - wiek, wzrost, kolor wlosow. Podaj jedno:\n"
2. Uyzwajac input, zapytaj o ta rzecz (czyli, albo o wiek, albo o wzrost, albo o kolor wlosow)
3. Uyzwajac print wypisz "twoj {cecha} to {wartosc}"
"""

# cecha = input("Podaj o co program ma cie zapytac - wiek, wzrost, kolor wlosow. Podaj jedno:\n")

# wartosc_cechy = input(f"Podaj swoj {cecha}:\n")
# print(f"twoj {cecha} to {wartosc_cechy}")


"""
Cwiczenie 3

Zapytaj uzytkownika o:
- imie postaci
- imie postaci przyjaciela
- nazwe tajemnisczego obiektu
- nazwe miejsca w ktorym zostal znaleziony tajemniczy obiekt

In a quiet town, [Your_Name] found a small [Object_Name] hidden beneath the old [Place_Name]. 
No one knew who had left it there, or why it seemed to hum softly at night.
Curious, [Your_Name] showed it to [Friends_Name], who warned that some things are forgotten for a reason. 
But when the sky darkened and the [Object_Name] began to glow, they realized it wasn't meant to stay buried.
Whatever it was, and whoever they were, this was the moment everything changed.
"""

# imie_postaci = input("Podaj imie postaci:\n")
# imie_przyjaciela = input("Podaj imie postaci przyjaciela:\n")
# nazwa_tajemniczego_obiektu = input("Podaj nazwe tajemniczego obiektu:\n")
# nazwa_tajemniczego_miejsca = input("Podaj nazwe tajemniczego miejsca:\n")

# tekst = f"""In a quiet town, {imie_postaci} found a small {nazwa_tajemniczego_obiektu} hidden beneath the old {nazwa_tajemniczego_miejsca}. 
# No one knew who had left it there, or why it seemed to hum softly at night.
# Curious, {imie_postaci} showed it to {imie_przyjaciela}, who warned that some things are forgotten for a reason. 
# But when the sky darkened and the {nazwa_tajemniczego_obiektu} began to glow, they realized it wasn't meant to stay buried.
# Whatever it was, and whoever they were, this was the moment everything changed."""

# print(tekst)

# ========================================================================================================================================
# zamiany typow
# str -> int
# str -> float
# ========================================================================================================================================

# Kazdy typ w pythonie posiada specjalna funkcje ktora nazywamy konstruktorem
# przypomnienie jak wygladaly funkcje w kodzie - innymi slowy jak rozpoznac czy cos jest funkcja czy jest zmienna

# tworzenie zmiennej
zmienna_tekstowa = str("wartosc")
zmienna_calkowita = int(4096)
zmienna_zmiennoprzecinkowa = float(40.96)

# uzycie zmiennej
# ... zmienna_tekstowa ...

# uzycie funkcji
print(
    zmienna_calkowita, 
    zmienna_tekstowa, 
    zmienna_zmiennoprzecinkowa,
)

# To czym sa te specjalne funkcje nazywane konstruktorami?
# Te funkcje pozwalaja tworzyc zmienne konkretnego typu
# to znaczy ze dla:
# - wartosci tekstowych - stringow - str - istnieje funkcja str()
# - wartosci calkowitych - intow - int - istnieje funkcja int()
# - wartosci zmiennoprzecinkowych - floatow - float - istnieje funkcja float()
# Te konstruktory pozwalaja nam na uzycie mechanizmu KONWERSJI TYPOW

# zmienna_str_a = "4096"
# zmienna_str_b = "4"

# zmienna_int_a = int(zmienna_str_a) # int(zmienna_str_a) -> int("4096") -> 4096
# zmienna_int_b = int(zmienna_str_b) # int(zmienna_str_b) -> int("4") -> 4

# wynik_dodawania_stringow = zmienna_str_a + zmienna_str_b
# wynik_dodawania_intow = zmienna_int_a + zmienna_int_b

# print(f"wynik dodawania stringow do siebie {zmienna_str_a} + {zmienna_str_b} = {wynik_dodawania_stringow}")
# print(f"wynik dodawania intow do siebie {zmienna_int_a} + {zmienna_int_b} = {wynik_dodawania_intow}")

# ========================================================================================================================================

a_str = input("Podaj wartosc a:\n")
b_str = input("Podaj wartosc b:\n")

# Uwaga kolejnosc dzialan jak w matematyce
# wynik = int(a_str + b_str) # int(a_str + b_str) -> int("2" + "12") -> int("212") -> 212

wynik = int(a_str) + int(b_str) # int(a_str) + int(b_str) -> int("2") + int("12") -> 2 + 12 -> 14
print(f"{a_str} + {b_str} = {wynik}")




