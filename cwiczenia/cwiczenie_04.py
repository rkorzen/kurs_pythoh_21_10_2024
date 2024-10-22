"""
W zadanym napisie policz wystąpienia każdego ze znaków
Wynik przechowaj w słowniku

"""
text = "W zadanym napisie policz wystąpienia każdego ze znaków Wynik przechowaj w słowniku"

zliczenia = {}

for znak in text:
    if znak in zliczenia:
        zliczenia[znak] += 1
    else:
        zliczenia[znak] = 1

print(zliczenia)

# rozw 2:

zliczenia = {}

for znak in text:
    zliczenia[znak] = zliczenia.get(znak, 0) + 1

print(zliczenia)

# rozw 3:

# import collections
from collections import defaultdict  as dd1

# zliczenia = collections.defaultdict(int)
zliczenia = dd1(int)

for znak in text:
    zliczenia[znak] += 1  # zliczenia[znak] = zliczenia[znak] + 1

print(dict(zliczenia))

# rozw 4:
from collections import Counter

print(Counter(text))
