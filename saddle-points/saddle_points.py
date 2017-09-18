def saddle_points(m):
    mt = transpose(m)
    if not m == transpose(mt):
        raise ValueError
    return set((i, j) for i, row in enumerate(m) for j, col in enumerate(mt)
                if (row[j] == max(row) and col[i] == min(col)))


def transpose(m):
    return [list(col) for col in zip(*m)]
