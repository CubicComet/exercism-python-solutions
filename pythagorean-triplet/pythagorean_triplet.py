import math


def primitive_triplets(b):
    if b % 4 != 0:
        raise ValueError("Argument must be a multiple of 4")
    # triplets = []
    # for n in range(1, b//2 + 1):
    #     m, rem = divmod(b, 2*n)
    #     if m - n <= 0:
    #         continue
    #     if rem == 0:
    #         a = m**2 - n**2
    #         c = m**2 + n**2
    #         triplets.append(tuple(sorted((a, b, c))))

    return set(filter(are_coprime, _triplets(b)))


def _triplets(b):
    triplets = []
    for n in range(1, b//2 + 1):
        m, rem = divmod(b, 2*n)
        if m - n <= 0:
            continue
        if rem == 0:
            a = m**2 - n**2
            c = m**2 + n**2
            triplets.append(tuple(sorted((a, b, c))))
    return triplets


def are_coprime(tup):
    a, b, c = tup
    return math.gcd(a,b) == math.gcd(b,c) == math.gcd(c,a) == 1


def triplets_in_range(lower, upper):
    in_range = lambda x: lower <= min(x) and max(x) <= upper
    triplets = []
    for i in range(lower, 2*upper+1):
        if i % 4 == 0:
            triplets += _triplets(i)
    return set(filter(in_range, triplets))


def is_triplet(tup):
    a, b, c = sorted(tup)
    return a**2 + b**2 == c**2
