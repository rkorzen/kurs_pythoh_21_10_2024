"""
pip install pytest

Napisz funkcję zwracającą zbiór wszystkich znaków występujących w
napisie więcej niż zadana liczba razy.

Przykład użycia:
>> wiecej_niz('ala ma kota a kot ma ale', 3)
{'a', ' '}
"""


def wiecej_niz(text, prog):
    result = set()
    for znak in text:
        if text.count(znak) > prog:
            result.add(znak)
    return result



