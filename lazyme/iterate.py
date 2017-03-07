# -*- coding: utf-8 -*-

from itertools import groupby, islice

try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

def per_section(it, is_delimiter=lambda x: x.isspace()):
    """
    From http://stackoverflow.com/a/25226944/610569
    """
    ret = []
    for line in it:
        if is_delimiter(line):
            if ret:
                yield ret  # OR  ''.join(ret)
                ret = []
        else:
            ret.append(line.rstrip())  # OR  ret.append(line)
    if ret:
        yield ret

def per_chunk(iterable, n=1, fillvalue=None):
    """
    From http://stackoverflow.com/a/8991553/610569

        >>> list(per_chunk('abcdefghi', n=2))
        [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h'), ('i', None)]
        >>> list(per_chunk('abcdefghi', n=3))
        [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i')]
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def per_window(sequence, n=1):
    """
    From http://stackoverflow.com/q/42220614/610569

        >>> list(per_window([1,2,3,4], n=2))
        [(1, 2), (2, 3), (3, 4)]
        >>> list(per_window([1,2,3,4], n=3))
        [(1, 2, 3), (2, 3, 4)]
    """
    start, stop = 0, n
    seq = list(sequence)
    while stop <= len(seq):
        yield tuple(seq[start:stop])
        start += 1
        stop += 1

def zigzag(sequence):
    """
    http://stackoverflow.com/a/1442794/610569

        >>> zigzag(list(range(10)))
        ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])
    """
    return sequence[::2], sequence[1::2] # Returns (evens, odds)
