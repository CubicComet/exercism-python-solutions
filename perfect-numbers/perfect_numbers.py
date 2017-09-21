def divisor_generator(n):
    big_factors = {1}
    for i in range(2, n):
        if i in big_factors:
            break
        if n % i == 0:
            big_factors.add(n // i)
            yield i
    yield from big_factors


def is_perfect(n):
    return n == sum(divisor_generator(n))
