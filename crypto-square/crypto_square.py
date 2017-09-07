import math


def encode(s):
    s = list(filter(str.isalnum, s.lower()))
    size = math.ceil(math.sqrt(len(s)))
    s += "." * (size**2 - len(s))
    parts = [s[i*size:(i+1)*size] for i in range(size)]
    return " ".join(map("".join, zip(*parts))).replace(".", "")
