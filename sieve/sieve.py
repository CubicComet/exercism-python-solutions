def sieve(n):
    return list(primes(n))


def primes(n):
    if n < 2:
        raise StopIteration
    yield 2
    not_prime = set()
    for i in range(3, n+1, 2):
        if i not in not_prime:
            not_prime.update(range(i*i, n+1, i))
            yield i
