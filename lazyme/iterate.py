# -*- coding: utf-8 -*-

from itertools import groupby

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
