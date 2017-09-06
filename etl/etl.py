def transform(scrabble):
    return {ch.lower(): v for (v, chs) in scrabble.items() for ch in chs}
