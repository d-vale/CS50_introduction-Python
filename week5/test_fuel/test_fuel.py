import pytest
from fuel import convert, gauge


# Tests pour convert

def test_convert_typical():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/3") == 33

def test_convert_full():
    assert convert("4/4") == 100
    assert convert("100/100") == 100

def test_convert_empty():
    assert convert("0/4") == 0
    assert convert("0/100") == 0

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("3/2")

def test_convert_negative_fraction():
    with pytest.raises(ValueError):
        convert("-3/2")

def test_convert_non_integer():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1/b")


# Tests pour gauge

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
