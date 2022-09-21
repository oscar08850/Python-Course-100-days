

#Calculator

#Add
def add(n1, n2):
    """Devuelve el resultado de n1 + n2"""
    return n1 + n2

##Substract
def substract(n1, n2):
    """Devuelve el resultado de n1 - n2"""
    return n1 - n2

#Multiply
def multiply(n1, n2):
    """Devuelve el resultado de n1 * n2"""
    return n1 * n2

#Divide
def divide(n1, n2):
    """Devuelve el resultado de n1 / n2"""
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

num2 = int(input("What's the second number?: "))

operation_symbol = input("Pick an operation from the line above: ")

answer = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

acabar = "y"
while(acabar == "y"):
    acabar = input("seguir? y or n: ")
    operation_symbol = input("Pick an operation: ")
    num3 = int(input("Dame otro numero: "))
    answer = operations[operation_symbol](answer, num3)
    print(f"{answer} {operation_symbol} {num3} = {answer}")


