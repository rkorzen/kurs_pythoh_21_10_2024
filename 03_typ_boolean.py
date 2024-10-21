print(True)
print(False)

print("False")

print(str(True))

print(bool("False"))
print(bool(""))
print("="*80)

print(not True)
print(True and False)
print(True and True)

print(True or False)

x = 1
print(x < 0 or x % 2 == 0)  # False or False
print("="*80)

warunek = x < 0
# warunek = 1
x = warunek
# warunek to zmienna, nazwa, referencja

print(warunek == True)  # 1 == True
print(warunek is True)  # 1 is True
warunek2 = False
print(warunek2 == False)  # 0 == False
print(warunek2 is False)  # 0 is False

print(warunek is x)

print(id(warunek), id(x), id(False), id(True), sep="\n")

print(1 + True)


print(help(bool))