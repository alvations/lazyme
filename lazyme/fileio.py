import fnmatch
import glob
import gzip
import hashlib
import os
import sys


def get_file_hash(filename, chunksize=8192):
    """
    [in]: xyz.zip
    [out]: de6f177970ae09dc3fb66228d51c1e3b
    """
    with open(filename, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(chunksize):
            file_hash.update(chunk)
        return file_hash.hexdigest()


def find_files(dir_path, extension="*"):
    """
    From https://stackoverflow.com/a/2186565/610569
    """
    if sys.version_info.major == 3 and sys.version_info.minor >= 5:
        pattern = "/".join([dir_path, "**", extension])
        for filename in glob.iglob(pattern, recursive=True):
            yield filename
    else:
        for root, dirnames, filenames in os.walk(dir_path):
            for filename in fnmatch.filter(filenames, extension):
                yield os.path.join(root, filename)


def open_two(filename1, filename2, strip=True):
    with open(filename1) as fin1, open(filename2) as fin2:
        for line1, line2 in zip(fin1, fin2):
            if strip:
                yield line1.strip(), line2.strip()
            else:
                yield line1, line2


def open_apply(filename, func):
    with open(filename) as fin:
        for line in fin:
            yield func(line)


def open_singlefile_xz(filename, mode="rt", encoding="utf8"):
    import lzma

    with lzma.open(filename, mode, encoding=encoding) as fin:
        yield from fin


def open_singlefile_gz(filename, mode="rt"):
    with gzip.open(filename, mode) as fin:
        yield from fin
