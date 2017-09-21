CODE = {"wink": 1, "double blink": 2, "close your eyes": 4, "jump": 8}


def handshake(n):
    try:
        n = int(n, 2)
    except (ValueError, TypeError):
        n = int(n)
    if not 0 < n < 32:
        return []
    lst = [action for action, val in CODE.items() if n & val]
    return lst if not n & 16 else list(reversed(lst))


def code(lst):
    try:
        actions = [CODE[item] for item in lst]
    except KeyError:
        actions = []

    if len(actions) > 1 and actions == sorted(actions, reverse=True):
        actions.append(16)
    elif actions != sorted(actions): # Catch out-of-order actions
        actions = []

    return "{:b}".format(sum(actions))
