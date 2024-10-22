"""
Kalkulator bez użycia funkcji

Stworz prosty kalkulator dla dzialan +-/*

$ python kalkulator.py

Podaj rodzaj operacji (+-/*): +
Podaj arg 1: 1
Podaj arg 2: 4
Wynik: 5

"""

number = int | float

def add(a: number, b: number) -> number:
    """
    :param a: The first number to add.
    :param b: The second number to add.
    :return: The sum of the two numbers.
    """
    return a + b

def sub(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cholero nie dziel przez 0"
    return a / b

func = add
if __name__ == "__main__":
    print(__name__)
    op = input("Podaj rodzaj operacji (+-/*): ")
    a = int(input("Podaj arg 1: "))
    b = int(input("Podaj arg 2: "))

    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }

    func = operations[op]

    wynik = func(a, b)

    print(f"Wynik: {wynik}")

    add(1, 2)
    add(1.1, 2.2)
    add("1", "2")