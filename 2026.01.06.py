# Typy w pythone, czesc dalsza
# 2. Liczby zmiennoprzecinkowe
# - w pythonie oznaczane slowem 'float' (od ang. floating point number)

a = 7.0
b = 2.0

suma = a + b  # 9.0
roznica = a - b  # 5.0
iloczyn = a * b  # 14.0
iloraz = a / b  # 3.5
iloraz_calkowity = a // b  # 3.0
modulo = a % b  # 1.0
potega = a**b  # 49.0

print(suma, roznica, iloczyn, iloraz, iloraz_calkowity, modulo, potega)

# ----------
# Type casting

print("Hello world!")
a = float(5)
print(f"a = {a}")

# -------------
#
# Konstruktory typow to takie funkcje ktore
# pozwalaja nam na zamiane jednego typu na drugi
#
# - int - posiada konstruktor 'int(x)' - na podanym argumencie x dojdzie
#   proba do zamiany go na wartosc calkowita, np.:
#   - int(5) -> 5
#   - int(5.0) -> 5
#   - int(5.3) -> 5
#   - int(5.7) -> 5
#   - int("13") -> 13
# - float - posiada kontruktor 'float(x)' - na podanym argumencie x dojdzie
#   proba do zamany go na wartosc zmiennoprzecinkowa, np.:
#   - float(4.3) -> 4.3
#   - float(5) -> 5.0
#   - float("13") -> 13.0
#   - float("13.0") -> 13.0
#
# -------------

# 3. String (Wartosci tekstowe)
# str - od ang. string, dokladnie string-of-characters (ciag znakow)
# str(x)
# - str(5.0) -> "5.0"
# - str("hello world") -> "hello world"
# - str(3) -> "3"
# - str(-13) -> "-13"

imie = input("Podaj swoje imie:")
print("Hej,", imie)

# Zadanie 1
# Napisz program ktory korzysta z funkcji input oraz
# print i dodaje do siebie dwie podane przez uzytkownika liczby

a_str = input("podaj liczbe a: ")
b_str = input("podaj liczbe b: ")
a = float(a_str)
b = float(b_str)
print(a + b)
