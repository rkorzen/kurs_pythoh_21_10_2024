print(int())
print(float())
print(bool(0), bool(0.0))

print(0.1 + 0.1 + 0.1 == 0.3)

print(0.1 + 0.1 + 0.1)

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") == Decimal("0.3"))


print(1.67e309)
print(float("-inf"))
print(float("-inf") < 10 < float("inf"))
print(float("-inf") < float("nan") < float("inf"))
print(float("nan") == float("nan"))


print(1.23e100)