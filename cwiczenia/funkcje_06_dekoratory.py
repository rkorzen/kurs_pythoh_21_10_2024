import time


def foo():
    return [x**3 for x in range(1000000)]


def bar(r):
    return [x**3 for x in range(r)]

t = time.time()
func = foo
func()
print(f"uzycie funkcji {func.__name__} zajelo: {time.time() - t}s")


t = time.time()
func = bar
func(10000000)
print(f"uzycie funkcji {func.__name__} zajelo: {time.time() - t}s")
