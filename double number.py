'''This program takes a number as input and doubles it'''

#Start a loop for error catching
keep_asking = True
while keep_asking:
    #Take number input as a float and then print double the number
    try:
        num = float(input("Enter a positive number:"))
        if num >= 0:
            keep_asking = False
        else:
            print("Enter a positive number:")
            
    except ValueError:
        print("Please enter a number")

print(f"{num} doubled is {num * 2}")
