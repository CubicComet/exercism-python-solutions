from datetime import date


class MeetupDayException(Exception):
    pass


WEEKDAYS = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
            "Friday": 4, "Saturday": 5, "Sunday": 6}

TEENTH = {1:15, 2:16, 3:17, 4:18, 5:19, 6:13, 7:14}

ORDINAL = {"1st": 0, "2nd": 7, "3rd": 14, "4th": 21, "5th": 28}


def meetup_day(y, m, dow, dom):
    start = date(y, m, 1)
    first_dow = (WEEKDAYS[dow] - start.weekday()) % 7 + 1
    
    if dom == "teenth":
        d = date(y, m, TEENTH[first_dow])
    elif dom == "last":
        try:
            d = date(y, m, first_dow + 28)
        except ValueError:
            d = date(y, m, first_dow + 21)
    else:
        try:
            d = date(y, m, first_dow + ORDINAL[dom])
        except ValueError:
            raise MeetupDayException("Out of range")
        except KeyError:
            raise MeetupDayException("Invalid input")
    
    return d
