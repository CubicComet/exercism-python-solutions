import operator
from functools import reduce


def largest_product(s, n):
    if s and not s.isnumeric():
        raise ValueError("Invalid character in string")

    return max(map(product, slices(s, n)))


def product(lst):
    return reduce(operator.mul, lst, 1)


def slices(s, n):
    m = len(s)
    if n > m:
        raise ValueError("Slice cannot be larger than the string")
    if n < 0:
        raise ValueError("Slices must have a positive non-zero length")

    return [list(map(int, s[i:i+n])) for i in range(m-n+1)]
