import math


def encode(s, n):
    _n = 2 * n - 2
    chunks = [s[i::_n] + " " for i in range(_n)]
    lines = []
    for i in range(n):
        if i == 0 or i == n-1:
            lines.append(chunks[i])
        else:
            lines.append("".join(x + y for x, y in zip(chunks[i], chunks[-i])))
    return "".join(map(str.strip, lines))


def decode(s, n):
    _n = 2 * n - 2
    diff = len(s) % _n
    if diff == 0:  diff = _n
    base_chunk_len = math.ceil(len(s) / _n)
    _chunk_lens = [base_chunk_len - 1 if i >= diff else base_chunk_len
                       for i in range(_n)]

    chunk_lens = [_chunk_lens[i] if i in {0, n-1}
                  else _chunk_lens[i] + _chunk_lens[-i] for i in range(n)]

    start = 0
    chunks = []
    for i in range(n):
        chunks.append(s[start:start+chunk_lens[i]])
        start += chunk_lens[i]

    _chunks = []
    for i in range(_n):
        if i == 0 or i == n-1:
            _chunks.append(chunks[i] + " ")
        elif i < n:
            _chunks.append(chunks[i][0::2] + " ")
        else:
            _chunks.append(chunks[_n - i][1::2] + " ")

    return "".join(map("".join, zip(*_chunks))).strip()
