class Luhn(object):
    def __init__(self, number):
        self.number = number.replace(" ", "")

    def is_valid(self):
        if len(self.number) < 2 or not self.number.isdigit():
            return False
        numbers = map(int, reversed(self.number))
        return sum(map(Luhn._double, enumerate(numbers))) % 10 == 0

    @staticmethod
    def _double(i_n):
        i, n = i_n
        if i % 2 == 0:
            x = n
        else:
            x = 2 * n
            if x > 9:
                x -= 9
        return x
