import re
import operator


OPS = {"multiplied by": operator.mul,
       "divided by": operator.floordiv,
       "plus": operator.add,
       "minus": operator.sub}


def calculate(s):
    if not re.match("^What is ((-?[0-9]+) ([a-z ]+))+ (-?[0-9]+)\?", s):
        raise ValueError("Input not understood")
    values = re.findall("-?[0-9]+", s)
    ops = re.findall("(?<=[0-9] )[a-z ]+(?= -?[0-9]+)", s)
    value = int(values[0])
    try:
        for val, op in zip(values[1:], ops):
            value = OPS[op](value, int(val))
    except KeyError:
        raise ValueError("Invalid operator")
    return value
