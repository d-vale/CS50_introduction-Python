months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        try:
            date = input("Date: ").strip()
            year, month, day = parse_date(date)
            print(f"{year:04}-{month:02}-{day:02}")
            break
        except ValueError:
            pass


def parse_date(date):
    # Parse a date string in M/D/YYYY or Month D, YYYY format.
    # Returns (year, month, day) as integers, or raises ValueError if invalid.

    # Try numeric format: M/D/YYYY
    if "/" in date:
        parts = date.split("/")
        if len(parts) != 3:
            raise ValueError
        month, day, year = int(parts[0]), int(parts[1]), int(parts[2])

    # Try textual format: Month D, YYYY
    elif "," in date:
        parts = date.split(" ")
        if len(parts) != 3:
            raise ValueError
        month_name = parts[0]
        day = int(parts[1].rstrip(","))
        year = int(parts[2])
        if month_name not in months:
            raise ValueError
        month = months.index(month_name) + 1

    else:
        raise ValueError

    # Validate ranges
    if not (1 <= month <= 12 and 1 <= day <= 31):
        raise ValueError

    return year, month, day


main()

# This one was hard :)
