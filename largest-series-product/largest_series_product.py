import operator
from functools import reduce

import series # series.py symbolically linked in current folder


def largest_product(s, n):
    if s and not s.isnumeric():
        raise ValueError("Invalid character in string")

    return 1 if n == 0 else max(map(product, series.slices(s, n)))


def product(lst):
    return reduce(operator.mul, lst, 1)
