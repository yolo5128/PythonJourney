import random
import time

dice = [1, 2, 3, 4, 5, 6]

dice_chosen = random.choice(dice)
player_score = 0
bot_score = 0
rounds = 1

print("--------------------------")
print("Welcome to the Dice game!")
print("--------------------------")
time.sleep(2)



while True:
    print(f"Round {rounds}!")
    player = input("Enter a number to roll 1-6: ")

    try:
        player = int(player)
    except ValueError:
        print("Invalid input, enter only integers please.")
        continue

    if player not in dice:
        print("Invalid choice. Please try again.")
        continue

    if rounds == 5 and player_score > bot_score:
        print("------------------------------------------")
        print(f"Congratulations You've Won!")
        print(f"     Here's the results    ")
        print(f"Your score: {player_score} | bot score: {bot_score}")
        print("------------------------------------------")
        break
    elif rounds == 5 and bot_score > player_score:
        print("------------------------------------------")
        print(f"Womp Womp Womp! You've Lost")
        print(f"     Here's the results    ")
        print(f"Your score: {player_score} | bot score: {bot_score}")
        print("------------------------------------------")
        break
    elif rounds == 5 and player_score == bot_score:
        print("------------------------------------------")
        print(f"Close call, It was a tie!")
        print(f"     Here's the results    ")
        print(f"Your score: {player_score} | bot score: {bot_score}")
        print("------------------------------------------")
        break


    if player < dice_chosen:
        print(f"you rolled {player} bot rolled {dice_chosen}")
        print(f"bot wins round {rounds}")
        bot_score = bot_score + 1
        rounds = rounds + 1
    elif player > dice_chosen:
        print(f"you rolled {player} bot rolled {dice_chosen}")
        print(f"you have won round {rounds}")
        player_score = player_score + 1
        rounds = rounds + 1
    elif player == dice_chosen:
        print(f"You and the bot have both rolled a {dice_chosen}")
        bot_score = bot_score + 1
        player_score = player_score + 1
        rounds = rounds + 1