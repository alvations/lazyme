from lazyme.colorful import hex_to_rgb, rgb_to_hex


def test_rgb_to_hex():
    assert rgb_to_hex((255, 255, 195)) == "ffffc3"
    assert rgb_to_hex((0, 0, 0)) == "000000"


def test_hex_to_rgb():
    assert hex_to_rgb("ffffc3") == (255, 255, 195)
    assert hex_to_rgb("000000") == (0, 0, 0)


def test_roundtrip():
    for rgb in [(12, 34, 56), (200, 100, 50), (255, 0, 128)]:
        assert hex_to_rgb(rgb_to_hex(rgb)) == rgb
