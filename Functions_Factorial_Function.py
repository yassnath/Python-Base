def my_factorial(n): # function signature
 # function body
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print(my_factorial(5))