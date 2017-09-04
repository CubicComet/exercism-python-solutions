def on_square(n):
    if n < 65:
        return 1 << (n - 1)
    else:
        raise ValueError


def total_after(n):
    if n and n < 65:
        return (1 << n) - 1
    else:
        raise ValueError
