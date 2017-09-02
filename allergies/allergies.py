class Allergies(object):

    ALLERGENS = {1:"eggs", 2:"peanuts", 4:"shellfish", 8:"strawberries",
                 16:"tomatoes", 32:"chocolate", 64:"pollen", 128:"cats"}

    def __init__(self, number):
        self.number = number

    def is_allergic_to(self, string):
        return string in self.lst

    @property
    def lst(self):
        return [Allergies.ALLERGENS[k] for k in Allergies.ALLERGENS.keys()
                if self.number & k] # uses bit-wise comparison
