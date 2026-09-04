#Jongwon Um
#Assignment 1c

#Part 1
name_of_object = input("Enter the name of the object: ")
mass_kg = input("what is the mass of the object in kg?")
velocity = input("what is the velocity of the object in m/s")

name_of_object_clean = name_of_object.strip().title()
mass_kg_num = float(mass_kg)
velocity_num = float(velocity)

KE_joules = 0.5*mass_kg_num*(velocity_num**2)

KE_calories = KE_joules/4.184

KE_ergs = KE_joules * 10**7

#print("Kinetic Energy Report for: ", name_of_object_clean)
output_line_one = f"Kinetic Energy Report for: {name_of_object_clean}"
print(output_line_one)
print("-------------------------------")
output_line_three = f"Joules:\t{KE_joules} J"
#print("Joules:\t", KE_Joules, "J")
print(output_line_three)
output_line_three = f"Calories:"

