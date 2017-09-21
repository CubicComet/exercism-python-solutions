GIFT = {1: "a Partridge in a Pear Tree",
        2: "two Turtle Doves",
        3: "three French Hens",
        4: "four Calling Birds",
        5: "five Gold Rings",
        6: "six Geese-a-Laying",
        7: "seven Swans-a-Swimming",
        8: "eight Maids-a-Milking",
        9: "nine Ladies Dancing",
        10: "ten Lords-a-Leaping",
        11: "eleven Pipers Piping",
        12: "twelve Drummers Drumming"}

ORD = {1: "first", 2: "second", 3: "third", 4: "fourth",
       5: "fifth", 6: "sixth", 7: "seventh", 8: "eighth",
       9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth"}


BASE = "On the {:s} day of Christmas my true love gave to me, {:s}.\n"


def verse(n):
    return BASE.format(ORD[n], ", ".join(_gifts(n)))


def verses(a, b):
    return "\n".join(verse(i) for i in range(a, b+1)) + "\n"


def sing():
    return verses(1, 12)


def _gifts(n):
    if n == 1:
        yield GIFT[1]
    else:
        for i in reversed(range(2, n+1)):
            yield GIFT[i]
        yield "and " + GIFT[1]
