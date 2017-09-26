SEG = {'0': (' _ ', '| |', '|_|', '   '),
       '1': ('   ', '  |', '  |', '   '),
       '2': (' _ ', ' _|', '|_ ', '   '),
       '3': (' _ ', ' _|', ' _|', '   '),
       '4': ('   ', '|_|', '  |', '   '),
       '5': (' _ ', '|_ ', ' _|', '   '),
       '6': (' _ ', '|_ ', '|_|', '   '),
       '7': (' _ ', '  |', '  |', '   '),
       '8': (' _ ', '|_|', '|_|', '   '),
       '9': (' _ ', '|_|', ' _|', '   ')}

OCR = {v: k for k, v in SEG.items()}


def number(seg):
    rows = [[row[i:i+3] for i in range(0, len(row), 3)] for row in seg]
    try:
        return "".join(digit(d) for d in zip(*rows))
    except TypeError:
        print(rows)


def digit(d):
    try:
        return OCR[tuple(d)]
    except KeyError:
        if len(d) != 4 or not all(len(row) == 3 for row in d):
            raise ValueError("Improperly formatted input")
        else:
            return "?"


def grid(digits):
    try:
        segments = [SEG[n] for n in digits]
    except KeyError:
        raise ValueError("Unrecognised digit")
    return ["".join(row) for row in zip(*segments)]
