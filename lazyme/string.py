# -*- coding: utf-8 -*-

import re

def deduplicate(s, ch):
    """
    From http://stackoverflow.com/q/42216559/610569

        s = 'this is   an   irritating string with  random spacing  .'
        deduplicate(s)
        'this is an irritating string with random spacing .'
    """
    return ch.join([substring for substring in s.strip().split(ch) if substring])


def remove_html_tags(s):
    """
    From http://stackoverflow.com/a/12982689/610569
    """
    return re.sub('<.*?>', '', s)


def rstrip_digit(s):
    """
    From http://stackoverflow.com/a/40691501/610569
    """
    return re.sub(r'\d+$', '', s)


def remove_text_inside_brackets(s, brackets="()[]"):
    """
    From http://stackoverflow.com/a/14603508/610569
    """
    count = [0] * (len(brackets) // 2) # count open/close brackets
    saved_chars = []
    for character in s:
        for i, b in enumerate(brackets):
            if character == b: # found bracket
                kind, is_close = divmod(i, 2)
                count[kind] += (-1)**is_close # `+1`: open, `-1`: close
                if count[kind] < 0: # unbalanced bracket
                    count[kind] = 0
                break
        else: # character is not a bracket
            if not any(count): # outside brackets
                saved_chars.append(character)
    return ''.join(saved_chars)