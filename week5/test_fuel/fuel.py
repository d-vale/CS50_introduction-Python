def main():
    fraction = input("Fraction: ")
    while True:
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y or x < 0:
        raise ValueError
    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
