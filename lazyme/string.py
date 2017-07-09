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
           'black': '\033[30m',
           'white': '\033[97m',
           'back_red': '\033[101m',
           'back_green': '\033[102m',
           'back_yellow': '\033[103m',
           'back_blue': '\033[104m',
           'back_pink': '\033[105m',
           'back_gray':, '\033[47m',
           'back_black':, '\033[40m',
           'back_white':, '\033[107m',
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


def color_print(s, color='default', bold=False, background='', underline=False,
                end='\n', file=sys.stdout):
    """
    From http://stackoverflow.com/a/287944/610569
    """
    s = palette[color] + s
    if bold:
        s = palette['bold'] + s
    if underline:
        s = palette['underline'] + s
    if background != '':
        s = palette['back_' + background] + s
    print(s + palette['default'], end=end, file=file)


def color_str(s, color='default', bold=False, background='', underline=False):
    s = palette[color] + s
    if bold:
        s = palette['bold'] + s
    if underline:
        s = palette['underline'] + s
    if background != '':
        s = palette['back_' + background] + s
    return s + palette['default']

