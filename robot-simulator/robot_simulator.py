import math

# Create globals for the bearings
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


# Define simpler int-only sine and cosine functions
def sin(deg):
    return int(math.sin(math.radians(deg)))

def cos(deg):
    return int(math.cos(math.radians(deg)))


class Robot(object):
    def __init__(self, bearing=NORTH, x_pos=0, y_pos=0):
        self.bearing = bearing
        self._x = x_pos
        self._y = y_pos
        self._METHODS = {"R": self.turn_right,
                        "L": self.turn_left,
                        "A": self.advance}

    def turn_right(self):
        self.bearing = (self.bearing - 90) % 360

    def turn_left(self):
        self.bearing = (self.bearing + 90) % 360

    def advance(self):
        self._x += cos(self.bearing)
        self._y += sin(self.bearing)

    def simulate(self, commands):
        for command in commands:
            self._METHODS[command]()

    @property
    def coordinates(self):
        return (self._x, self._y)
