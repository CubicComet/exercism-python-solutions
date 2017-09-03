from string import ascii_lowercase, digits


ATBASH = {k: v for k, v in zip(ascii_lowercase + digits,
                               ascii_lowercase[::-1] + digits)}


def encode(s):
    encoded = atbash(s)


def decode(s):
    return atbash(s)


def atbash(s):
    return "".join(ATBASH.get(ch, "") for ch in s.lower())
