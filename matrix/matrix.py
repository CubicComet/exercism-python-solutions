class Matrix(object):
    def __init__(self, s):
        self.rows = [list(map(int, row.split()))
                       for row in s.split("\n")]

    @property
    def columns(self):
        return [[row[i] for row in self.rows]
                for i in range(len(self.rows[0]))]
