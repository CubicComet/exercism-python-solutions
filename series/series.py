def slices(s, n):
    m = len(s)
    if n > m:
        raise ValueError("Slice cannot be larger than the string")
    if n < 1:
        raise ValueError("Slices must have a positive non-zero length")
        
    return [list(map(int, s[i:i+n])) for i in range(m-n+1)]
