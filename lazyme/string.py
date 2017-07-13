# -*- coding: utf-8 -*-

from __future__ import print_function
import re
import sys

palette = {
    'black': '\033[30m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'pink': '\033[95m', 'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'gray': '\033[37m',
    'default': '\033[0m',
}

highlighter = {
    'black': '\033[40m',
    'red': '\033[101m',
    'green': '\033[102m',
    'yellow': '\033[103m',
    'blue': '\033[104m',
    'pink': '\033[105m', 'magenta': '\033[105m',
    'cyan': '\033[106m',
    'white': '\033[107m',
    'gray': '\033[47m',
}

formatter = {
    'default': '\033[0m',
    'bold': '\033[1m',
    'faint': '\033[2m',
    'italic': '\033[3m',        # Doesn't work on Ubuntu/Mac terminal.
    'underline': '\033[4m',
    'blinking': '\033[5m',
    'fast_blinking': '\033[6m', # Doesn't work on Ubuntu/Mac terminal.
    'reverse': '\033[7m',       # Note: This reverses the back-/foreground color.
    'hide': '\033[8m',
    'strikethrough': '\033[9m', # Doesn't work on Ubuntu/Mac terminal.
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


def color_print(s, color=None, highlight=None, end='\n', file=sys.stdout,
                **kwargs):
    """
    From http://stackoverflow.com/a/287944/610569
    See also https://gist.github.com/Sheljohn/68ca3be74139f66dbc6127784f638920
    """
    if color in palette and color != 'default':
        s = palette[color] + s
    # Highlight / Background color.
    if highlight and highlight in highlighter:
        s = highlighter[highlight] + s
    # Custom string format.
    for name, value in kwargs.items():
        if name in formatter and value == True:
            s = formatter[name] + s
    print(s + palette['default'], end=end, file=file)


def color_str(s, color=None, highlight=None, **kwargs):
    if color in palette and color != 'default':
        s = palette[color] + s
    # Highlight / Background color.
    if highlight and highlight in highlighter:
        s = highlighter[highlight] + s
    # Custom string format.
    for name, value in kwargs.items():
        if name in formatter and value == True:
            s = formatter[name] + s
    return s + palette['default']
