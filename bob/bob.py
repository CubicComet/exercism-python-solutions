def hey(s):
    s = s.strip()
    if s.isupper():
        return "Whoa, chill out!"
    elif s == "":
        return "Fine. Be that way!"
    elif s.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
