from twttr import shorten

def test_twttr_default():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("Python Programming") == "Pythn Prgrmmng"

def test_twttr_all_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_twttr_empty():
    assert shorten("") == ""

def test_twttr_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("h3ll0 w0rld") == "h3ll0 w0rld"

def test_twttr_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO WORLD") == "HLL WRLD"

