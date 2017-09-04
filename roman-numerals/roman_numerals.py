def numeral(arabic):
    m, rem = divmod(arabic, 1000)
    d, rem = divmod(rem, 500)
    c, rem = divmod(rem, 100)
    l, rem = divmod(rem, 50)
    x, rem = divmod(rem, 10)
    v, i = divmod(rem, 5)

    numerals = m * "M"
    numerals += _numeral((c, d), ("C", "D", "M"))
    numerals += _numeral((x, l), ("X", "L", "C"))
    numerals += _numeral((i, v), ("I", "V", "X"))
    return numerals


def _numeral(nums, letters):
    i, v, x = letters
    if nums[1] == 1:
        return i + x if nums[0] == 4 else v + nums[0] * i
    else:
        return i + v if nums[0] == 4 else nums[0] * i
