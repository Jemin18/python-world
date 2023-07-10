import random
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

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

url = "https://starngage.com/plus/en-us/influencer/ranking"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table')
followers_data = pd.DataFrame(columns=["Name", "Country", "Description", "Followers"])

for row in table.tbody.find_all("tr"):
    col = row.find_all("td")
    if col:
        name = col[1].text.strip()
        name = re.sub(r'\n|\s*@.*', '', name)
        followers = col[2].text.strip()
        country = col[4].text.strip()
        description = col[5].text.strip()
        description = re.sub(r'\n|\s*@.*', '', description)
        topics = [topic.text for topic in col[5].find_all("a")]
        description = ",".join(topics)
        followers_data = followers_data._append({"Name": name, "Country": country, "Description": description, "Followers": followers}, ignore_index=True)


def check_answer(guess, a_person_followers, b_person_followers):
    if guess == "A":
        return a_person_followers > b_person_followers
    else:
        return b_person_followers > a_person_followers


def parse_followers(follower_count):
    count = float(follower_count[:-1])
    unit = follower_count[-1]
    if unit == "K":
        count *= 1000
    elif unit == "M":
        count *= 1000000
    return int(count)


def game():
    score = 0
    while True:
        random_row_1 = followers_data.sample(n=1).iloc[0]
        random_name_1 = random_row_1['Name']
        random_country_1 = random_row_1['Country']
        random_description_1 = random_row_1['Description']
        random_followers_1 = random_row_1['Followers']

        random_row_2 = followers_data.sample(n=1).iloc[0]
        random_name_2 = random_row_2['Name']
        random_country_2 = random_row_2['Country']
        random_description_2 = random_row_2['Description']
        random_followers_2 = random_row_2['Followers']

        if random_name_1 == random_name_2 or not random_country_1.strip() or not random_country_2.strip():
            continue

        print(f"Compare A: {random_name_1}, Description: [{random_description_1}], from {random_country_1}.")
        vs = """
         _    __
        | |  / /____
        | | / / ___/
        | |/ (__  )
        |___/____(_)
        """
        print(vs)
        print(f"Against B: {random_name_2}, Description: [{random_description_2}], from {random_country_2}.")

        no_of_followers_1 = parse_followers(random_followers_1)
        no_of_followers_2 = parse_followers(random_followers_2)
        # print(no_of_followers_1)
        # print(no_of_followers_2)

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








