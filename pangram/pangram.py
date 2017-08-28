from string import ascii_lowercase


ALPHA = set(ascii_lowercase)


def is_pangram(s):
    return set(s.lower()).issuperset(ALPHA)
