import math


def nth_prime(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    _n = int(2 + 1.2 * n * math.log(n))
    return list(primes(_n))[n-1]


def primes(n):
    if n < 2:
        raise StopIteration
    yield 2
    not_prime = set()
    for i in range(3, n+1, 2):
        if i not in not_prime:
            not_prime.update(range(i*i, n+1, i))
            yield i
