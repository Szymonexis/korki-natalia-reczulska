# Typy danych w Pythonie
# 1. Liczby calkowite - (eng. Intigers) - int
# - moga byc wartosci od okolo -4294967296 do okolo 4294967296
# - tworzy sie je bez uzycia przecinka
# - mozna je dodawac, odejmowac, dzielic, mnozyc, potegowac, itd.

a = 2
b = 3

# dodawanie
print(a + b)  # jezeli oba argumenty sa typu int to wynik tez bedzie int

# odejmowanie
print(a - b)  # jezeli oba argumenty sa typu int to wynik tez bedzie int

# mnozenie
print(a * b)  # jezeli oba argumenty sa typu int to wynik tez bedzie int

# dzielenie
print(
    a / b
)  # nawet jezeli oba argumenty sa typu int to wynik moze nie byc typu int (!!!)

# dzielnie calkowite
print(a // b)  # jezeli oba argumenty sa typu int to wynik tez bedzie int

# reszta z dzielenia (modulo)
print(a % b)  # jezeli oba argumenty sa typu int to wynik tez bedzie int

# potegowanie
# print(a ^ b)    # UWAGA: ^ to nie jest operator potegowania, jest to operator XOR !!!
print(a**b)

wynik_z_dzielenia = a / b
wynik_z_mnozenia = a * b
wynik_z_odejmowania = a - b
wynik_z_dodawania = a + b
