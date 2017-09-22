import re


class InvalidBoard(ValueError):
    pass


def board(b):
    if not is_valid_board(b):
        raise InvalidBoard("Board is malformed and thus invalid")
    b = [[ch for ch in row] for row in b]
    for i in range(1, len(b)-1):
        for j in range(1, len(b[0])-1):
            if b[i][j] == " ":
                m = "".join(b[i-1][j-1:j+2] + b[i][j-1:j+2] + b[i+1][j-1:j+2])
                count = m.count("*")
                if count:
                     b[i][j] = str(count)
    return list(map("".join, b))


def is_valid_board(b):
    width = "{" + str(len(b[0]) - 2) + "}"
    height = "{" + str(len(b) - 2) + "}"
    r = re.compile("^(\+-{w}\+)(\|[ *]{w}\|){h}(\+-{w}\+)$".format(w=width,
                                                                   h=height))
    return bool(r.match("".join(b)))
