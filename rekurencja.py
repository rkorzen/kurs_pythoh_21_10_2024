
# 5! = 5*4!
# 0! = 1

def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n-1)

print(silnia(5))


def counter(n):
    print(n)
    counter(n+1)

counter(1)