import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if not match:
        return False
    return all(
        0 <= int(octet) <= 255 and (len(octet) == 1 or octet[0] != "0")
        for octet in match.groups()
    )


if __name__ == "__main__":
    main()
