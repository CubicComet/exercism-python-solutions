import math


def primitive_triplets(b):
    if b % 4 != 0:
        raise ValueError("Argument must be a multiple of 4")
    return set(filter(are_coprime, _triplets(b)))


def triplets_in_range(lower, upper):
    in_range = lambda x: lower <= min(x) and max(x) <= upper
    base_triplets = []
    for i in range(4, upper, 4):
        base_triplets += _triplets(i)
    triplets = base_triplets.copy()
    for i in range(2, upper//5+1):
        multiply = lambda y: y*i
        trip_multiply = lambda x: tuple(map(multiply, x))
        triplets += map(trip_multiply, base_triplets)
    return set(filter(in_range, triplets))


def is_triplet(tup):
    a, b, c = sorted(tup)
    return a**2 + b**2 == c**2


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
