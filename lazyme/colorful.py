

def rgb_to_hex(rgb):
    """
    >>> rgb_to_hex((255, 255, 195))
    'ffffc3'
    """
    return '{:02x}{:02x}{:02x}'.format(*rgb)

def hex_to_rgb(hexa):
    """
    >>> hex_to_rgb('ffffc3')
    (255, 255, 195)
    """
    return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))
