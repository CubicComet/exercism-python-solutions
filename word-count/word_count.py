def word_count(s):
    words = strip_punc(s.lower()).split()
    return {word: words.count(word) for word in set(words)}



def strip_punc(s):
    return "".join(ch if ch.isalnum() else " " for ch in s)
