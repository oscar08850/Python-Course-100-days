
from turtle import Turtle, Screen
from prettytable import PrettyTable

table = PrettyTable()
print(table)
print()

table.add_column("Pokemon name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type",["Electric", "Fire", "Water"])

table.add_row(["Hello", "pepe"])

print(table.align)

print (table)