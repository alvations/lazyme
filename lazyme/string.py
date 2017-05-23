# -*- coding: utf-8 -*-

from __future__ import print_function
import re
import sys

palette = {'red': '\033[91m',
           'green': '\033[92m',
           'yellow': '\033[93m',
           'blue': '\033[94m',
           'pink': '\033[95m',
           'default': '\033[0m',
           'bold': '\033[1m',
           'underline': '\033[4m',
          }

def deduplicate(s, ch):
    """
    From http://stackoverflow.com/q/42216559/610569

        s = 'this is   an   irritating string with  random spacing  .'
        deduplicate(s)
        'this is an irritating string with random spacing .'
    """
    return ch.join([substring for substring in s.strip().split(ch) if substring])


def remove_html_tags(s, pad=' '):
    """
    From http://stackoverflow.com/a/12982689/610569
    """
    return re.sub('<.*?>', pad, s)


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


def color_print(s, color='default', bold=False, underline=False,
                end='\n', file=sys.stdout):
    """
    From http://stackoverflow.com/a/287944/610569
    """
    s = palette[color] + s
    if bold:
        s = palette['bold'] + s
    if underline:
        s = palette['underline'] + s
    print(s + palette['default'], end=end, file=file)


def color_str(s, color='default', bold=False, underline=False):
    s = palette[color] + s
    if bold:
        s = palette['bold'] + s
    if underline:
        s = palette['underline'] + s
    return s + palette['default']























##
