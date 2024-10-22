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
    text = "\n".join(args)
    for k, v in kwargs.items():
        text = text.replace(f"${k}", str(v))
    return text

t = foo(
    'koszt $cena PLN',
    'kwota $cena brutto',
    'podatek vat wynosi $vat',
    'moj zwierza to $kot',
    cena=10,
    vat=20,
    kot="mruczek"
)
print(t)