# Um, Jongwon
# Computer Programming, Period 4
# Assignment: Homework 4a
# 10/26/2026

# Part A
# a.
people={
    "first_name": "Joe",
    "last_name":"Canyon",
    "age":"17",
    "city":"LA"
}
print(people["first_name"])
print(people["last_name"])
print(people["age"])
print(people["city"])

# b
fav_food = ["pizza", "mac n cheese", "bacon", "baguette"]
hobbies = ["sleeping", "running", "gaming", "eating"]

aboutMe = {
    "name": "Jongwon",
    "age": "16",
    "favFood": fav_food,
    "hairColor": "black",
    "favSubject": "english",
    "favSweet": "gummy bears",
    "favHobbies": hobbies,
    "likeCoding": True
}
print(aboutMe)

# c
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

phonebook["Jake"] = 938273443
del phonebook["Jill"]
print(phonebook)

# Part B
# 1
glossary = {
    "monarch": "a king or queen",
    "pope": "head of the church",
    "temple": "a place of worship",
    "justification": "the process of receiving the gift of salvation in christ jesus",
    "treaty": "an agreement"
}

print("monarch:", glossary["monarch"], "\n")
print("pope:", glossary["pope"], "\n")
print("temple:", glossary["temple"], "\n")
print("justification:", glossary["justification"], "\n")
print("treaty:", glossary["treaty"], "\n")

#2
glossary = {
    "monarch": "a king or queen",
    "pope": "head of the church",
    "temple": "a place of worship",
    "justification": "the process of receiving the gift of salvation in christ jesus",
    "treaty": "an agreement",
    "gospel": "good news",
    "covenant": "a promise",
    "faith": "belief in god",
    "prayer": "talking to god",
    "sin": "acts against god"
}

for k, v in glossary.items():
    print(k, ":", v, "\n")

#3
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states"
}
for k, v in rivers.items():
    print("the", k, "runs through", v)
for k in rivers.keys():
    print(k)
for v in rivers.values():
    print(v)

#4
person1 = {
    "first_name": "bob",
    "last_name": "smith",
    "fav_color": "blue",
    "birth_month": "may"
}

person2 = {
    "first_name": "john",
    "last_name": "ryan",
    "fav_color": "red",
    "birth_month": "june"
}

person3 = {
    "first_name": "danny",
    "last_name": "jones",
    "fav_color": "green",
    "birth_month": "july"
}

people = [person1, person2, person3]
for person in people:
    for k, v in person.items():
        print(k, ":", v)
    print("\n")

#5
cities = {
    "paris": {
        "country": "france",
        "population": "2 million",
        "fact": "has eiffel tower"
    },
    "los angeles": {
        "country": "united states",
        "population": "4 million",
        "fact": "located in california"
    },
    "rome": {
        "country": "italy",
        "population": "3 million",
        "fact": "has colosseum"
    }
}
for city, info in cities.items():
    print("city:", city)
    for k, v in info.items():
        print(k, ":", v)
    print("\n")