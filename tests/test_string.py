from lazyme.string import (
    color_str,
    deduplicate,
    remove_html_tags,
    remove_text_inside_brackets,
    rstrip_digit,
)


def test_deduplicate_spaces():
    s = "this is   an   irritating string with  random spacing  ."
    assert deduplicate(s, " ") == "this is an irritating string with random spacing ."


def test_remove_html_tags():
    assert remove_html_tags("<b>hi</b>", pad="") == "hi"
    assert remove_html_tags("<p>a</p><p>b</p>", pad="|") == "|a||b|"


def test_rstrip_digit():
    assert rstrip_digit("foo123") == "foo"
    assert rstrip_digit("bar") == "bar"


def test_remove_text_inside_brackets():
    assert remove_text_inside_brackets("hello (world) !") == "hello  !"
    assert remove_text_inside_brackets("a [b] c") == "a  c"


def test_color_str_wraps_reset():
    out = color_str("x", color="red")
    assert out.startswith("\033[91m")
    assert out.endswith("\033[0m")
    assert "x" in out


def test_color_str_no_color():
    # Unknown color is a no-op style-wise but still appends reset.
    out = color_str("x")
    assert out == "x\033[0m"
