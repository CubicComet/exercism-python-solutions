def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors += [2]
        n //= 2
    factor = 3
    while n != 1:
        while n % factor == 0:
            factors += [factor]
            n //= factor
        factor += 2
    return factors
