import random
from collections import defaultdict


def largest_palindrome(max_factor, min_factor=0):
    return _palindromes(max_factor, min_factor, max)


def smallest_palindrome(max_factor, min_factor=0):
    return _palindromes(max_factor, min_factor, min)


def _palindromes(max_factor, min_factor, minmax):
    pals = defaultdict(set)

    for i in range(min_factor, max_factor+1):
        for j in range(min_factor, max_factor+1):
            p = i * j
            if is_palindrome(p):
                pals[p].add(tuple(sorted([i,j])))

    value = minmax(pals)
    factors = random.choice(list(pals[value]))
    return (value, factors)


def is_palindrome(n):
    return str(n) == str(n)[::-1]
