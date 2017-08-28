from string import ascii_lowercase


LOWERCASE = set(ascii_lowercase)


def is_isogram(s):
    chars = [c for c in s.lower() if c in LOWERCASE]
    return len(chars) == len(set(chars))
