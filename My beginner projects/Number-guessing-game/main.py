import random
import time

random_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

chosen_number = random.choice(random_number)
guess = 0

print("--------------------------------------")
print("Welcome to the Number Guessing Game!")
print("--------------------------------------")
print()
time.sleep(.95)
print("I'm thinking of a number between 1 and 10.")
print()

while guess != chosen_number:
    guess = input("Guess a number between 1 and 10: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    if guess < chosen_number:
        print(f"{guess} is too low. Try again!")
    elif guess > chosen_number:
        print(f"{guess} is too high. Try again!")
    else:
        print(f"Congratulations! {guess} is correct. You guessed the number!")
