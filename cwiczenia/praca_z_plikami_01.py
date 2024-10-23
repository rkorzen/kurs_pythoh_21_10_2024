"""

Wczytaj plik dane/logs.txt

Policz czas przebywania w systemie dla każdego z użytkownikow

wypisz dane w porzadku malejacym

sorted(dane,  reverse=True)
dict()
d.get(klucz, domyslna_wartosc)

strip, split


"""

calkowity_czas = {}
ostatnie_zalogowanie = {}

with open("../dane/logs.log") as f:
    for wiersz in f:
        nick, action, t = wiersz.strip().split(";")
        t = int(t)

        if action == "LOGIN":
            ostatnie_zalogowanie[nick] = t

        elif action == "LOGOUT":
            calkowity_czas[nick] = calkowity_czas.get(nick, 0) + t - ostatnie_zalogowanie[nick]

print(ostatnie_zalogowanie)
print(calkowity_czas)

print()

for user, t in sorted(calkowity_czas.items(), key=lambda x: x[1], reverse=True):
    print(f" - {user:8} spedził w systemie {t} s")

