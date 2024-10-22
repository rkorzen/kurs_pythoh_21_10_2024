"""
pip install pytest

Napisz funkcję zwracającą zbiór wszystkich znaków występujących w
napisie więcej niż zadana liczba razy.

Przykład użycia:
>> wiecej_niz('ala ma kota a kot ma ale', 3)
{'a', ' '}


"""


def wiecej_niz(text, prog):
    pass


def test_wiecej_niz_1():
    assert wiecej_niz('', 1) == set()

def test_wiecej_niz_2():
    assert wiecej_niz("aaabb", 2) == {"a"}

def test_wiecej_niz_3():
    assert wiecej_niz('ala ma kota a kot ma ale', 3) == {"a", " "}

