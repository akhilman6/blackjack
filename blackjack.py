from art import logo
import random


def deal_cards():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(usr_score, cmptr_score):
    if usr_score > 21 and cmptr_score > 21:
        return "You went over. You lose 😤"
    if usr_score == cmptr_score:
        return "Draw 🙃"
    elif cmptr_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif usr_score == 0:
        return "Win with a Blackjack 😎"
    elif usr_score > 21:
        return "You went over. You lose 😭"
    elif cmptr_score > 21:
        return "Opponent went over. You win 😁"
    elif usr_score > cmptr_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():

    print(logo)

    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_cards())
        computer_card.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"    Users cards: {user_card}, score: {user_score}")
        print(f"    Computer's first card: {computer_card[0]}")

        if user_score == 0 or user_score > 21 or computer_score == 0:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to draw a card? y or n: ")
            if user_should_deal == "y":
                user_card.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_cards())
        computer_score = calculate_score(computer_card)

    print(f"    User's cards: {user_card}, score: {user_score}")
    print(f"    Computer's cards: {computer_card}, score: {computer_score}")
    print(compare(user_score, computer_score))


play_game()
while input("Do you want to play again? y on n: ") == "y":
    play_game()
