def distance(a, b):
    if len(a) != len(b):
        raise ValueError
    return len([1 for (x,y) in zip(a,b) if x != y])
