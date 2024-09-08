# Problem: Compute the factorial of a number using a while loop.



def factorial(n):
    result = 1
    i = 2
    while i<=n:
        result *= i
        i+=1
    return(result)



print(factorial(5))











































"""factorial = 5
number = 1

while number <5:
    factorial *= number
    number +=1          

print(factorial)
#5    """