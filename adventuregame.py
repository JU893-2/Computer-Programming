# You need to have at least 30 if statements
# no direction cna lead the user hanging without instructions 
first_driection = input("Would you like to turn right or left")
if first_driection=="left":
    print("\nAs you enter inside the left door, a shrouding mist surrounds your every move as you try to navigate through")
    print("You see three silhouettes, maybe they can help you later on? Pick one. ")
    x=input(("Pick which to grab: \na A knife shaped silhouette\nb A sword shaped silhouette"))
    if x == "a":
        if x == "b":
            print("jf")
        else:
            print("frie")

if first_driection=="right":
    print("\nAs you enter inside the right door, you come face to face to what seems to be a dragon?")
    print("The dragon seems friendly, what do you do?")
    y=input(("Do you... \na Befriend the dragon\nb Try and kill the dragon"))
    if y == "a":      
        if y == "b":
            print("You die")
        else:
            print("Wow")


             
