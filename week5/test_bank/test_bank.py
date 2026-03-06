from bank import value


def test_hello_returns_zero():
    assert value("Hello, how are you?") == 0
    assert value("Hello!") == 0
    assert value("hello") == 0


def test_h_not_hello_returns_twenty():
    assert value("How are you?") == 20
    assert value("Howdy") == 20
    assert value("Hi there") == 20


def test_other_returns_hundred():
    assert value("What's up?") == 100
    assert value("Sup") == 100
    assert value("Good morning") == 100


def test_case_insensitive():
    assert value("HELLO") == 0
    assert value("HOWDY") == 20
    assert value("WHAT'S UP") == 100
