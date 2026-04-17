import os
import sys

from lazyme.pythonic import (
    wheres_packages,
    wheres_this_file,
    which_pip,
    which_python,
)


def test_which_python():
    assert which_python() == sys.executable


def test_which_pip_returns_str_or_none():
    out = which_pip()
    assert out is None or isinstance(out, str)


def test_wheres_packages():
    out = wheres_packages()
    assert isinstance(out, str) and os.path.isdir(out)


def test_wheres_this_file():
    out = wheres_this_file()
    assert out.endswith("lazyme")
