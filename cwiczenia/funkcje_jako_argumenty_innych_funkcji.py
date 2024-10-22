"""
Zaimplementuj funkcję przycinającą listę na podstawie podanego
warunku początkowego oraz końcowego:
Przykład użycia:

przytnij(
    data=[1, 2, 3, 4, 5, 6, 7],
    start=lambda x: x > 3,
    stop=lambda x: x == 6,
    )

[4, 5, 6]

"""


def przytnij(data, start, stop):
    result = []
    for el in data:
        if start(el):
            result.append(el)
        if stop(el):
            break

    return result


assert przytnij(
    data=[1, 2, 3, 4, 5, 6, 7], start=lambda x: x > 3, stop=lambda x: x == 6
) == [4, 5, 6]


assert przytnij(
    data=[1, 2, 3, 4, 5, 6, 7], start=lambda x: x > 5, stop=lambda x: x == 6
) == [6]


def parzyste(x):
    return x % 2 == 0

def rowne_6(x):
    return x == 6

print(przytnij(
    data=[1, 2, 3, 4, 5, 6, 7], start=parzyste, stop=lambda x: x == 6
))
