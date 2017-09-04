def numeral(n):
    numerals = (n//1000) * "M"
    numerals += _numeral(((n%500)//100, (n%1000)//500), ("C", "D", "M"))
    numerals += _numeral(((n%50)//10, (n%100)//50), ("X", "L", "C"))
    numerals += _numeral(((n%5), (n%10)//5), ("I", "V", "X"))
    return numerals


def _numeral(nums, letters):
    i, v, x = letters
    if nums[1] == 1:
        return i + x if nums[0] == 4 else v + nums[0] * i
    else:
        return i + v if nums[0] == 4 else nums[0] * i
