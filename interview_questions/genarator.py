def gen(n):
    number = 0

    while number < n:
        yield number
        number += 1

seq = gen(5)

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))