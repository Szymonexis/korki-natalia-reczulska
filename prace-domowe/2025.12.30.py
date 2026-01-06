# Napisz program w ktorym obliczysz wartosc
# funkcji liniowej dla dwoch wartosci x_1 oraz x_2
# Wzor funkcji to f(x) = 2*x - 17
# Badane punkty to:
# - x_1 = 13
# - x_2 = 7
#
# Nie musisz tworzyc zadnych funkcji dodatkowych,
# co chce zebys zrobila to wypisala wzor funkcji
# podstawiajac w miejsce x odpowiednia zmienna (x_1 lub x_2)
# oraz zapisala wartosci funkcji dla danego
# punktu x do nowej zmiennej, tzn.
# - dla x_1 zapisz wynik funkcji do nowej zmiennej o nazwie y_1
# - dla x_2 zapisz wynik funkcji do nowej zmiennej o nazwie y_2
#
# Wypisz obie wartosci y_1 oraz y_2 oraz wylicz i wypisz ich:
# - sume
# - roznice
# - iloczyn (mnozenie)
# - iloraz (dzielenie)
# - iloraz calkowity (dzielenie calkowite)
# - modulo (reszte z dzielenia)
#
# Jezeli zadanie jest zbyt pogmatwane lub czegos nie
# rozumiesz, napisz do mnie, sprobuje pomoc
#
# Powodzenia :)

x_1 = 13
x_2 = 7

y_1 = 2 * x_1 - 17
y_2 = 2 * x_2 - 17

print(y_1, y_2)

suma = y_1 + y_2
roznica = y_1 - y_2
iloczyn = y_1 * y_2
iloraz = y_1 / y_2
iloraz_calkowity = y_1 // y_2
modulo = y_1 % y_2

print(suma, roznica, iloczyn, iloraz, iloraz_calkowity, modulo)
