class TriangleError(Exception):
    pass


class Triangle(object):
    def __init__(self, *dims):
        if not self.is_valid(dims):
            raise TriangleError("Invalid dimensions: {}".format(dims))
        self.dims = dims

    def kind(self):
        a, b, c = self.dims
        if a == b and b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"

    @staticmethod
    def is_valid(dims):
        if len(dims) != 3:
            return False
        a, b, c = dims
        return (a > 0 and b > 0 and c > 0) \
                and (a + b > c and a + c > b and b + c > a)
