def main():
    x, y = get_fraction()
    print(gauge(x, y))


def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x, y = int(x), int(y)

            # raise is needed here because Python only raises these errors automatically during arithmetic operations.
            # Since we're only validating the input (no division yet), we must raise them manually
            # to trigger the except block and prompt the user again.
            if y == 0:
                raise ZeroDivisionError  # if y is 0, it will raise ZeroDivisionError
            if x > y or x < 0:
                raise ValueError  # if x is greater than y or x is negative, it will raise ValueError
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return x, y


def gauge(x, y):
    percent = round(x / y * 100)
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"


main()
