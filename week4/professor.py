import random


def main():
    # Prompt the user for a difficulty level
    level = get_level()
    score = 0

    # Generate and ask 10 addition problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y
        attempts = 0

        # Allow up to 3 attempts per problem
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                # Input is not a valid integer
                print("EEE")
                attempts += 1
                continue

            if answer == correct:
                # Correct answer: increment score and move on
                score += 1
                break
            else:
                # Wrong answer: display EEE and retry
                print("EEE")
                attempts += 1

        # After 3 failed attempts, reveal the correct answer
        if attempts == 3:
            print(f"{x} + {y} = {correct}")

    # Display the final score out of 10
    print(f"Score: {score}")


def get_level():
    # Keep prompting until the user enters 1, 2, or 3
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass  # Non-integer input, try again


def generate_integer(level):
    # Generate a random non-negative integer with the appropriate number of digits
    if level == 1:
        return random.randint(0, 9)      # 1 digit
    elif level == 2:
        return random.randint(10, 99)    # 2 digits
    elif level == 3:
        return random.randint(100, 999)  # 3 digits
    else:
        raise ValueError("Level must be 1, 2, or 3")


if __name__ == "__main__":
    main()
