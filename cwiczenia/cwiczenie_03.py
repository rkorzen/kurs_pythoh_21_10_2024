import sys
import math

# Sprawdzenie, czy zostały podane odpowiednie parametry
if len(sys.argv) != 4:
    print("Użycie: python nazwa_skryptu.py a b c")
    sys.exit(1)

# Pobieranie współczynników a, b, c
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

# Sprawdzenie, czy funkcja ma sens (a nie może być zerem)
if a == 0:
    print("To nie jest funkcja kwadratowa (a nie może być zerem).")
    sys.exit(1)

# Wyświetlanie równania
print(f"Rozwiązujemy równanie kwadratowe: {a}x^2 + {b}x + {c} = 0")

# Obliczanie delty
delta = b**2 - 4 * a * c

# Wyświetlanie obliczeń delty
print(f"\nObliczamy deltę, która jest kluczowa do znalezienia miejsc zerowych funkcji:")
print(f"Delta = b^2 - 4ac = ({b})^2 - 4 * {a} * {c}")
print(f"Delta = {b**2} - {4 * a * c} = {delta}")

# Rozstrzygnięcie w zależności od wartości delty
if delta > 0:
    print("\nPonieważ delta jest większa od zera, równanie ma dwa różne miejsca zerowe.")
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Obliczamy pierwiastki delty: √{delta} = {math.sqrt(delta)}")
    print(f"x1 = (-b - √delta) / 2a = (-{b} - {math.sqrt(delta)}) / (2 * {a}) = {x1}")
    print(f"x2 = (-b + √delta) / 2a = (-{b} + {math.sqrt(delta)}) / (2 * {a}) = {x2}")
    print(f"Funkcja ma dwa miejsca zerowe: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    print("\nPonieważ delta jest równa zero, równanie ma jedno podwójne miejsce zerowe.")
    x = -b / (2 * a)
    print(f"x = -b / 2a = -{b} / (2 * {a}) = {x}")
    print(f"Funkcja ma jedno miejsce zerowe: x = {x}")
else:
    print("\nPonieważ delta jest mniejsza od zera, równanie nie ma miejsc zerowych (brak rozwiązań rzeczywistych).")
