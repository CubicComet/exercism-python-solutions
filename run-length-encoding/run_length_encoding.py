import re


def decode(s):
    parts = re.findall(r'[0-9]*?[^0-9]', s)
    out_string = ""
    for part in parts:
        try:
            n = int(part[:-1])
        except ValueError:
            n = 1
        out_string += n * part[-1]
    return out_string


def encode(s):
    out_string = ""
    old_ch = char_or_blank(s, 0)
    start = 0

    for i in range(len(s)+1):
        ch = char_or_blank(s, i)
        if ch != old_ch:
            count = s[start:i].count(old_ch)
            if count is 1:
                out_string += old_ch
            else:
                out_string += str(count) + old_ch
            start = i
        old_ch = ch

    return out_string


def char_or_blank(s, i):
    try:
        ch = s[i]
    except IndexError:
        ch = ""
    return ch
