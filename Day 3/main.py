# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


nombreMinusculas1 = name1.lower()
nombreMinusculas2 = name2.lower()


T = nombreMinusculas1.count("t") + nombreMinusculas2.count("t")
R = nombreMinusculas1.count("r") + nombreMinusculas2.count("r")
U = nombreMinusculas1.count("u") + nombreMinusculas2.count("u")
E = nombreMinusculas1.count("e") + nombreMinusculas2.count("e")

L = nombreMinusculas1.count("l") + nombreMinusculas2.count("l")
O = nombreMinusculas1.count("o") + nombreMinusculas2.count("o")
V = nombreMinusculas1.count("v") + nombreMinusculas2.count("v")

firstDigit = T + R + U + E
secondDigit = L + O + V + E

finalScore = int(str(firstDigit)+str(secondDigit))

if finalScore < 10 or finalScore > 90:
    print(f"Your score is {finalScore}, you go together like coke and mentos.")

elif finalScore >= 40 and finalScore <= 50:
    print(f"your score is {finalScore}, you are alright together.")
else:
    print(f"Your score is {finalScore}.")

