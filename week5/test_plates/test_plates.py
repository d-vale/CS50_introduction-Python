from plates import is_valid


# Plaques valides
def test_valid_letters_only():
    assert is_valid("CS50") == True

def test_valid_two_letters():
    assert is_valid("AB") == True

def test_valid_six_chars():
    assert is_valid("AAA222") == True

def test_valid_letters_and_numbers():
    assert is_valid("AA123") == True


# Longueur invalide
def test_too_short():
    assert is_valid("A") == False

def test_too_long():
    assert is_valid("AAAAAAA") == False


# Ne commence pas par deux lettres
def test_starts_with_number():
    assert is_valid("1AA") == False

def test_only_one_starting_letter():
    assert is_valid("A1") == False


# Zéro comme premier chiffre
def test_first_digit_zero():
    assert is_valid("CS05") == False

def test_first_digit_zero_at_end():
    assert is_valid("AA05") == False


# Lettre après un chiffre
def test_letter_after_digit():
    assert is_valid("AAA22A") == False

def test_digit_then_letter():
    assert is_valid("CS5P") == False


# Caractères non alphanumériques
def test_punctuation():
    assert is_valid("CS.50") == False

def test_space():
    assert is_valid("CS 50") == False

def test_exclamation():
    assert is_valid("CS50!") == False

