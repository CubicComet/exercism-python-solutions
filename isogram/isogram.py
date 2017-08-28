from string import ascii_lowercase


LOWERCASE = set(ascii_lowercase)


def is_isogram(s):
    chars = [c for c in s.lower() if c in LOWERCASE]
    return len(chars) == len(set(chars))


# You could also achieve this using "c.isalpha()" instead of LOWERCASE
# You would then not need to import from `string`, but it's marginally slower
