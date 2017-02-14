# -*- coding: utf-8 -*-

def deduplicate(s, ch):
    """
    From http://stackoverflow.com/q/42216559/610569

        >>> s = 'this is   an   irritating string with  random spacing  .'
        >>> deduplicate(s)
        'this is an irritating string with random spacing .'
    """
    return ch.join([substring for substring in s.strip().split(ch) if substring])
