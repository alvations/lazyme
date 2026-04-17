from lazyme.iterate import (
    camel_shuffle,
    per_chunk,
    per_section,
    per_window,
    remove_none,
    skipping_window,
    zigzag,
)


def test_per_section_basic():
    lines = ["a\n", "b\n", "\n", "c\n", "d\n"]
    assert list(per_section(iter(lines))) == [["a", "b"], ["c", "d"]]


def test_per_section_trailing_no_delim():
    lines = ["a\n", "b\n"]
    assert list(per_section(iter(lines))) == [["a", "b"]]


def test_per_chunk_fill():
    assert list(per_chunk("abcdefghi", n=2)) == [
        ("a", "b"), ("c", "d"), ("e", "f"), ("g", "h"), ("i", None),
    ]


def test_per_chunk_exact():
    assert list(per_chunk("abcdefghi", n=3)) == [
        ("a", "b", "c"), ("d", "e", "f"), ("g", "h", "i"),
    ]


def test_per_window():
    assert list(per_window([1, 2, 3, 4], n=2)) == [(1, 2), (2, 3), (3, 4)]
    assert list(per_window([1, 2, 3, 4], n=3)) == [(1, 2, 3), (2, 3, 4)]


def test_zigzag():
    assert zigzag(list(range(10))) == ([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])


def test_skipping_window():
    assert list(skipping_window([1, 2, 3, 4, 5], 2, 3)) == [(1, 2, 3), (2, 3, 4)]


def test_camel_shuffle_shape():
    assert camel_shuffle(list(range(12))) == [0, 4, 8, 9, 5, 1, 2, 6, 10, 11, 7, 3]


def test_remove_none():
    assert list(remove_none([1, None, 2, None, 3])) == [1, 2, 3]
    assert list(remove_none([None, None])) == []
