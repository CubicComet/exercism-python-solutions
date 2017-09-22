BRACKETS = ["()", "[]", "{}"]


def check_brackets(s):
    brackets = "".join(filter(is_bracket, s))
    length = len(brackets)+1
    while 0 < len(brackets) < length:
        length = len(brackets)
        for pair in BRACKETS:
            brackets = brackets.replace(pair, "")
    return len(brackets) == 0


def is_bracket(ch):
    return ch in {"{", "}", "[", "]", "(", ")"}
