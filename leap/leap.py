def is_leap_year(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

# Alternatively, we can use the below, but it's slightly slower.
#    return (not y % 400) or (bool(y % 4)^bool(y % 100))
