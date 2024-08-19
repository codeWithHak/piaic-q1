# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

set_pass = input("set your password: ")
my_pass = len(set_pass)


if my_pass < 6:
    strength = "Weak"

elif my_pass < 11:
    strength = "Medium"

elif my_pass > 10:
    strength = "Strong"

print("Password Strength:",strength)    