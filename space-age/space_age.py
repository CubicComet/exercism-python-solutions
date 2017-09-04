class SpaceAge(object):
    YEARS = {"on_earth": 1,
             "on_mercury": 0.2408467,
             "on_venus": 0.61519726,
             "on_mars": 1.8808158,
             "on_jupiter": 11.862615,
             "on_saturn": 29.447498,
             "on_uranus": 84.016846,
             "on_neptune": 164.79132}

    def __init__(self, seconds):
        self.seconds = seconds

    @property
    def years(self):
        return self.seconds/31557600

    def __getattr__(self, on_planet):
        if on_planet in SpaceAge.YEARS:
            return lambda: round(self.years/SpaceAge.YEARS[on_planet], 2)
        else:
             raise AttributeError
