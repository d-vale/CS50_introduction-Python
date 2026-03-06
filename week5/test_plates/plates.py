def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Length must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Only letters and numbers allowed (no punctuation, spaces, etc.)
    if not s.isalnum():
        return False

    # Numbers must come at the end; no letter after a digit
    # The first number used cannot be a '0'
    found_digit = False
    for c in s:
        if c.isdigit():
            if not found_digit:
                # First digit encountered
                if c == '0':
                    return False
                found_digit = True
        else:
            # It's a letter
            if found_digit:
                # Letter after a digit → invalid
                return False

    return True


if __name__ == "__main__":
    main()
