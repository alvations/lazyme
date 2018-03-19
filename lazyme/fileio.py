# -*- coding: utf-8 -*-

import fnmatch
import glob
import os
import sys


def find_files(dir_path, extension="*"):
    """
    From https://stackoverflow.com/a/2186565/610569
    """
    if sys.version_info.major == 3 and sys.version_info.minor >= 5:
        pattern = '/'.join([dir_path, '**', extension])
        for filename in glob.iglob(pattern, recursive=True):
            yield filename
    else:
        for root, dirnames, filenames in os.walk(dir_path):
            for filename in fnmatch.filter(filenames, extension):
                yield os.path.join(root, filename)
