SUPERLIST = "superlist"
SUBLIST = "sublist"
EQUAL = "equal"
UNEQUAL = "unequal"

VERY_UNLIKELY_STRING = "ꗲꅯḪꍙ"


def check_lists(a, b):
    if a == b:
        return EQUAL
    _a = VERY_UNLIKELY_STRING.join(map(str, a))
    _b = VERY_UNLIKELY_STRING.join(map(str, b))
    if _a in _b:
        return SUBLIST
    elif _b in _a:
        return SUPERLIST
    else:
        return UNEQUAL
