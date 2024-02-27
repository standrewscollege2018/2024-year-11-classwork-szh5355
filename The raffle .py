print("Welcome to the raffle program.")
prize = input("What is the prize being raffled?")
value = input("What is the value of the prize (do not enter $ sign)")

name = input("Enter name of entrant: ")
if name == 'end':
    keep_going = False
else:
    keep_going = True
