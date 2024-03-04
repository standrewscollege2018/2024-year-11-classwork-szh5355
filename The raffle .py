
import random
print("Welcome to the raffle program.")
prize = input("What is the prize being raffled?")
value = input("What is the value of the prize (do not enter $ sign)")

names = []
keep_asking = True
while keep_asking ==True:
    name = input("Enter name of entrant:")
    if name == "End":
        keep_asking = False
    else:
        names.append(name)

number_of_entrants = len(names)
winner = random.randint(0,number_of_entrants-1)
print(names[winner])
