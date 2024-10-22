from kalkulator_02 import add, mul, div, sub
add.x = "szabanascie"
print(dir(add))

print(add.__annotations__)
print(add.__doc__)

help(add)

add(1)
dane_a = [1, 2, 3]
dane_b = [2, 3, 4]

functions = [add, mul, div, sub]


for func in functions:
    for a, b in zip(dane_a, dane_b):
        print(func(a, b))
