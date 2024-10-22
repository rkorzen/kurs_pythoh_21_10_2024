"""
Kalkulator bez użycia funkcji

Stworz prosty kalkulator dla dzialan +-/*

$ python kalkulator.py

Podaj rodzaj operacji (+-/*): +
Podaj arg 1: 1
Podaj arg 2: 4
Wynik: 5

"""

op = input("Podaj rodzaj operacji (+-/*): ")
a = int(input("Podaj arg 1: "))
b = int(input("Podaj arg 2: "))


if op == "+":
    wynik = a + b
elif op == "-":
    wynik = a - b
elif op == "*":
    wynik = a * b
elif op == "/":
    if b == 0:
        wynik = "Cholero nie dziel przez 0"
    else:
        wynik = a / b

print(f"Wynik: {wynik}")