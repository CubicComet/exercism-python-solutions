def flatten(lst):
    """Completely flatten an arbitrarily-deep list"""
    return [*_flatten(lst)]


def _flatten(lst):
    """Generator for flattening arbitrarily-deep lists"""
    if isinstance(lst, (list, tuple)):
        for item in lst:
            if item is None:
                continue
            else:
                yield from _flatten(item)
    else:
        yield lst
