"""

Napisz funkcję obliczającą liczbę znaków w zadanym napisie
pomiędzy zadanymi znakami. Znaki, pomiędzy którymi ma odbywać
się zliczanie, powinny być argumentami z wartościami domyślnymi -
odpowiednio < i >.

Nawiasy mogę być zagnieżdżone i mogą
wystąpić wiele razy. Znaki pomiędzy zagnieżdżonymi nawiasami
liczone są zgodnie z poziomem zagnieżdżenia.

sdsdsds = 0
sdsds<sd>sdsd = 2
0 1 2
a<a<b>> = 3

"""
import unittest


def policz_znaki(text, start="<", stop=">"):
    licznik = 0
    poziom = 0

    for char in text:
        if char == start:
            poziom += 1
        elif char == stop:
            poziom -= 1
        else:
            licznik += poziom
    return licznik



class TestZliczaZnaki(unittest.TestCase):

    def test_zlicz_znaki_dla_pustego_napis(self):
        self.assertEqual(policz_znaki(""), 0)

    def test_zlicz_znaki_jeden_poziom_zaglebieina(self):
        self.assertEqual(policz_znaki("a<aaa>"), 3)
        self.assertEqual(policz_znaki("a<a>"), 1)

    def test_zlicz_znaki_wiele_poziomow_zaglebienia(self):
        self.assertEqual(policz_znaki("a<<a>aa>"), 4)
        self.assertEqual(policz_znaki("<<<a<a>>>>"), 7)

    def test_zlicz_znaki_niestandardowe_start_i_stop(self):
        self.assertEqual(policz_znaki("[a]"), 0)
        self.assertEqual(policz_znaki("<[a]>", start="[", stop="]"), 1)


if __name__ == '__main__':
    unittest.main()