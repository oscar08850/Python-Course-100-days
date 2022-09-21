import random



cpu = random.randint(0,2)

player = int(input("Choose? type 0 for rock, 1 for Paper, or 2 for scissors: "))


while (True):

    cpu = random.randint(0, 2)

    player = int(input("Choose? type 0 for rock, 1 for Paper, or 2 for scissors: "))

    if cpu == player:
        print("Draw")
    elif cpu == 0 and player == 2:
        print("PIERDES: piedra gana a tijera")
    elif cpu == 1 and player == 0:
        print("PIERDES: Papel gana a piedra:")
    elif cpu == 2 and player == 1:
        print("PIERDES Tijera gana a Papel")

    elif cpu == 0 and player == 1:
        print("GANAS: piedra pierde contra papel")
    elif cpu == 1 and player == 2:
        print("PIERDES: Papel pierde contra tijera")
    elif cpu == 2 and player == 0:
        print("GANAS Tijera pierde contra roca")

