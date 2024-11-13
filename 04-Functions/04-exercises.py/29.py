def factorial(n):

# 0! = 1, 1! = 1
    if n==0 or n==1:
        result = 1
 

# n! = n * (n-1)!
    elif n > 1:
        result= (n * factorial(n-1))

    
    return result

print(factorial(5))