# Simple Number Guessing Game
import random

print("🎯 Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 10")

# Computer picks a random number
secret_number = random.randint(1, 10)
guess = None
attempts = 0
# Game loop
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("📈 Too low! Try again.")
    elif guess > secret_number:
        print("📉 Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {secret_number}")

print("Thanks for playing! 👍")