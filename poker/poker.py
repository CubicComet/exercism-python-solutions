from statistics import mode, StatisticsError


VALUE = {k: v for k, v in zip("23456789TJQKA", range(13))}


def poker(hands):
    values = list(map(hand_value, hands))
    max_val = max(values)
    return [hand for hand, value in zip(hands, values) if value == max_val]


def hand_value(hand):
    values = [VALUE[card[0]] for card in hand]
    suits = [card[1] for card in hand]

    if is_flush(suits) and is_straight(values):
        type_score = 8
    elif is_fourkind(values):
        type_score = 7
    elif is_fullhouse(values):
        type_score = 6
    elif is_flush(suits):
        type_score = 5
    elif is_straight(values):
        type_score = 4
    elif is_threekind(values):
        type_score = 3
    elif is_twopair(values):
        type_score = 2
    elif is_onepair(values):
        type_score = 1
    else:
        type_score = 0

    print((hand, type_score, poker_sort(values)))

    return (13**5 * type_score
            + sum(13**i * val for i, val in enumerate(poker_sort(values))))


def is_flush(suits):
    return len(set(suits)) == 1

def is_straight(values):
    return len(set(values)) is 5 and (max(values) - min(values) == 4)

def is_fourkind(values):
    try:
        return len(set(values)) is 2 and values.count(mode(values)) is 4
    except StatisticsError:
        return False

def is_fullhouse(values):
    try:
        return len(set(values)) is 2 and values.count(mode(values)) is 3
    except StatisticsError:
        return False

def is_threekind(values):
    try:
        return len(set(values)) is 3 and values.count(mode(values)) is 3
    except StatisticsError:
        return False

def is_twopair(values):
    if len(set(values)) is 3:
        try:
            return values.count(mode(values)) is 2
        except StatisticsError:
            return True
    else:
        return False

def is_onepair(values):
    try:
        return len(set(values)) is 4 and values.count(mode(values)) is 2
    except StatisticsError:
        return False


def poker_sort(values):
    return sorted(values, key=lambda x: 13*values.count(x)+x)
