class Matrix(object):
    def __init__(self, s):
        self.rows = [list(map(int, row.split()))
                       for row in s.split("\n")]

    @property
    def columns(self):
        return [list(col) for col in zip(*self.rows)]
