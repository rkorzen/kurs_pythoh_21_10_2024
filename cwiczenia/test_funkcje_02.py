import pytest
from funkcje_02 import wiecej_niz

@pytest.fixture
def text():
    return 'ala ma kota a kot ma ale'

def test_wiecej_niz_1():
    assert wiecej_niz('', 1) == set()

def test_wiecej_niz_2():
    assert wiecej_niz("aaabb", 2) == {"a"}

def test_wiecej_niz_3(text):
    assert wiecej_niz(text, 3) == {"a", " "}
