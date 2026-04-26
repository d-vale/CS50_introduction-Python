import sys
import inflect
from datetime import date


def main():
    bd_str = input("Date of Birth: ")
    try:
        bd = date.fromisoformat(bd_str)
    except ValueError:
        sys.exit("Invalid date")
    minutes = calculate_minutes(bd, date.today())
    p = inflect.engine()
    print(p.number_to_words(minutes, andword="").capitalize() + " minutes")


def calculate_minutes(birthdate, today):
    return (today - birthdate).days * 1440


if __name__ == "__main__":
    main()
