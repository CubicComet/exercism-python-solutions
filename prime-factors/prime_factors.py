import sieve


def prime_factors(n):
    primes = sieve.sieve(n)
    factors = []
    for p in primes:
        while n % p == 0:
            factors += [p]
            n //= p
    return factors
