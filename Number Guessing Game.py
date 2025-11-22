import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Computer picks a random number
number = random.randint(1, 100)
attempts = 0

while True:
    # Take user input
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Check the guess
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it right in {attempts} tries!")
        break
