NUMS = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
        6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
        11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
        16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
        20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
        70:"seventy", 80:"eighty", 90:"ninety"}


def say(n):
    if not 0 <= n < 1e12:
        raise AttributeError("Number out of bounds")
    if n is 0:
        return "zero"

    number = ""

    b, rem = divmod(n, 1e9)
    m, rem = divmod(rem, 1e6)
    t, rem = divmod(rem, 1e3)

    if b:
        number += _say(b) + " billion "
    if m:
        number += _say(m) + " million "
    if t:
        number += _say(t) + " thousand "
    if rem:
        if (b or m or t) and (rem < 100):
            number += "and "
        number += _say(rem)

    return number.strip()


def _say(n):
    if n in NUMS:
        return NUMS[n]
    elif n < 100:
        tens, rem = divmod(n, 10)
        return NUMS[tens*10] + "-" + _say(rem)
    else:
        huns, rem = divmod(n, 100)
        hun_str = " hundred and " if rem else " hundred "
        return NUMS[huns] + hun_str + _say(rem)
