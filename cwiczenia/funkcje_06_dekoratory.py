import time
from functools import wraps


def timeit(func):

    @wraps(func)
    def opakowanie(*args, **kwargs):
        t = time.time()
        r = func(*args, **kwargs)
        print(f"uzycie funkcji {func.__name__} zajelo: {time.time() - t}s")
        return r

    return opakowanie



@timeit
def foo():
    return [x**3 for x in range(1000000)]

@timeit
def bar(r):
    return [x**3 for x in range(r)]
#
# t = time.time()
# func = foo
# func()
# print(f"uzycie funkcji {func.__name__} zajelo: {time.time() - t}s")
#
#
# t = time.time()
# func = bar
# func(10000000)
# print(f"uzycie funkcji {func.__name__} zajelo: {time.time() - t}s")


foo()

bar(1000000)
