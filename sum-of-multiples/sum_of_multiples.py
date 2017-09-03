def sum_of_multiples(limit, factors):
    return sum(filter(lambda n: n < limit,
                      {f*i for i in range(1, limit) for f in factors}))
