"""

Wczytaj plik dane/logs.txt

Policz czas przebywania w systemie dla każdego z użytkownikow

wypisz dane w porzadku malejacym

sorted(dane,  reverse=True)
dict()
d.get(klucz, domyslna_wartosc)

strip, split


"""

with open("dane/logs.log") as f:
    print(f.read())