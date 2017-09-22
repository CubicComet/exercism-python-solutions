from collections import deque


class FactorsOutOfBounds(Exception):
    pass


def largest_palindrome(max_factor, min_factor=0):
    return _palindromes(max_factor, min_factor, deque.pop)


def smallest_palindrome(max_factor, min_factor=0):
    return _palindromes(max_factor, min_factor, deque.popleft)


def _palindromes(max_factor, min_factor, pop_minmax):
    pals = deque(filter(is_palindrome, range(min_factor**2, max_factor**2 + 1)))
    while pals:
        value = pop_minmax(pals)
        try:
            return (value, factor_pair(value, min_factor, max_factor))
        except FactorsOutOfBounds:
            pass
    raise NoPalindromes("No palindrome products found in the specified range")


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def factor_pair(n, min_factor, max_factor):
    for i in range(max([1, min_factor]), max_factor+1):
        if n % i == 0:
            j = n // i
            if min_factor <= j <= max_factor:
                return (i, j)
    raise FactorsOutOfBounds("There are no factors in that range")
