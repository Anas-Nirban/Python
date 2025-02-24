import random
from art import logo
def deal_card():
    """Returns and random card from the deck of card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user, dealer):
    if user == dealer:
        print("DRAW")
    elif dealer == 0:
        print("You lost")
    elif user == 0:
        print("You win!!!")
    elif user>21:
        print("You lost")
    elif dealer>21:
        print("You won")
    else:
        print("You lose")

def playGame():

    print(logo)
    user_cards = []
    dealer_cards = []
    is_gameOver = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_gameOver:
        user = calculate_score(user_cards)
        dealer = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards} and current score: {user}")
        print(f"Dealer's cards:{dealer_cards[0]}")

        if user == 0 or dealer == 0 or user > 21:
            is_gameOver = True
        else:
            users_deal = input("Type 'y' to continue or 'n' to stop the game: ")
            if users_deal == "y":
                user_cards.append(deal_card())
            else:
                is_gameOver = True

    while dealer !=0 and dealer <17:
        dealer_cards.append(deal_card())
        dealer = calculate_score(dealer_cards)

    print(f"Your final hand is {user_cards} and your score is {user}")
    print(f"Dealer's final hand is {dealer_cards} and dealer's score is {dealer}")
    compare(user, dealer)

    while input("Do you want to play blackjack again?? ") == "y":
        print("\n"  * 20)
        playGame()
playGame()