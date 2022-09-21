
# Tip Calculator

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
percentage = percentage/100

people = int(input("How many people to split the bill? "))

plusBill = bill * percentage
totalBill = plusBill + bill

totalPerPerson= round(totalBill/people , 2)
print(f"each person should pay: ${totalPerPerson}")