
import os
import pip
import sys
import site


def which_python():
    return sys.executable

def which_pip():
    return pip.__path__[0]

def wheres_packages():
    return site.getsitepackages()[0]

def wheres_this_file():
    return os.path.dirname(os.path.realpath(__file__))
