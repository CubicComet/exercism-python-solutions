import math


def encode(s):
    s = "".join(filter(str.isalnum, s.lower()))
    size = math.ceil(math.sqrt(len(s)))
    return " ".join(s[i::size] for i in range(size))
