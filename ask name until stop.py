# Set up list 
names = []

get_name = True
while get_name:
    # get name
    name = input()
    # If user enters stop then end the loop
    if name.lower() == "stop":
        get_name = False
    elif name.strip("") == "":
        print("No blanks allowed")
    else:
        names.append(name)
