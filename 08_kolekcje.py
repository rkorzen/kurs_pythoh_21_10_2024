# tuple (krotka)
napis = "1234a"
print(tuple())
#         0  1  2  3  4
krotka = (1, 2, 3, 4, "a")

# list (lista)
lista = [1, 2, 3, 4, "a"]

print("krotka", dir(krotka))
print("lista", dir(lista))

print(krotka.count(0))
# print(krotka.index("b"))

print(len(krotka))
print(len(lista))


print(napis[4])
print(krotka[4])
print(lista[4])


# tu widac roznice miedzy mutwalny a niemutowalny
# krotka[4] = "b"  # to daje blad
lista[4] = "b"

print(lista)

# slicing
#          01234
napis = "1234sdsd2edw2eda"
print(napis[1:len(napis)-1])
print(napis[1:-1:3])
print(napis[::-1])

# IndexError - dla indeksu ktory nie istnieje
# print(napis[2222])

print(dir(lista))
print(id(lista))
lista.append(102)
print(id(lista))

lista = lista + [100, 10002]
print(id(lista))

print(lista)

print(lista.pop())
print(lista)

# stos w oparciu o listy jest prosty i wydajny
# LIFO


# koleji w oparciu list nie jest wydajne

# print(help(lista.pop))

print(lista.pop(0))
print(lista)


# set (zbior)

{1, 2, 3}

set()


# dict (slownik)

{1: "a" , 2: "b"}

dict()

print(type({}))
print(hash((1, 2, 3,2,3,4,5,5,6,7,8,8,9,9,90)))
print(([1, 2, 3], "a"))
x = ("a")
print(x)

{x}


## range()

# help(range)

print(range(10))
print(list(range(10)))

print(range(10, 20))
print(list(range(10, 20)))

print(range(10, 20, 2))
print(list(range(10, 20, 2)))

## comprehensions - idiomy pythonowe

lista = dir([])
print(lista)

print([x for x in lista if not x.startswith("__")])
print({y**3 for y in range(1, 100, 10)})

#

a = {1, 2, 3}
b = {2, 3, 4}
c = {2, 3}

print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(a ^ b)

print(b.issuperset(c))
print(c.issubset(b))


