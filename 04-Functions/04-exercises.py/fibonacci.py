def f(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    # return 0 and 1 respectively for 0 and 1st element
    a = 0
    b = 1
    # create two variables 0 and 1
    for _ in range(2, n + 1) : # idk why this line, but for nth element in range from 2 
        next_fib = a + b # creare next fib number
        a = b # update variable for +1
        b = next_fib # update variable for counted up

    return b

print(f(9))
