##Blackjack
import random
from art import logo
from replit import clear

keep_playing = "y"
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []



def give_user_card():
    card = random.randint(0, 12)
    user_cards.append(deck[card])
    return


def give_cpu_card():
    card = random.randint(0, 12)
    computer_cards.append(deck[card])
    return


def calculate_total(list_cards):
    total = 0
    for cards in list_cards:
        total = total + cards
    return total


def print_status():
    print(f"Your cards: {user_cards}, current score = {calculate_total(user_cards)} \n")
    print(f"Computer first card: {computer_cards[0]} \n")


def print_final():
    print(f"Your cards: {user_cards}, final score = {calculate_total(user_cards)} \n")
    print(f"Computer first card: {computer_cards[0]} \n")
    print(f"Computer's final hand: {computer_cards}, final score = {calculate_total(computer_cards)} \n")


def show_winner():
    if calculate_total(user_cards) <= 21:
        if calculate_total(computer_cards) > 21:
            print("Opponent went over you win")
        elif calculate_total(user_cards) > calculate_total(computer_cards):
            print("You win!")
        elif calculate_total(user_cards) == calculate_total(computer_cards):
            print("It's a draw!")
        else:
            print("You lose!!!")
    else:
        print("You went over. You lose!")


def welcome_game():
    print(logo)
    give_user_card()
    give_user_card()
    give_cpu_card()
    give_cpu_card()
    print_status()


welcome_game()
keep_playing = input("Would you like another card? y or n: ")

while keep_playing == "y":
    clear()
    print(logo)
    give_user_card()
    print_status()
    if calculate_total(user_cards) > 21:
        break
    if calculate_total(computer_cards) < 17:
        give_cpu_card()
    elif calculate_total(computer_cards) > 21 or calculate_total(user_cards) > 21:
        break
    keep_playing = input("Would you like another card? y or n: ")

print_final()
show_winner()
