import gzip

import pytest

from lazyme.fileio import (
    find_files,
    get_file_hash,
    open_apply,
    open_singlefile_gz,
    open_two,
)


def test_get_file_hash(tmp_path):
    f = tmp_path / "x.txt"
    f.write_bytes(b"hello")
    import hashlib

    assert get_file_hash(str(f)) == hashlib.md5(b"hello").hexdigest()


def test_find_files(tmp_path):
    (tmp_path / "a.txt").write_text("a")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "b.txt").write_text("b")
    found = sorted(find_files(str(tmp_path), "*.txt"))
    assert len(found) == 2
    assert all(p.endswith(".txt") for p in found)


def test_open_two_strip(tmp_path):
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"
    f1.write_text("one\ntwo\n")
    f2.write_text("1\n2\n")
    assert list(open_two(str(f1), str(f2))) == [("one", "1"), ("two", "2")]


def test_open_two_no_strip(tmp_path):
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"
    f1.write_text("one\n")
    f2.write_text("1\n")
    assert list(open_two(str(f1), str(f2), strip=False)) == [("one\n", "1\n")]


def test_open_apply(tmp_path):
    f = tmp_path / "x.txt"
    f.write_text("a\nb\nc\n")
    assert list(open_apply(str(f), str.strip)) == ["a", "b", "c"]


def test_open_singlefile_gz(tmp_path):
    f = tmp_path / "x.txt.gz"
    with gzip.open(f, "wt") as fout:
        fout.write("one\ntwo\n")
    assert list(open_singlefile_gz(str(f))) == ["one\n", "two\n"]
