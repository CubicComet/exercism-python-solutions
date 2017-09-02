def square_of_sum(n):
    return square(sum(range(n+1)))


def sum_of_squares(n):
    return sum(map(square, range(n+1)))


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)


def square(n):
    return n*n
