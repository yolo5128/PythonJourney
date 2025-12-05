import random
import time

options = ["rock", "paper", "scissors"]

user_wins = 0
computer_wins = 0
rounds = 0

print("--------------------------------------")
print("Welcome to Rock, Paper, Scissors!")
print("--------------------------------------")
print()
time.sleep(0.95)

while True:
    print(f"Round {rounds}!")
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors"):
        print(f"You win this round, {user_choice} beats {computer_choice}")
        user_wins += 1
        rounds = rounds + 1
    elif (user_choice == "paper" and computer_choice == "rock"):
        print(f"You win this round, {user_choice} beats {computer_choice}")
        user_wins += 1
        rounds = rounds + 1
    elif (user_choice == "scissors" and computer_choice == "paper"):
        print(f"You win this round, {user_choice} beats {computer_choice}")
        user_wins += 1
        rounds = rounds + 1
    elif rounds == 3:
        print("Game over!")
        print(f"Final score - You: {user_wins}, Computer: {computer_wins}")
        break
    else:
        print(f"Computer wins this round, {computer_choice} beats {user_choice}")
        computer_wins += 1
        rounds = rounds + 1