
def ints(_s, _separator=' '):
    """Returns all the integer in a string ignoring non integer tokens"""
    _l = map(str_to_i, _s) if _separator == '' else map(str_to_i, tokens(_s, _separator))
    return list(filter(lambda _x: _x is not None, _l))


def str_to_i(_s):
    """Converts a string to an integer, returns None if not an integer"""
    try:
        return int(_s.strip())
    except ValueError:
        return None


def print_tuple(*_args, _separator=' '):
    """Prints all the elements in a tuple separated by a given separator, default ' '"""
    return _separator.join(map(lambda _x: str(_x), _args))


def tokens(_s, _separator=' '):
    """Returns all the tokens from a string, separated by a given separator, default ' '"""
    return _s.strip().split(_separator)


def combinations(_elements, _n=None, _repetition=False):
    """Returns all the possible combinations of length n from the given elements, with or without repetition"""
    if _n is not None and _n > len(_elements) and not _repetition:
        raise Exception(f'n ({_n}) cannot be greater than the number of elements ({len(_elements)}) '
                        f'if repetition is not allowed')
    yield from _combinations(_elements, len(_elements) if _n is None else _n, 0 if _repetition else 1, [])


def _combinations(_elements, _n, _offset, _prefix):
    if len(_prefix) == _n:
        yield _prefix
    else:
        for _i in range(0, len(_elements)):
            yield from _combinations(_elements[_i+_offset:], _n, _offset, _prefix + [_elements[_i]])


def permutations(_elements, _n=None, _repetition=False):
    """Returns all the possible permutations of length n from the given elements, with or without repetition"""
    if _n is not None and _n > len(_elements) and not _repetition:
        raise Exception(f'n ({_n}) cannot be greater than the number of elements ({len(_elements)}) '
                        f'if repetition is not allowed')

    if _repetition:
        yield from _permutations_with_rep(_elements, len(_elements) if _n is None else _n, [])
    else:
        yield from _permutations(_elements, _n, [])


def _permutations(_elements, _n, _prefix):
    if len(_prefix) == _n or len(_elements) == 0:
        yield _prefix
    else:
        for _i in range(0, len(_elements)):
            yield from _permutations(_elements[:_i] + _elements[_i+1:], _n, _prefix + [_elements[_i]])


def _permutations_with_rep(_elements, _n, _prefix):
    if len(_prefix) == _n:
        yield _prefix
    else:
        for _e in _elements:
            yield from _permutations_with_rep(_elements, _n, _prefix + [_e])
