def check(a):
    try:
        a = int(a)
        return True
    except ValueError:
        return False

get_age = True
while get_age:
    age=input("Age:")
    if check(age):
        get_age = False
    else:
        print("Oops")



get_weight = True
while get_weight:
    weight=input("Weight:")
    if check(weight):
        get_weight = False
    else:
        print("Oops")



if age >= 16 and weight >= 50:
    print ("You are eligible")
else:
    print ("You are not eligible")


    
