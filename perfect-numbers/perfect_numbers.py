from math import sqrt, ceil


def divisor_generator(n):
    yield 1
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            yield i
            yield n // i


def is_perfect(n):
    return n == sum(divisor_generator(n))
