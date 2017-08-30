import datetime


def add_gigasecond(dt_obj):
    return dt_obj + datetime.timedelta(seconds=10**9)

