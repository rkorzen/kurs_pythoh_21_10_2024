"""
Zaimplementuj funkcję spłaszczającą podaną listę.
Przykład użycia:

splaszcz([1, 2, 3, [4, 5, [6]], 7])

[1, 2, 3, 4, 5, 6, 7]

"""


def splaszcz(lista):
    wynik = []
    for el in lista:
        # if type(el) == list:
        if isinstance(el, list):
            wynik.extend(splaszcz(el))
        else:
            wynik.append(el)

    return wynik


def test_splaszcz():
    assert splaszcz([]) == []
    assert splaszcz([1, 2, 3]) == [1, 2, 3]
    assert splaszcz([1, [2, 3]]) == [1, 2, 3]
    assert splaszcz([1, [2, [3]], 4]) == [1, 2, 3, 4]


