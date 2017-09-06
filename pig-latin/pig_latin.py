import re


_REGEX = (r'^(?P<c>([^aeiou]?qu)|([^aeiouxy]+?)|([xy](?=[aeiou]))|())'
          + r'(?P<v>(([xy][^aeiou]+)|([aeiou])).*)$')
REGEX = re.compile(_REGEX)


def translate(phrase):
    return " ".join(map(_translate, phrase.split()))


def _translate(word):
    matches = REGEX.match(word)
    return matches["v"] + matches["c"] + "ay"
