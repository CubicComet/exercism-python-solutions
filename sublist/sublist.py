SUPERLIST = "superlist"
SUBLIST = "sublist"
EQUAL = "equal"
UNEQUAL = "unequal"


def check_lists(a, b):
    if a == b:
        return EQUAL
    elif is_sublist(a, b):
        return SUBLIST
    elif is_sublist(b, a):
        return SUPERLIST
    else:
        return UNEQUAL


def is_sublist(a, b):
    return a in [b[i:i + len(a)] for i in range(len(b) - len(a) + 1)]
