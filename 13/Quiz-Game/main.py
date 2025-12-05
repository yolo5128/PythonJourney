#python quiz game

questions = ("How many elements are in the periodic table?: ", 
             "How many continents are there on Earth?: ",
             "How many colors are in a rainbow?: ", 
             "How many planets are in our solar system?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
            ("A. 3", "B. 5", "C. 6", "D. 7"),
            ("A. 4", "B. 3", "C. 7", "D. 6"),
            ("A. 8", "B. 6", "C. 10", "D. 15"))

answers = ("C", "D", "C", "A")
guesses = []
score = 0

question_number = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_number]:
        print(option)


    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[question_number]} is the correct answer.")
    question_number += 1

print("-------------------------")
print("          RESULTS        ")
print("-------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

