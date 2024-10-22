import pytest
import unittest
def dzielenie(a, b):
    if b == 0:
        raise ValueError("Argument b nie może być 0")
    return a / b



def test_exception_is_raises_when_b_is_equal_0():
    with pytest.raises(ValueError):
        dzielenie(1, 0)


class TestDzielenie(unittest.TestCase):

    def test_exception_is_raises_when_b_is_equal_0(self):
        with self.assertRaises(ValueError):
            dzielenie(1, 0)