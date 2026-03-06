def main():
    grocery = {}
    while True:
        try:
            item = input().strip().upper()
            # Increment count for existing item, or initialize to 1
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except EOFError:
            break

    # Print items sorted alphabetically with their count
    for item in sorted(grocery):
        print(f"{grocery[item]} {item}")


main()
