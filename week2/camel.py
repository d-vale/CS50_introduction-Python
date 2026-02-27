def main():
    camelcase_string = input("camelCase: ")
    print("snake_case:", camelcase_to_snakecase(camelcase_string))


def camelcase_to_snakecase(s):
    # List to store de final result
    result = []
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Check if the result list is not empty we need to add an underscore before the lowercase character
            if result:
                result.append('_')
            result.append(char.lower())  # Finaly add de lowercase character to the result list
        else:  # If the character is not uppercase we just add it to the result list
            result.append(char)

    # Join the list into a string and return it
    return ''.join(result)


main()
