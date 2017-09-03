import re


def abbreviate(s):
    return "".join(re.findall(r'^[A-Z]|(?<=[ -])[A-Za-z](?![A-Z])', s)).upper()
