import string


UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase


def rotate(s, n):
    rules = shift_rules(n)
    return "".join(rules.get(ch, ch) for ch in s)

def shift_rules(n):
    shifted = UPPER[n:] + UPPER[:n] + LOWER[n:] + LOWER[:n]
    return {k:v for k,v in zip(UPPER+LOWER, shifted)}
