# ======================
# Zadanie 2
# ======================
# Stworz program ktory pobierze od uzytkownika tekst (minimum 20 znakow dlugosci)
# Nastepnie twoj program:
# - wypisze wycinek tekstu (numer znaku poczatkowego i
#   koncowego podane przez uzytkownika - pamietaj o konwersji na int())
# - wypisze wszystkie slowa z tekstu w postaci
#   listy (czyli podzieli tekst uzywajac znaku spacji)
# - wypisze tekst podzielony przy uzyciu wybranego prze uzytkownika separatora
#   np.:
#   tekst = "aabbccaabbccaabbcc"
#   wybrany_separator = "aa",
#   czesci_tekstu = ["", "bbcc", "bbcc", "bbcc"]
# - wypisze tekst z zamienionymi wielkosciami liter
#   np.
#   tekst = "Liberate Tutemet Ex Inferis"
#   tekst_odwrocony = "lIBERATE tUTEMET eX iNFERIS"
# - wykona jeszcze jedna, dodatkowa wybrana przez
#   ciebie operacje na tekscie i wypisze jej wynik
# ======================

# ---------------------------------------------------

# typy danych w pythonie
# | Nazwa typu i jego konstruktor | Opis
# | ----------------------------- | ------------------------------------
# | int                           | wartosci liczbowe calkowite
# | float                         | wartosc liczbowe zmiennoprzecinkowe
# | str                           | tekst / ciagi znakow


# zmienne typu calkowitego (int)
zmienna_int = 3
zmienna_int = int("3")
zmienna_int = int("-3")
zmienna_int = int(3.1)

print(f"zmienna_int = {zmienna_int}")


# zmienne typu zmiennoprzecinkowego (float)
zmienna_float = 3.0
zmienna_float = float("3")
zmienna_float = float("3.0")
zmienna_float = float("3.1")
zmienna_float = float("-3.1")
zmienna_float = float(4)
zmienna_float = float(int("4"))

print(f"zmienna_float = {zmienna_float}")

# --------------------------------------------------------------------------------

# operacje arytmetyczne
a = 3
b = 6

# dodawanie
przyklad_dodawania = 2 + 4
przyklad_dodawania = 2 + 4.0
przyklad_dodawania = a + b

# odejmowanie
przyklad_odejmowania = 4 - 2
przyklad_odejmowania = 4 - 2.0
przyklad_odejmowania = a - b

# mnozenie
przyklad_mnozenia = 4 * 2
przyklad_mnozenia = int(4 * 2.0)
przyklad_mnozenia = a * b

# dzielenie
przyklad_dzielenia = 4 / 2
przyklad_dzielenia = 5 / 2  # wynik to 2.5
przyklad_dzielenia = 4 / 0  # podniesie (wyrzuci) ZeroDivisionError
przyklad_dzielenia = a / b

# dzielenie calkowite
przyklad_dzielenia_calkowitego = 4 // 2
przyklad_dzielenia_calkowitego = 5 // 2  # wynik to 2
przyklad_dzielenia_calkowitego = 4 // 0  # podniesie (wyrzuci) ZeroDivisionError
przyklad_dzielenia_calkowitego = a // b

# potegowanie
przyklad_potegowania = 4**2
przyklad_potegowania = 4**2.0
przyklad_potegowania = a**b

# modullo (reszta z dzielenia calkowitego)
przyklad_modullo = 4 % 2  # 0
przyklad_modullo = 5 % 2  # 1
# -----------------------------
przyklad_modullo = -3 % 3  # 0
przyklad_modullo = -2 % 3  # 1
przyklad_modullo = -1 % 3  # 2
przyklad_modullo = 0 % 3  # 0
przyklad_modullo = 1 % 3  # 1
przyklad_modullo = 2 % 3  # 2
przyklad_modullo = 3 % 3  # 0
przyklad_modullo = 4 % 3  # 1
przyklad_modullo = 5 % 3  # 2
przyklad_modullo = 6 % 3  # 0
# -----------------------------
przyklad_modullo = a % b

# --------------------------------------------------------------------------------
