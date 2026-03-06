def main():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(text):
    vowels = "aeiouAEIOU"  # String is a list of characters
    result = ""
    for c in text:
        if c not in vowels:  # If the character is not in the list of vowels, add it to the result
            result += c
    return result


if __name__ == "__main__":
    main()
