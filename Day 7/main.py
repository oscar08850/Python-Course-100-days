import random

word_list = ["ardvark", "baboon", "camel"]

choosenWord = random.choice(word_list)
print(f"the word is {choosenWord}")

cadena = []
for letra in range(len(choosenWord)):
    cadena.append("_")

print(cadena)
lives = 6

end_of_game = False

while not end_of_game:
    char = input("Choose a letter: ").lower()
    i = 0
    for position in range(len(choosenWord)):
        letra = choosenWord[position]
        if char == letra:
            cadena[i] = letra
        i += 1
    print(f"las vidas son {lives}")

    if char not in choosenWord:
        lives -= 1

    if "_" not in cadena:
        end_of_game = True
        print("You Win!!!")

    elif lives == 0:
        end_of_game = True
        print("You Lose :( ")
    print(cadena)
    print()
