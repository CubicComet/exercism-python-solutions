def board(white, black):
    if white == black:
        raise ValueError("Pieces cannot share a position")
    _board = [['_']*8 for _ in range(8)]
    wx, wy = white
    bx, by = black
    try:
        _board[wx][wy] = "W"
        _board[bx][by] = "B"
    except IndexError:
        raise ValueError("Piece coordinates out of range")
    return list(map("".join, _board))


def can_attack(white, black):
    if white == black or max(white + black) > 7:
        raise ValueError("Invalid piece positions")
    wx, wy = white
    bx, by = black
    return wx == bx or wy == by or abs(wx - bx) == abs(wy - by)
