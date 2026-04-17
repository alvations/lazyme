import os
import shutil
import site
import sys


def which_python():
    return sys.executable

def which_pip():
    return shutil.which("pip")

def wheres_packages():
    return site.getsitepackages()[0]

def wheres_this_file():
    return os.path.dirname(os.path.realpath(__file__))
