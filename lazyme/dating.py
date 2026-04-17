from datetime import date, timedelta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def dates_in_quarter(year, quarter):
    assert 0 < quarter <= 4  # Allow only Q1 to Q4.
    quarter_to_months = {1: (1, 4), 2: (4, 7), 3: (7, 10), 4: (10, 1)}
    start_month, end_month = quarter_to_months[quarter]
    end_year = year + 1 if quarter == 4 else year
    start_date = date(year, start_month, 1)
    end_date = date(end_year, end_month, 1)
    return daterange(start_date, end_date)
