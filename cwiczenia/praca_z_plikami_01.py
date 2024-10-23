"""

Wczytaj plik dane/logs.txt

Policz czas przebywania w systemie dla każdego z użytkownikow

wypisz dane w porzadku malejacym

sorted(dane,  reverse=True)
dict()
d.get(klucz, domyslna_wartosc)

strip, split


"""



def odczyt_danych(nazwa_pliku: str) -> list[tuple[str, str, int]]:
    """
    :param nazwa_pliku: Name of the file to read data from
    :return: A list of tuples where each tuple contains two strings and an integer extracted from the file
    """
    with open(nazwa_pliku) as f:
        data = f.read().splitlines()

    data = [d.split(";") for d in data]
    data = [(a, b, int(c)) for a, b, c in data]
    return data


def zrob_zliczenia(data: list[tuple[str, str, int]]) -> dict[str, int]:
    """
    :param data: A list of tuples where each tuple contains three elements:
                 a string representing the username,
                 a string representing the action ('LOGIN' or 'LOGOUT'),
                 and an integer representing the timestamp.
    :return: A dictionary where the keys are usernames and the values are the total time each user has been logged in.
    """
    calkowity_czas = {}
    ostatnie_zalogowanie = {}
    for wiersz in data:
        nick, action, t = wiersz
        if action == "LOGIN":
            ostatnie_zalogowanie[nick] = t

        elif action == "LOGOUT":
            calkowity_czas[nick] = (
                calkowity_czas.get(nick, 0) + t - ostatnie_zalogowanie[nick]
            )
    return calkowity_czas


def wyswietl_dane(dane: dict[str, int]) -> None:
    """
    :param dane: Dictionary containing user names as keys and the time spent in the system as values
    :return: None
    """
    for user, t in sorted(dane.items(), key=lambda x: x[1], reverse=True):
        print(f" - {user:8} spedził w systemie {t} s")


def main():
    data = odczyt_danych("../dane/logs.log")
    data = zrob_zliczenia(data)
    wyswietl_dane(data)


if __name__ == "__main__":
    main()