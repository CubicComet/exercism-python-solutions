PHRASES = ("house that Jack built.",
           "lay in",
           "malt",
           "ate",
           "rat",
           "killed",
           "cat",
           "worried",
           "dog",
           "tossed",
           "cow with the crumpled horn",
           "milked",
           "maiden all forlorn",
           "kissed",
           "man all tattered and torn",
           "married",
           "priest all shaven and shorn",
           "woke",
           "rooster that crowed in the morn",
           "kept",
           "farmer sowing his corn",
           "belonged to",
           "horse and the hound and the horn")


def verse(n):
    return construct_verse(n).format(*PHRASES)


def construct_verse(n):
    v = ["This is the {{{0}}}".format(2*n)]
    v += ["that {{{0}}} the {{{1}}}".format(2*(n-i)+1, 2*(n-i))
          for i in range(1, n+1)]
    return "\n".join(v)


def rhyme():
    return "\n\n".join(verse(i) for i in range(12))
