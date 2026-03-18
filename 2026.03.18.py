# Powtozenie nazjwazniejszych rzeczy

"""
1. Komentarze
-------------------------------------------------
"""

# Komentarze jedno linijkowe tworzymy w ten sposob

"""
Komentarze wielolinijkowe tworzymy w ten sposob
"""

"""
2. Funkcja print
-------------------------------------------------
Funckja print jest prosta w uzyciu funkcja - przyjmuje ona dowolna wartosc
i drukuje ja do konsoli - tak zwanego wyjscia standardowego

Przyklady:
"""
# print()  # wydrukuje pusta linie - zakonczona znakiem nowej linii \n
# print(5)  # wydrukuje 5
# print(5, "5", 13.0, [0, 1, 2])  # wydrukuje 5 5 13.0 [0, 1, 2]

"""
3. Funkcja input
-------------------------------------------------
Funkcja input to funckja ktora pobiera wartosc od 
uzytkownika przy uzyciu konsoli - tzw. wejscia standardowego.

Waznym jest aby pamietac ze zwracana wartosc jest ZAWSZE 
typu str (string - ciag tekstowy).

input moze przyjac poszczegolny argument - tekst wypisany 
zaraz przed wlaczeniem wejscia standardowego.

Przyklady:
"""
# zaciagnie wartosc od uzytkownika i zapisze do zmiennej
# user_value = input()

# wypisze "Podaj swoje imie", zaciagnie wartosc od uzytkownika i zapisze do zmiennej
# user_name = input("Podaj swoje imie")

"""
TODO:

4. Control Flow - wyrazenia while, if, for - do tego jeszcze nie doszlismy
"""

"""
5. Wyrazenia

Wyrażenia w Python to fragmenty kodu, 
które zwracają jakąś wartość (czyli coś obliczają).

Przyklady:
"""

# 2 + 3  # wynik: 5
# 10 / 2  # wynik: 5.0
# x = 5
# x * 2  # wynik: 10
# len("hello")  # wynik: 5
# 5 > 3  # wynik: True
# 10 == 2  # wynik: False
# x = 10
# "duże" if x > 5 else "małe"

"""
6. Operatory arytmetyczne

W pythonie posiadamy nastepujace operatory arytmetyczne:

- "+" - dodawanie
- "-" - odejmowanie
- "*" - mnozenie
- "/" - dzielenie
- "**" - potegowanie
- "//" - dzielenie calkowite
- "%" - modulo

Warto pamietac ze w pythonie posiadamy dwa szeroko uzywane (trzy lacznie)
typy wartosci liczbowych - int, float (oraz complex - o 
tym musza wiedziec tylko naukowcy i matematycy korzystajacy z jezyka).

Jezeli w wyrazeniu arytmetycznym wykorzystamy mieszanke typow, 
to wynik bedzie zostanie zwrocony w typie o najwyzszej wadze, 
wedlug ponizszej listy (im wyzej tym wieksza waga typu):

- complex
- float
- int
"""

"""
7. print() - kilka wyrazen

Przedstawione w punkcie 2. - mowa o tym ze print moze 
przyjmowac wiecej niz jeden argument
"""

"""
8. modulo

Mowa w punkcie 6.
"""

"""
9. zmienne

Zmienne to kontenery - pudla na wartosci zwracane 
przez wyrazenia, funkcje, itd.

Przechowuja wartosci pod nadana nazwa

Przyklady:
"""

# zmienna value przechowuje teraz wartosc "Some text"
# value = "Some text"
# uzywamy zmiennej value aby przekazac wartosc "Some text" do funkcji print()
# print(value)

"""
TODO:

10. Metody (funkcje)

Do tego jeszcze nie doszlismy - tzn. doszlismy do konceptu funkcji, 
ale nie dotknelismy czesci tematu w ktorej mowa jak sie je tworzy 
"""


"""
operacje na stringach

11. lower()
"SOME STRING".lower() -> "some string"
rowniez istnieje upper - inwersja lower:
"some string".upper() -> "SOME STRING"

12. captialize()
"some string".capitalize() -> "Some string"

13. title()
"some string".title() -> "Some String"

14. replace()
"some string".replace("some", "other") -> "other string"

15. swapcase()
"sOmE sTrInG".swapcase() -> "SoMe StRiNg"

16. strip()
"    some string    ".strip() -> "some string"
"lllllsome stringlllll".strip("l") -> "some string"

17. Konkatenacja stringow
print("some" + " " + "string") -> wypisze "some string"
mozna tez korzystac z f-stringow 
(czasami nazywane format stringami lub stringami interpolowanymi)

18. Mnozenie stringow
print("a" * 20) -> wypisze "aaaaaaaaaaaaaaaaaaaa"

"""

"""
19. Parametr sep - print
20. Parametr end - print

print() przyjmuje dwa dodatkowe argumenty kluczowe 
(podawane za pomoca klucza parametru - 
normlanie przyjmuje parametry pozycyjne)
Sa to:
- sep=<jakas_wartosc_string> - sep od angielskiego separator - pol. oddzielacz, 
    tekst uzywany do separowania wypisywanych do wyjscia standardowego argumentow, 
    domyslnie ustawiony na " " (pojedynczy znak spacji)
- end=<jakas_wartosc_string> - end - pol. koniec,
    tekst uzywane na samym koncu wypisywanego tekstu,
    domyslnie ustawiony na "\n" (pojedynczy znak nowej linii, odpowiednik enter)

Przyklady:
"""
# Wypisze:
# a b c<enter>
# print("a", "b", "c")

# Wypisze:
# a OOO b OOO c<enter>
# print("a", "b", "c", sep=" OOO ")

# Wypisze:
# a b c - koniec<enter>
# print("a", "b", "c", end=" - koniec\n")

# Wypisze:
# a OOO b OOO c - koniec<enter>
# print("a", "b", "c", sep=" OOO ", end=" - koniec\n")
