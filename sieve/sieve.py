def sieve(n):
    return list(primes(n))


def primes(n):
    if n < 2:
        raise StopIteration
    yield 2
    not_prime = set()
    for i in range(3, n+1, 2):
        if i not in not_prime:
            yield i
        not_prime.update(range(i, n, i))
