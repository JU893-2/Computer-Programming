#  Menu and individual price variables
menu = ["Breakfast Burrito", "Cheeseburger", "Hot Dog", "Teriyaki Bowl", "Chips", "Fries", "Soda", "Water"]
burrito_price = 4.50
cheeseburger_price = 4.00
hotdog_price = 3.00
teriyaki_price = 5.00
chips_price = 1.00
fries_price = 2.50
soda_price = 1.75
water_price = 1.50

#  Welcome and display menu
print("Welcome to Z's Point of Sale System")
for item in menu:
    print(item)

# Get a combination order: Food, Side, and Drink
print("\n--- Build Your Combination ---")
food_choice = input("Choose a main food item: ")
side_choice = input("Choose a side item: ")
drink_choice = input("Choose a drink item: ")
qty = int(input("Enter quantity for the combo: "))

# Calculate Food Price
if food_choice == "Breakfast Burrito":
    food_price = burrito_price
elif food_choice == "Cheeseburger":
    food_price = cheeseburger_price
elif food_choice == "Hot Dog":
    food_price = hotdog_price
elif food_choice == "Teriyaki Bowl":
    food_price = teriyaki_price
else:
    food_price = 0

# Calculate Side Price (Taxed at 10%)
if side_choice == "Chips":
    side_price = chips_price * 1.10
elif side_choice == "Fries":
    side_price = fries_price * 1.10
else:
    side_price = 0

# Calculate Drink Price (Taxed at 10%)
if drink_choice == "Soda":
    drink_price = soda_price * 1.10
elif drink_choice == "Water":
    drink_price = water_price * 1.10
else:
    drink_price = 0

# Total calculation for the combo
base_amount = (food_price + (chips_price if side_choice == "Chips" else fries_price if side_choice == "Fries" else 0) + (soda_price if drink_choice == "Soda" else water_price if drink_choice == "Water" else 0)) * qty
total_amount = (food_price * qty) + (side_price * qty) + (drink_price * qty)

# Order 
print("\nItem\t\t\tQuantity\tBase Amount\tTotal Amount")
print("---\t\t\t--------\t-----------\t------------")
print(food_choice, "\t\t", qty, "\t\t", food_price * qty, "\t\t", food_price * qty)
print(side_choice, "\t\t\t", qty, "\t\t", side_price * qty / 1.10, "\t\t", side_price * qty)
print(drink_choice, "\t\t\t", qty, "\t\t", drink_price * qty / 1.10, "\t\t", drink_price * qty)
print("TOTAL\t\t\t", qty, "\t\t", base_amount / 1.10 if total_amount != base_amount else base_amount, "\t\t", total_amount)

# Cash or Cub Cash
payment = input("\nEnter payment type (Cash or Cub Cash): ")

if payment == "Cash":
    cash_given = int(input("Enter cash amount: "))
    change = cash_given - total_amount
    print("Change returned: $", change)
    print("Thank you!")
else:
    balance = 100
    remaining = balance - total_amount
    print("Thank you for using Cub Cash!")
    print("Remaining card balance: $", remaining)