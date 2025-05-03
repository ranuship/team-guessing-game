import random

wins = 0
games_played = 0

while True:
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100")

    try:
        guess = int(input())
    except ValueError:
        print("That's not a valid number! Try again.")
        continue

    games_played += 1

    if guess == number:
        print("You win!")
        wins += 1
    else:
        print(f"Wrong! The number was {number}")

    print(f"Score: {wins} wins out of {games_played} games")

    print("Play again? (y/n)")
    if input().lower() != 'y':
        break
