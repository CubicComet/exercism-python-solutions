import random
import string


class Robot(object):
    USED_NAMES = set()

    def __init__(self):
        self.new_name()

    def reset(self):
        old_name = self.name
        self.new_name()
        self.USED_NAMES.remove(old_name)
        # Personally, I would remove the old name from the set before
        # generating a new one, but the tests require that I do it the other
        # way around (or not do it).

    def new_name(self):
        name = "".join(self._name_format())
        if name in self.USED_NAMES:
            self.new_name()
        else:
            self.USED_NAMES.add(name)
            self.name = name

    @staticmethod
    def _name_format():
        for i in range(2):
            yield random.choice(string.ascii_uppercase)
        for i in range(3):
            yield random.choice(string.digits)
