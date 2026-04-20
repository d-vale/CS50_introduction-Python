import re
import sys


def main():
    url = parse(input("HTML: "))
    if url:
        print(url)


def parse(s):
    match = re.search(r'<iframe[^>]+src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()
