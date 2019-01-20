# -*- coding: utf-8 -*-

import os

try: # Try importing Python3 urllib
    import urllib.request
except ImportError: # Now importing Python2 urllib
    import urllib

def get_content(url):
    try: # Using Python3 urllib.
        with urllib.request.urlopen(url) as response:
            return response.read() # Returns http.client.HTTPResponse.
    except AttributeError: # Using Python3 urllib.
        return urllib.urlopen(url).read() # Returns an instance.

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
