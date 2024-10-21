"""
1. stworz zestaw danycgh opisujacy 3 pracownikoiw

imie, wiek, stawka


2. stworz zmienna ktora bedzie przechowywal "raport" o tych 3 osobach

3. uzyj print na tej zmiennej. Oczekiwany wynik to:


imie     wiek stawka
====================
Jan      32   200.00
Gabrysia 25   185.00
Zofia    33   220.24

"""
x, y = 1, 2
print(f"{x:<5} {y:6}")

imie_1 = "Jan"
imie_2 = "Gabrysia"
imie_3 = "Zofia"

wiek_1, wiek_2, wiek_3 = 32, 25, 33
stawka_1, stawka_2, stawka_3 = 200.00, 185.00, 220.24

raport_1 = f"{imie_1:10} {wiek_1:<4} {stawka_1:7.2f}"
raport_2 = f"{imie_2:10} {wiek_2:<4} {stawka_2:7.2f}"
raport_3 = f"{imie_3:10} {wiek_3:<4} {stawka_3:7.2f}"

raport = f"""{"imie":10} {"wiek":<4} {"stawka":7}
=======================
{raport_1}
{raport_2}
{raport_3}
"""

print(raport)

