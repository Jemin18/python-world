import random
from game_data import data
# The data for this game is imported from the list of dictionaries of game_data.py file which is uploaded in this repository.
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
print(logo)


def check_answer(guess, a_person_followers, b_person_followers):
    if a_person_followers > b_person_followers:
        return guess == "A"
    else:
        return guess == "B"


def game():
    score = 0
    while True:
        first_person = random.choice(data)
        second_person = random.choice(data)
        if first_person == second_person:
            second_person = random.choice(data)
        print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}.")
        vs = """
         _    __
        | |  / /____
        | | / / ___/
        | |/ (__  )
        |___/____(_)
        """
        print(vs)
        print(f"Against B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}.")

        no_of_followers_1 = first_person["follower_count"]
        no_of_followers_2 = second_person["follower_count"]

        q = input("What is your choice? Type 'A' or 'B': ").upper()

        is_correct = check_answer(q, no_of_followers_1, no_of_followers_2)
        if is_correct:
            score += 1
            print(f"Your score: {score}")
            continue
        else:
            print("Oops, that's incorrect. Game over.")
            print(f"Your final score : {score}")
            break


game()

while True:
    play_again = input("Do you want to play the game again. Type 'y' for yes or 'n' for no: ")
    if play_again.lower() == "y":
        game()
    elif play_again.lower() == "n":
        print("Thanks for playing.")
        break








