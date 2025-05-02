import random

while True:
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100")

    try:
        guess = int(input())
    except ValueError:
        print("That's not a valid number! Try again.")
        continue

    if guess == number:
        print("You win!")
    else:
        print(f"Wrong! The number was {number}")

    print("Play again? (y/n)")
    if input().lower() != 'y':
        break