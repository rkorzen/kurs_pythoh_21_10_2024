import time


def moj_generator():
    yield 1
    yield 2

mgen = moj_generator()

print(next(mgen))
print(next(mgen))
# print(next(mgen))
print("w pętli")


for i in mgen:
    print(i)


def counter(i=1):
    while True:
        yield i ** 3
        i += 1

c = counter(10)

print(next(c))
print(next(c))
print(next(c))


# for i in c:
#     time.sleep(0.5)
#     print(i)


print([x for x in range(10)])
print((x for x in range(10)))