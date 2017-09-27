class TriangleError(Exception):
    pass


class Triangle(object):
    def __init__(self, *dims):
        if not self.is_valid(dims):
            raise TriangleError("Invalid dimensions: {}".format(dims))
        self.dims = sorted(dims)

    def kind(self):
        a, b, c = self.dims
        if a == b and b == c: # implies a == c
            return "equilateral"
        elif a == b or b == c: # sorted, so a < c here unless a == c above
            return "isosceles"
        else:
            return "scalene"

    @staticmethod
    def is_valid(dims):
        if len(dims) != 3:
            raise ValueError("Triangles have 3 sides")
        a, b, c = sorted(dims)
        return a > 0 and a + b > c
