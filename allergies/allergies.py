class Allergies(object):

    ALLERGENS = {1:"eggs", 2:"peanuts", 3:"shellfish", 4:"strawberries",
                 5:"tomatoes", 6:"chocolate", 7:"pollen", 8:"cats"}

    def __init__(self, number):
        self.number = number

    def is_allergic_to(self, string):
        return string in self.lst

    @property
    def lst(self):
        return [Allergies.ALLERGENS[k+1] for k in range(8)
                if self.number & (1 << k)]
