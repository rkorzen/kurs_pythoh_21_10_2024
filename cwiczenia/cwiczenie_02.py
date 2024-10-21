"""
Jest plansza o wymiarach 100x100
Na podstawie połozenia zdefiniowanego w zmiennyc x i y
wypisz przybliżone położenie na planszy

"""

x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

# x = 9 i y = 95 = LGR
# x = 10 i y = 95 = GK

if x < 0 or y < 0 or x > 100 or y > 100:
    print("Poza plansza")
elif x < 10 and y > 90:
    print("GLR")
elif x > 90 and y > 90:
    print("GPR")
elif x > 90 and y < 10:
    print("DPR")
elif x < 10 and y < 10:
    print("DLR")
elif x < 10:
    print("LK")
elif x > 90:
    print("PK")
elif y < 10:
    print("DK")
elif y > 90:
    print("GK")
else:
    print("C")