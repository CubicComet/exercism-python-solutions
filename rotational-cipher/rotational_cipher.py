import string


UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase


def rotate(s, n):
    return "".join(rot_gen(s,n))


def shift_rules(n):
    shifted = UPPER[n:] + UPPER[:n] + LOWER[n:] + LOWER[:n]
    return {k:v for k,v in zip(UPPER+LOWER, shifted)}


def rot_gen(s, n):
    rules = shift_rules(n)
    for ch in s:
        try:
            yield rules[ch]
        except KeyError:
            yield ch
