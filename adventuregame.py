# You need to have at least 30 if statements
# No direction can leave the user hanging without instructions 

first_driection = input("Would you like to turn right or left? ")

if first_driection == "left":
    print("\nAs you enter inside the left door, a shrouding mist surrounds your every move as you try to navigate through.")
    print("You see two silhouettes, maybe they can help you later on? Pick one.")
    x = input("Pick which to grab: \n1 A knife shaped silhouette\n2 A sword shaped silhouette\n")

    if x == "1":
        print("\nYou picked up a knife, two times the size of your body length, it has a flaming end at the end of its slit.")
        print("You follow along a dirt path, hoping to find anything that satisfies your interests.")
        print("\nAt the end of the path you see a woman at the left and a man at the right, which one do you choose. Choose wisely.")
        y = input("\n1 Man\n2 Woman\n")

        if y == "1":
            print("\nYou encounter a man with a similar shadow as you, maybe it's you in a different future.")
            print("The man whips out a flaming knife, the same as yours but seems much stronger.")
            print("He lunges at you. You try and fight back but fail to do so. As the man pierces your flaming heart, he whispers to you...")
            print("Should've picked the other way")
            print("You have died")

        elif y == "2":
            print("\nYou encounter a woman with a similar figure as you, maybe it's your past friend in a different future.")
            print("The woman suddenly charges at you with an icy sword like dagger.")
            z = input("What do you do?\n1 Fight back and charge\n2 Try and reason with the woman\n")

            if z == "1":
                print("\nThe woman slices at your throat but you dodge and immobilize her legs.")
                print("Once she is immobilized her body turns into flames.")
                print("You have defeated the enemy.")
            elif z == "2":
                print("\nThe woman does not like your tone, she slices you into bits.")
                print("You have died.")
            else:
                print("\nYou hesitated for too long! She strikes before you can decide.")
                print("You have died.")
        else:
            print("\nYou stood indecisive in the mist and vanished into the fog.")
            print("You have died.")

    elif x == "2":
        print("\nYou picked up a sword, half the size of your body length, I guess you can consider it a dagger, you feel a cold presence at the end of its slit.")
        print("Once you pick up the sword, one man appears on the right and one on the left.")
        print("Pick who to follow.")
        z = input("\n1 Man on the Right\n2 Man on the Left\n")

        if z == "1":
            print("\nThe man seems to be a wizard who seeks your aid, he also has a bunch of gold in his pouch.")
            a = input("\nDo you:\n1 Help the wizard\n2 Rob the wizard\n")

            if a == "1":
                print("\nThe wizard asks you to help save his town overrun by ogres. You follow along.")
                print("As you reach the town you see 5 ogres ahead of your path.")
                b = input("Do you:\n1 Ask the wizard to cast a fireball\n2 Depend on your sword skills\n")

                if b == "1":
                    print("\nThe wizard casts a fireball but seems to have no effect.")
                    print("Having noticed your presence the 5 ogres jump both you and the wizard.")
                    print("You have died.")
                elif b == "2":
                    print("\nYou rush into the town slicing all 5 of the ogres' legs.")
                    print("Having taken them by surprise, their bodies start to freeze up and shatter.")
                    print("You have saved the town!")
                else:
                    print("\nThe ogres spot you while you hesitate and attack.")
                    print("You have died.")

            elif a == "2":
                print("\nYou threaten the wizard and successfully rob him.")
                print("With no consequences whatsoever, you happily buy a drink at the local store.")
                print("Nothing much to do in this world.")
                print("Game over. Are you proud of your actions?")
            else:
                print("\nThe wizard gets suspicious of your hesitation and teleports away.")
                print("You are lost forever.")

        elif z == "2":
            print("\nThe man on the left turns out to be a shadowy assassin!")
            c = input("\nDo you:\n1 Draw your sword and fight\n2 Run back into the mist\n")

            if c == "1":
                print("\nYour cold dagger glows bright and parries his deadly blade.")
                print("You strike him down and escape safely!")
                print("You survived!")
            elif c == "2":
                print("\nYou turn around to run, but he throws a throwing knife right into your back.")
                print("You have died.")
            else:
                print("\nYou froze in fear and the assassin takes you down instantly.")
                print("You have died.")
        else:
            print("\nYou didn't choose either man. The mist consumes you.")
            print("You have died.")

    else:
        print("\nYou didn't grab a weapon! Unarmed, you are easy prey for the creatures in the mist.")
        print("You have died.")

elif first_driection == "right":
    print("\nAs you enter inside the right door, you come face to face to what seems to be a dragon?")
    print("The dragon seems friendly, what do you do?")
    y = input("Do you:\n1 Befriend the dragon\n2 Try and kill the dragon\n")

    if y == "1":
        print("\nThe dragon lowers its wing, inviting you to ride.")
        fly_destination = input("Where do you want to fly?\n1 To the Gold Kingdom\n2 Into the Storm\n")

        if fly_destination == "1":
            print("\nYou fly to a mountain of gold and live like a king!")
            print("You win!")
        elif fly_destination == "2":
            print("\nLightning strikes mid-flight.")
            print("You have died.")
        else:
            print("\nThe dragon drops you for giving unclear instructions.")
            print("You have died.")

    elif y == "2":
        print("\nYou find a nearby weapon and charge!")
        attack_location = input("Where do you strike?\n1 The head\n2 The tail\n")

        if attack_location == "1":
            print("\nThe dragon breathes fire before you reach it.")
            print("You have died.")
        elif attack_location == "2":
            print("\nThe dragon whips you away with force.")
            print("You have died.")
        else:
            print("\nYou hesitate and get swallowed whole.")
            print("You have died.")

    else:
        print("\nThe dragon gets confused by your actions and blows you away.")
        print("You have died.")

else:
    print("\nYou stood outside the doors for too long and the floor collapses!")
    print("You have died.")