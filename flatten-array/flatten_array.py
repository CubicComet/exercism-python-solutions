def flatten(lst):
    """Completely flatten an arbitrarily-deep list"""
    return [*_flatten(lst)]


def _flatten(lst):
    """Generator for flattening arbitrarily-deep lists"""
    for item in lst:
        if isinstance(item, (list, tuple)):
            yield from _flatten(item)
        elif item is not None:
            yield item
