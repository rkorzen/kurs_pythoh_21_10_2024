def foo():
    ...

def hello(name="World"):
    return f"Hello {name}"


def add(a, b, *args, c=0, d=0, **kwargs ):
    print(f"a: {a}, b: {b}, args:{args}, kwargs: {kwargs}")
    return a + b + c + d + sum(args) + sum(kwargs.values())


def suma(a, b, *, to_string=False):
    result = a + b
    if to_string:
        return str(result)
    return result

if __name__ == '__main__':
    # region x
    assert foo() is None
    assert hello() == "Hello World"
    assert hello("Rafał") == "Hello Rafał"

    assert add(1, 2) == 3
    assert add(1, 2, 3) == 6
    assert add(1, 2, 3, 4) == 10
    assert add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) == 12


    assert add(a=1, b=2) == 3
    assert add(1, b=2,) == 3
    assert add(b=1, a=2) == 3

    assert add(a=1, b=2, c=3) == 6
    # endregion

    assert suma(1, 2) == 3

    # assert suma(1, 2, True) == "3"

    assert suma(1, 2, to_string=True) == "3"
    assert suma(1, 2, to_string=1) == "3"
