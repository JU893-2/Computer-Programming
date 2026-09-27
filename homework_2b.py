# Um, Jongwon
# Computer Programming, period 7
# Assignment 2b
# 9/27/2026

# alien color #1 
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")
# b
alien_color = 'yellow'
if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")

# alien colors #2
alien_color = 'green'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")
alien_color = 'yellow'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")
alien_color = 'red'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

# Stages of Life 3
following_ages = [1, 3, 10, 13, 19, 20, 21, 65]
for age in following_ages:
    if age < 2:
        print(f"Age {age}: The person is a baby.")
    elif age < 4:
        print(f"Age {age}: The person is a toddler.")
    elif age < 13:
        print(f"Age {age}: The person is a kid.")
    elif age < 20:
        print(f"Age {age}: The person is a teenager.")
    elif age < 65:
        print(f"Age {age}: The person is an adult.")
    else:
        print(f"Age {age}: The person is an elder.")

# 4 Hello Admin
usernames = ['jaden', 'sarah', 'admin', 'alex', 'chris']

if len(usernames) == 0:
    print("We need to find some users!")
else:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")

# 5 Checking Usernames
current_users = ['john', 'sarah', 'admin', 'alex', 'chris']
new_users = ['eric', 'SARAH', 'JOHN', 'peter', 'megan']
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' has already been used. You will need to enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")

# 6 Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")   