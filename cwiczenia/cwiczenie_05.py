"""
Pobieraj od użytkownika liczby - do momentu w którym wpisze q lub po prostu enter.

Wypisz następujące informacje:
- ilość unikalnych liczb wpisanych przez użytkownika
- ilość liczb parzystych z zakresu 2-1000, które znalazły się w tej kolekcji
- średnią z liczb wpisanych przez użytkownika

"""

liczby = []

while True:
    d = input("Podaj liczbę lub q by zakonczyc: ")
    if not d or d == "q":
        break
    liczby.append(int(d))


unikalne = len(set(liczby))
srednia = sum(liczby) / len(liczby)

l_parzyste_2_1000 = range(2, 1001, 2)
l_parzyste_w_liczby = set(l_parzyste_2_1000) & set(liczby)

raport = f"""
unikalnych liczb: {unikalne}
liczb parzystych z zakresy 2-1000: {len(l_parzyste_w_liczby)}
średnia: {srednia}
"""

print(raport)

