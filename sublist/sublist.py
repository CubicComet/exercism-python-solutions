SUPERLIST = "superlist"
SUBLIST = "sublist"
EQUAL = "equal"
UNEQUAL = "unequal"


def check_lists(a, b):
    if a == b:
        return EQUAL
    _a = ";;".join(map(str, a))
    _b = ";;".join(map(str, b))
    if _a in _b:
        return SUBLIST
    elif _b in _a:
        return SUPERLIST
    else:
        return UNEQUAL
