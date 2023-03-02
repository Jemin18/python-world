import random
logo ="""

██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""
print(logo)
print("Welcome to Number Guessing Game.")
print("I am thinking of a number between 1 and 100.")
correct_answer = random.choice(range(1,101))
difficulty_level = input("Choose a difficulty. Type 'e' for easy or 'h' for hard or 'v' for very hard: " )
attempts = 10

if difficulty_level.lower() == "e":
    def game():
        global attempts
        while True:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))

            if guess_number > correct_answer:
                print("Too high")

            elif guess_number < correct_answer:
                print("Too low")

            elif guess_number == correct_answer:
                print(f"Nice!!! You got it. The answer was {correct_answer}")
                break

            attempts -= 1
            if attempts == 0:
                print("Sorry you have no more attempts remaining. You lose")
                break
            print("Guess again.")

    game()

elif difficulty_level.lower() == "h":
    def game():
        global attempts
        attempts -= 5
        while True:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))

            if guess_number > correct_answer:
                print("Too high")

            elif guess_number < correct_answer:
                print("Too low")

            elif guess_number == correct_answer:
                print(f"Nice!!! You got it. The answer was {correct_answer}")
                print("You are a good guesser.")
                break

            attempts -= 1
            if attempts == 0:
                print("Sorry you have no more attempts remaining. You lose")
                break
            print("Guess again.")

    game()

elif difficulty_level.lower() == "v":
    def game():
        global attempts
        attempts -= 7
        while True:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))

            if guess_number > correct_answer:
                print("Too high")

            elif guess_number < correct_answer:
                print("Too low")

            elif guess_number == correct_answer:
                print(f"Nice!!! You got it. The answer was {correct_answer}")
                print("You are a very good guesser!")
                break

            attempts -= 1
            if attempts == 0:
                print("Sorry you have no more attempts remaining. You lose")
                break
            print("Guess again.")

    game()


