def test_package_imports():
    import lazyme
    assert lazyme.__version__


def test_all_modules_importable():
    # Each must import cleanly on its own.
    import lazyme.colorful  # noqa: F401
    import lazyme.data  # noqa: F401
    import lazyme.dating  # noqa: F401
    import lazyme.fileio  # noqa: F401
    import lazyme.hashing  # noqa: F401
    import lazyme.iterate  # noqa: F401
    import lazyme.pythonic  # noqa: F401
    import lazyme.string  # noqa: F401
    import lazyme.timing  # noqa: F401
    import lazyme.wikipedia  # noqa: F401
