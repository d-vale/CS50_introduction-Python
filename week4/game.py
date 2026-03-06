import random


def main():
    n = get_level()
    number = random.randint(1, n)

    # Keep prompting until the user guesses correctly
    while True:
        guess = get_guess()
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_level():
    # Ask for a positive integer level; reprompt on invalid input
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            pass


def get_guess():
    # Ask for a positive integer guess; reprompt on invalid input
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass


main()
