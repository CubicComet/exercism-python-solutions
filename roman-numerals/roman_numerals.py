def numeral(n):
    numerals = (n//1000) * "M"
    numerals += _numeral((n%1000)//100, "C", "D", "M")
    numerals += _numeral((n%100)//10, "X", "L", "C")
    numerals += _numeral(n%10, "I", "V", "X")
    return numerals


def _numeral(num, i, v, x):
    n, m = divmod(num, 5)
    if n == 1:
        return i + x if m == 4 else v + m * i
    else:
        return i + v if m == 4 else m * i
