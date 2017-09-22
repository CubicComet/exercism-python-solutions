BRACKETS = ["()", "[]", "{}"]


def check_brackets(s):
    brackets = "".join(filter(is_bracket, s))
    length = 0
    while brackets and length != len(brackets):
        length = len(brackets)
        for pair in BRACKETS:
            brackets = brackets.replace(pair, "")
    return len(brackets) == 0


def is_bracket(ch):
    return ch in {"{", "}", "[", "]", "(", ")"}
