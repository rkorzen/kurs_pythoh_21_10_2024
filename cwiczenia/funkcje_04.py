"""

Zaimplementuj funkcję formatującą podane napisy.
Przykład użycia:

formatuj(
    'koszt $cena PLN',
    'kwota $cena brutto',
    'podatek vat wynosi $vat',
    cena=10,
    vat=20
)
'koszt 10 PLN\nkwota 10 brutto\npodatek vat wynosi 20


formatuj(
    'koszt $x PLN',
    x=10,
)
'koszt 10 PLN

"""

def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(
    'koszt $cena PLN',
    'kwota $cena brutto',
    'podatek vat wynosi $vat',
    cena=10,
    vat=20
)

text = "koszt $cena PLN"
print(text.replace("$cena", "10"))

texty = ['koszt $cena PLN',
    'kwota $cena brutto',
    'podatek vat wynosi $vat',]


print("-".join(texty))