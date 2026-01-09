# Dopelnienie tematu liczb

a = 3
b = 4.0
c = 2
wynik = (a + b) * c
print(wynik)


# ten program nie dziala poprawnie bo nie konwertujemy tekstu (str)
# zwracanego przez funkcje input
# na wartosc zmiennoprzecinkowa (float)
a = input("Podaj mi liczbe zmiennoprzecinkowa:\n")
print(a)

# poprawna wersja programu
a_tekst = input("Podaj mi liczbe zmiennoprzecinkowa:\n")
a = float(a_tekst)
print(a)


a_tekst = input("Podaj liczbe calkowita a:\n")
b_tekst = input("Podaj liczbe calkowita b:\n")
c_tekst = input("Podaj liczbe calkowita c:\n")
a = int(a_tekst)
b = int(b_tekst)
c = int(c_tekst)
print(a + b + c)

# ----------

# Typy w pythone, czesc dalsza
# 3. Ciagi znakowe (teksty) - string - w pythonie str (od ang. string of characters)
# Mozemy stringi tworzy na wiele sposobow

pusty_string = ""

moj_str_1 = "Hej, hi, hello!"  # przy uzyciu cudzyslowia - jednolinikowy string
moj_str_2 = 'Hej, hi, hello!'  # przy uzyciu ampersant - jednolinikowy string
moj_str_3 = """Hej, hi, hello!"""  # przy uzyciu 3 cudzyslowii - specjalny typ stringa, wielolinijkowy

moj_str_cudzyslowia = "\"Hej\", \n\t'hi', \n\\hello!"
moj_str_apostrofy = '"Hej", \n\t\'hi\', \n\\hello!'
moj_str_wielolinijkowy = """"Hej",
\t'hi',
\\hello!"""

print(moj_str_cudzyslowia)
print(moj_str_apostrofy)
print(moj_str_wielolinijkowy)

"""
Zadanie 1
Stworz program ktory wypisze wiadomosc o takiej zawartosci:

Hejka,

    Pisze z <wstaw nazwe>,
    Jest super. Bylam ostatnio w "Mc Donald's" - nowy drwal jest dobry.

'Wyslano z iPhone'
"""


# === PODSUMOWANIE LEKCJI ===
# 
# Na tej lekcji poznaliśmy różne sposoby tworzenia stringów (ciągów znaków) w Pythonie.
# Oto najważniejsze informacje:
# 
# 1. CUDZYSŁÓW PODWÓJNY: "tekst"
#    - Służy do tworzenia jednolinijkowych stringów
#    - Wewnątrz możesz swobodnie używać apostrofów: "It's easy!"
#    - Jeśli chcesz użyć cudzysłowia wewnątrz, musisz go "uciec" (escape): "To jest \"cytat\""
#    - Znaki specjalne jak \n (nowa linia) czy \t (tabulator) muszą być dodane manualnie
# 
# 2. APOSTROF (CUDZYSŁÓW POJEDYNCZY): 'tekst'
#    - Działa dokładnie tak samo jak cudzysłów podwójny - to kwestia preferencji
#    - Wewnątrz możesz swobodnie używać cudzysłowów: 'Ona powiedziała "cześć"'
#    - Jeśli chcesz użyć apostrofu wewnątrz, musisz go "uciec": 'It\'s easy!'
#    - Również wymaga manualnego dodawania znaków specjalnych (\n, \t, itp.)
# 
# 3. POTRÓJNY CUDZYSŁÓW: """tekst"""
#    - To specjalny typ stringa - wielolinijkowy (multiline string)
#    - Możesz pisać w wielu liniach bez używania \n - Enter działa naturalnie
#    - Wcięcia (spacje, tabulatory) są automatycznie zachowane
#    - Możesz swobodnie używać zarówno ' jak i " wewnątrz bez escapowania
#    - Idealny do dłuższych tekstów, dokumentacji lub gdy tekst ma zachować formatowanie
# 
# KLUCZOWA RÓŻNICA:
# - "" i '' = stringi jednolinijkowe (wymagają \n do nowej linii)
# - """""" = string wielolinijkowy (nowa linia działa naturalnie po naciśnięciu Enter)
# 
# ZNAKI SPECJALNE (escape sequences):
# - \n = nowa linia (przechodzi do następnej linii)
# - \t = tabulator (wcięcie)
# - \\ = backslash (sam znak \)
# - \" = cudzysłów wewnątrz stringa z cudzysłowiem
# - \' = apostrof wewnątrz stringa z apostrofem
# 
# Dodatkowo powtórzyliśmy:
# - Konwersję typów: int() dla liczb całkowitych, float() dla zmiennoprzecinkowych
# - Funkcję input() która zawsze zwraca string, więc trzeba go konwertować na liczby
