import pytest
from working import convert


def test_basic_conversion():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"


def test_with_minutes():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("10:15 AM to 4:45 PM") == "10:15 to 16:45"


def test_midnight_and_noon():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("9 am to 5 pm")
    with pytest.raises(ValueError):
        convert("09:60 AM to 05:00 PM")
    with pytest.raises(ValueError):
        convert("hello")
