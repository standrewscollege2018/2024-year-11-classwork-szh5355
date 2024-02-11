def check(a):
    try:
        a = int(a)
        return True
    except ValueError:
        return False

AGE_MIN = 16
WEIGHHT_MIN = 50

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


if int(age) >= AGE_MIN and int(weight) >= WEIGHT_MIN:
    
