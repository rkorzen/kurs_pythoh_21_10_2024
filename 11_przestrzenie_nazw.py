"""
Model LEGB

Local

Enclosing

Global

Builtin

"""

dane = []
a = 1


def foo():
    """modyfikacja obiektu globalnego"""
    # global a

    dane.append("x")
    a = 2

    print("f locals", locals())
    print("f globals", globals())


print("g locals", locals())
print("g globals", globals())

print("a", a)
foo()
print("a", a)
print(dane)