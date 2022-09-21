import random

from data import data
from art import logo,vs

score = 0
gameover = False

def seleccionRandom(data):
    d = random.choices(data)
    return d

def eleccion(opcion1, opcion2, puntuacion):
    selecion = input("Elige A o B: ")
    if opcion1[0]["follower_count"] > opcion2[0]["follower_count"]:
        if selecion == "A":
            puntuacion = puntuacion + 1
            return puntuacion

def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"Compare A: {account_name} a {account_desc}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"



print(logo)
account_a = random.choices(data)[0]
account_b = random.choices(data)[0]
while account_a['name'] == account_b['name']:
    data2 = seleccionRandom(data)
print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

guess = input("Who has more followers? A or B: ").lower()

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

is_correct = check_answer(guess, a_follower_count, b_follower_count)

if is_correct:
    score += 1
    print(f"You are right: score: {score}")
else:
    print(f"You are wrong!: final score {score}")

# while(gameover == False):




