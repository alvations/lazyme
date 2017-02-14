# -*- coding: utf-8 -*-

from itertools import groupby, islice

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

def per_chunk(iterable, n=1):
    """
    From http://stackoverflow.com/a/8991553/610569

        >>> list(iter_by_n('abcdefghi', n=2))
        [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h'), ('i',)]
        >>> list(iter_by_n('abcdefghi', n=3))
        [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i')]
    """
    it = iter(iterable)
    while True:
       chunk = tuple(islice(it, n))
       if not chunk:
           return
       yield chunk

def per_window(iterable, n=1):
    """
    From http://stackoverflow.com/q/42220614/610569

        >>> list(per_window([1,2,3,4], n=2))
        [[1, 2], [2, 3], [3, 4]]
        >>> list(per_window([1,2,3,4], n=3))
        [[1, 2, 3], [2, 3, 4]]
    """
    start, stop = 0, n
    while stop <= len(iterable):
        yield iterable[start:stop]
        start += 1
        stop += 1
