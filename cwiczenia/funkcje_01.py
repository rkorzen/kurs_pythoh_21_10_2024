
def czy_jest_pierwsza(liczba):
    """
    Napisz funkcję sprawdzającą, czy dane liczba jest liczbą pierwszą.
    Przykład użycia:

    >>> czy_jest_pierwsza(1)
    False
    >>> czy_jest_pierwsza(-1)
    False
    >>> czy_jest_pierwsza(2)
    True
    >>> czy_jest_pierwsza(10)
    False
    >>> czy_jest_pierwsza(17)
    True
    >>> czy_jest_pierwsza(11)
    True

    # wywołanie testów:
    python -m doctest sciezka/do/pliku

    x % y == 0
    """

    if liczba < 2:
        return False

    for dzielnik in range(2, liczba):
        if liczba % dzielnik == 0:
            return False
    return True

