# -*- coding: utf-8 -*-

from __future__ import print_function
import re
import sys

palette = {'red': '\033[91m',
           'green': '\033[92m',
           'yellow': '\033[93m',
           'blue': '\033[94m',
           'pink': '\033[95m',
           'gray': '\033[37m',
           'white': '\033[97m',
           'black': '\033[30m',
           'default': '\033[0m',
           'bold': '\033[1m',
           'underline': '\033[4m',
          }

highlighter = {'red': '\033[101m',
                'green': '\033[102m',
                'yellow': '\033[103m',
                'blue': '\033[104m',
                'pink': '\033[105m',
                'gray': '\033[47m',
                'black': '\033[40m',
                'white': '\033[107m',
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


def color_print(s, color='default', highlight=None, bold=False, underline=False,
                end='\n', file=sys.stdout):
    """
    From http://stackoverflow.com/a/287944/610569
    """
    s = palette[color] + s
    if bold:
        s = palette['bold'] + s
    if underline:
        s = palette['underline'] + s
    if highlight and highlight in highlighter:
        s = higlighter[highlight] + s
    print(s + palette['default'], end=end, file=file)


def color_str(s, color='default', highlight=None, bold=False, underline=False):
    s = palette[color] + s
    if bold:
        s = palette['bold'] + s
    if underline:
        s = palette['underline'] + s
    if highlight and highlight in highlighter:
        s = higlighter[highlight] + s
    return s + palette['default']
