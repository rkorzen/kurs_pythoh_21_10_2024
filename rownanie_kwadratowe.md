### Zadanie: Obliczanie miejsc zerowych funkcji kwadratowej

Napisz program w Pythonie, który obliczy miejsca zerowe funkcji kwadratowej o postaci:

$ax^2 + bx + c = 0$


#### Szczegóły:

1. Program powinien przyjmować współczynniki \(a\), \(b\), i \(c\) jako argumenty wiersza poleceń.
2. Oblicz deltę ( $\Delta = b^2 - 4ac $) i wyświetl ją wraz z wyjaśnieniem kroków obliczeń.
3. Na podstawie delty rozstrzygnij liczbę miejsc zerowych funkcji:
   - Jeśli $ \Delta > 0 $, oblicz i wyświetl dwa różne miejsca zerowe.
   - Jeśli $ \Delta = 0 $, oblicz i wyświetl jedno podwójne miejsce zerowe.
   - Jeśli $ \Delta < 0 $, wyświetl informację, że brak jest miejsc zerowych (brak rozwiązań rzeczywistych).
4. Program powinien dokładnie wyświetlać kroki, w tym:
   - Obliczenie delty z wyjaśnieniem wzoru.
   - Obliczenie miejsc zerowych (lub informację o ich braku) na podstawie delty.

#### Przykład działania:

Dla równania kwadratowego $x^2 - 3x + 2 = 0$, program powinien wyświetlić:

```
Rozwiązujemy równanie kwadratowe: 1x^2 + -3x + 2 = 0

Obliczamy deltę, która jest kluczowa do znalezienia miejsc zerowych funkcji:
Delta = b^2 - 4ac = (-3)^2 - 4 * 1 * 2
Delta = 9 - 8 = 1

Ponieważ delta jest większa od zera, równanie ma dwa różne miejsca zerowe.
Obliczamy pierwiastki delty: √1 = 1
x1 = (-b - √delta) / 2a = (--3 - 1) / (2 * 1) = 1
x2 = (-b + √delta) / 2a = (--3 + 1) / (2 * 1) = 2
Funkcja ma dwa miejsca zerowe: x1 = 1, x2 = 2
```

Dla równania $x^2 + 4x + 4 = 0$:

```
Rozwiązujemy równanie kwadratowe: 1x^2 + 4x + 4 = 0

Obliczamy deltę, która jest kluczowa do znalezienia miejsc zerowych funkcji:
Delta = b^2 - 4ac = (4)^2 - 4 * 1 * 4
Delta = 16 - 16 = 0

Ponieważ delta jest równa zero, równanie ma jedno podwójne miejsce zerowe.
x = -b / 2a = -4 / (2 * 1) = -2
Funkcja ma jedno miejsce zerowe: x = -2
```

Dla równania $x^2 + 2x + 5 = 0$:

```
Rozwiązujemy równanie kwadratowe: 1x^2 + 2x + 5 = 0

Obliczamy deltę, która jest kluczowa do znalezienia miejsc zerowych funkcji:
Delta = b^2 - 4ac = (2)^2 - 4 * 1 * 5
Delta = 4 - 20 = -16

Ponieważ delta jest mniejsza od zera, równanie nie ma miejsc zerowych (brak rozwiązań rzeczywistych).
```

