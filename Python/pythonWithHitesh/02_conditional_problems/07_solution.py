# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

coffee_size  = "large".lower()
extra_shot = False

if extra_shot:
    coffee = f"{coffee_size} coffee with an extra shot of espresso"

else: 
    coffee = f"{coffee_size} coffee"

print("Order:",coffee)
"""coffe_order = input("what would you like to have: ")
extra_sugar = input("how much sugar: ")

print(f"Order: {coffe_order}, Sugar: {extra_sugar}")"""