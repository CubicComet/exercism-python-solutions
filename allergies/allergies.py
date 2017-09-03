class Allergies(object):

    ALLERGENS = [(1,"eggs"), (2,"peanuts"), (4,"shellfish"), (8,"strawberries"),
                 (16,"tomatoes"), (32,"chocolate"), (64,"pollen"), (128,"cats")]

    def __init__(self, number):
        self.number = number

    def is_allergic_to(self, string):
        return string in self.lst

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, n):
        self._number = n
        self._lst = [v for k, v in Allergies.ALLERGENS if n & k]

    @property
    def lst(self):
        return self._lst
