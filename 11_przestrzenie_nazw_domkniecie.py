
a = 1


def foo():
    b = 2

    def bar():
        nonlocal b
        b = 3

    print(b)
    bar()
    print(b)

foo()


def create_incr(step):

    def incr(liczba):
        return liczba + step

    return incr


incr_by_10 = create_incr(10)
incr_by_2 = create_incr(2)
print(incr_by_10(121))
print(incr_by_2(121))
