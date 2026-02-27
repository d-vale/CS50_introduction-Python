def main():
    run_machine()


def get_coin():
    coin = int(input("Insert a coin: "))
    if coin in [5, 10, 25]:
        return coin
    return 0  # Invalid coin: no deduction


def run_machine():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        amount_due -= get_coin()  # Deduct the coin value from the amount due
    print(f"Change Owed: {abs(amount_due)}")  # abs = absolute value to handle negative change


main()
