# Problem: Check if a number is prime.

number = int(input("give me a number I'll tel if it's prime or not: "))
is_prime = True
for i in range(2,number):
    if number % i == 0 :
        is_prime = False

print(is_prime)        