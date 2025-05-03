import random
import time

start_time = time.time()  # Start the timer

number = random.randint(1, 10)
print("Guess a number between 1 and 10")
guess = int(input())

if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")

if guess == number:
    print("You win!")
else:
    print(f"Wrong! The number was {number}")

end_time = time.time()
print(f"Time taken: {end_time - start_time:.2f} seconds")
