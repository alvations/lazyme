
import os
import sys
import urllib.request
from collections import deque
from collections.abc import Mapping, Set
from numbers import Number


def get_content(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

def norvig_bigtxt():
    url = "https://norvig.com/big.txt"
    # Check if the Norvig's big.txt file exists.
    if os.path.isfile('big.txt'):
        with open('big.txt') as fin:
            return fin.read()
    else: # Otherwise, download the big.txt.
        big_txt = get_content(url).decode('utf8')
        with open('big.txt', 'w') as fout:
            fout.write(big_txt)
        return big_txt


def getsize(obj_0):
    """
    Recursively iterate to sum size of object & members.
    From https://stackoverflow.com/a/30316760/610569
    """
    _seen_ids = set()
    def inner(obj):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size = sys.getsizeof(obj)
        if isinstance(obj, (str, bytes, Number, range, bytearray)):
            pass # bypass remaining control flow and return
        elif isinstance(obj, (tuple, list, Set, deque)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, Mapping) or hasattr(obj, 'items'):
            size += sum(inner(k) + inner(v) for k, v in getattr(obj, 'items')())
        # Check for custom object instances - may subclass above too
        if hasattr(obj, '__dict__'):
            size += inner(vars(obj))
        if hasattr(obj, '__slots__'): # can have __slots__ with __dict__
            size += sum(inner(getattr(obj, s)) for s in obj.__slots__ if hasattr(obj, s))
        return size
    return inner(obj_0)
