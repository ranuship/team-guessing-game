import random

while True:
    number = random.randint(1, 100)  # Member 2: Changed range to 1–100
    print("Guess a number between 1 and 100")
    guess = int(input())

    if guess == number:
        print("You win!")
    else:
        print(f"Wrong! The number was {number}")

    # Member 3: Replay feature
    print("Play again? (y/n)")
    if input().lower() != 'y':
        break
