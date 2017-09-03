def sum_of_multiples(limit, factors):
    return sum({n for f in factors for n in range(f, limit, f)})
