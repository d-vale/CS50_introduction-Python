import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(
        r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s
    )
    if not match:
        raise ValueError
    h1, m1, period1, h2, m2, period2 = match.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError
    if not (0 <= m1 <= 59 and 0 <= m2 <= 59):
        raise ValueError
    h1 = to_24h(h1, m1, period1)
    h2 = to_24h(h2, m2, period2)
    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def to_24h(hour, minutes, period):
    if period == "AM":
        return 0 if hour == 12 else hour
    else:
        return 12 if hour == 12 else hour + 12


if __name__ == "__main__":
    main()
