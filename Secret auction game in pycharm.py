print( '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to secret auction.")


def secret_bidding():
    dic = {}
    while True:
        name = input("What is your name? ")
        bid = int(input("What's your bid? $"))
        q = input("Are there any bidders? Type 'yes' or 'no'.\n")
        dic[name] = bid
        if q.lower() == "yes":
            continue
        else:
            break

    winner_bidder_name = ""
    highest_bid = 0
    for names in dic:
        auction_amount = dic[names]
        if auction_amount > highest_bid:
            highest_bid = auction_amount
            winner_bidder_name = names
    print(f"The winner is {winner_bidder_name} with a bid of ${highest_bid}.")


secret_bidding()









