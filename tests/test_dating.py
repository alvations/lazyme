from datetime import date

import pytest

from lazyme.dating import daterange, dates_in_quarter


def test_daterange_basic():
    out = list(daterange(date(2024, 1, 1), date(2024, 1, 4)))
    assert out == [date(2024, 1, 1), date(2024, 1, 2), date(2024, 1, 3)]


def test_dates_in_quarter_lengths():
    # 2024 is a leap year.
    assert len(list(dates_in_quarter(2024, 1))) == 31 + 29 + 31
    assert len(list(dates_in_quarter(2024, 2))) == 30 + 31 + 30
    assert len(list(dates_in_quarter(2024, 3))) == 31 + 31 + 30
    assert len(list(dates_in_quarter(2024, 4))) == 31 + 30 + 31


def test_dates_in_quarter_q4_spans_year():
    dates = list(dates_in_quarter(2023, 4))
    assert dates[0] == date(2023, 10, 1)
    assert dates[-1] == date(2023, 12, 31)


@pytest.mark.parametrize("bad", [0, 5, -1])
def test_dates_in_quarter_rejects_invalid(bad):
    with pytest.raises(AssertionError):
        list(dates_in_quarter(2024, bad))
