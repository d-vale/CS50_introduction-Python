def main():
    print(convertEmojy(input()))


def convertEmojy(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()
