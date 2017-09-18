VERSE = "{0} bottles of beer on the wall, {0} bottles of beer.\n" \
      + "Take one down and pass it around, {1} bottles of beer on the wall.\n"

ONE = "1 bottle of beer on the wall, 1 bottle of beer.\n" \
    + "Take it down and pass it around, no more bottles of beer on the wall.\n"

NO_MORE = "No more bottles of beer on the wall, no more bottles of beer.\n" \
        + "Go to the store and buy some more, 99 bottles of beer on the wall.\n"


def verse(number):
    if number == 0:
        return NO_MORE
    elif number == 1:
        return ONE
    else:
        return VERSE.format(number, number-1).replace("1 bottles", "1 bottle")


def song(number1, number2=0):
    return "".join(verse(i)+"\n" for i in reversed(range(number2, number1+1)))
