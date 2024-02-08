'''This program takes a number as input and doubles it'''

keep_asking = True
while keep_asking == True 
    #Take number input as a float and then print double the number
    try:
        num = float(input())
        keep_asking = False
    except ValueError:
        print("Please enter a number")

print(num*2)
