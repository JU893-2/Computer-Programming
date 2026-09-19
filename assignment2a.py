# Um, Jongwon
# Computer Programming, period 4
# Assignment: Homework 3
# September 19 2026

hobbies = ["running", "gaming", "eating", "sleeping", "watching TV"]
print (hobbies)
print(len(hobbies))
print(hobbies [2])
print(hobbies [0])

listz = ("hello!" *100)
print (listz)

list1=["pumpkin", "halloween", "jack-o-lantern", "spooky"]
list2=["christmas", "new year", "holiday", "santa"]
list3=[list1+list2]
print (list3)

favFoods=["steak", "potato chips", "mac-n-cheese", "peaches", "pasta"]
print (favFoods)
print(len(hobbies))
print(favFoods[2])
print(favFoods[-4])
favFoods.append("Jongwon")
favFoods.insert(2,16)
favFoods.remove("peaches")
print(favFoods)

for number in range(1,21):
    print(number)

odd_numbers=list(range(1,21,2))

for number in odd_numbers:
    print(number)

animals=["dog", "cat", "fox"]
for animal in animals:
    print(f"A {animal} would be great to take a photo of.")

print("All of these animals have fur on them!")

guests = ["Albert Einstein", "Barack Obama", "Nikola Tesla"]
for guest in guests:
    print(f"Dear {guest}, I invite you to a dinner with me.")

not_attending = "Barack Obama"
print(f"\n{not_attending} cannot make it to the dinner.")
guests[1]= "Isaac Newton"

print("\nUpdated List")
for guest in guests:
    print(f"{guest}, you are invited to my dinner.")





