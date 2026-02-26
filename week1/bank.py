def main():
    str = input("Greeting: ")
    print(greetingCheck(str))

def greetingCheck(str):
    str = str.lower().strip()
    if str == "hello" or str.split(",")[0] == "hello":
        return "$0"
    elif str[0] == "h":
        return "$20"
    else:
        return "$100"

main()
