def prime_factors(n):
    factors = []
    factor = 2
    while n != 1:
        while n % factor == 0:
            factors += [factor]
            n //= factor
        factor += 1
    return factors
