import hashlib

import pytest

from lazyme.hashing import md5


def test_md5_hex():
    assert md5("hello", digest="hex") == hashlib.md5(b"hello").hexdigest()


def test_md5_int():
    expected = int(hashlib.md5(b"hello").hexdigest(), 16)
    assert md5("hello", digest="int") == expected


def test_md5_binary_is_str():
    out = md5("hello", digest="binary")
    assert isinstance(out, str)
    assert set(out) <= {"0", "1"}


xxhash = pytest.importorskip("xxhash")


def test_xxh64_int():
    from lazyme.hashing import xxh64

    assert isinstance(xxh64("hello"), int)


def test_xxh64_hex():
    from lazyme.hashing import xxh64

    out = xxh64("hello", digest="hex")
    assert isinstance(out, str)
    assert len(out) == 16
