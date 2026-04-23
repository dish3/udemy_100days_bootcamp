# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

def find_highest_bidder(bids):
    winner = ""
    highest_bid = 0

    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"{winner} is the highest bidder with ${highest_bid}")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    should_continue = input("Are there other bidders? Type 'y' or 'n': ")

    if should_continue == "n":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "y":
        print("\n" * 20)


