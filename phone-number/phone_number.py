import re


class Phone(object):
    def __init__(self, n):
        cleaned = "".join(filter(str.isnumeric, n))
        m = re.match("^(1)?([2-9][0-9]{2})([2-9][0-9]{2})([0-9]{4})$", cleaned)
        if m:
            self._parts = [p if p else "" for p in m.groups()]
        else:
            self._parts = ("", "000", "000", "0000")

    def area_code(self):
        return self._parts[1]

    def pretty(self):
        return "({1}) {2}-{3}".format(*self._parts)

    @property
    def number(self):
        return "{1}{2}{3}".format(*self._parts)
