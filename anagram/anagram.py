def detect_anagrams(s, array):
    return [cand for cand in array if is_anagram(cand, s)]

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return s1 != s2 and sorted(s1) == sorted(s2)
