from replit import clear

seguimos = "yes"
apuestas = {}
max_key = ""

max_bid = 0

def reset():
    clear()
    logo = "Hola soy un logo"
    print(logo)

def addBid(nombre,bid):
    apuestas[nombre] = bid



while seguimos == "yes":
    reset()
    nombre = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    addBid(nombre, bid)
    seguimos = input("are there any other bidders? yes or or no. ")
    reset()


for key in apuestas:
    if apuestas[key] > max_bid:
        max_key = key
        max_bid = apuestas[key]

print(f"The winner is {max_key} with a bid of ${max_bid}")
