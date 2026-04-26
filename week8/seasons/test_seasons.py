from datetime import date
from seasons import calculate_minutes


def test_one_year():
    # 2023 is not a leap year: 365 days = 525600 minutes
    assert calculate_minutes(date(2023, 1, 1), date(2024, 1, 1)) == 525600


def test_two_years():
    # 2022 and 2023 are not leap years: 730 days = 1051200 minutes
    assert calculate_minutes(date(2022, 1, 1), date(2024, 1, 1)) == 1051200


def test_leap_year():
    # 2024 is a leap year: 366 days = 527040 minutes
    assert calculate_minutes(date(2024, 1, 1), date(2025, 1, 1)) == 527040


def test_same_day():
    assert calculate_minutes(date(2024, 6, 15), date(2024, 6, 15)) == 0
