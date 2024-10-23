from functools import wraps

def upiekszacz(func):

    @wraps(func)
    def opakowanie(*args, **kwargs):
        print("Upiekszam jakims dzialaniem przed")
        r = func(*args, **kwargs)
        print("Upiekszam jakims dzialanie po")
        return r

    # wraps robi za nas takie rzeczy:
    # opakowanie.__doc__ = func.__doc__
    # opakowanie.__name__ = func.__name__
    # opakowanie.__annotations__ = func.__annotations__
    return opakowanie


@upiekszacz
def foo():
    """To jest docstring funkcji foo"""
    print("Hello Play!")


@upiekszacz
def bar(x: int):
    return x+42

foo()
print(bar(10))

help(bar)