import random

number = random.randint(1, 100)

guess = int(input("Guess a number: "))

while guess != number:
    if guess < number:
        print("Higher")
    else:
        print("Lower")

    guess = int(input("Guess again: "))

print("Correct! You guessed the number.")

# Sample Output:
# Guess a number: 40
# Higher
# Guess again: 70
# Lower
# Guess again: 60
# Correct! You guessed the number.
