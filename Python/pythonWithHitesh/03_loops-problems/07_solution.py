# Problem: Keep asking the user for input until they enter a number between 1 and 10.


while True:
    inp = int(input("Give me a number between 1 and 10: "))
    if inp > 0 and inp < 11:
        break
















































"""while True:
    number = int(input("Give me number between 1 to 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again!")
        """