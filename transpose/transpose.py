def transpose(inp):
    rows = inp.split("\n")
    max_len = max(map(len, rows))
    inp_square = [row + ((max_len-len(row)) * " ") for row in rows]
    new_rows = ["".join(tup) for tup in zip(*inp_square)]
    return "\n".join(reversed(list(partial_rstrip(reversed(new_rows)))))


def partial_rstrip(rows):
    flag = False
    for row in rows:
        if not flag:
            if not row.endswith(" "):
                flag = True
            yield row.rstrip()
        else:
            yield row
