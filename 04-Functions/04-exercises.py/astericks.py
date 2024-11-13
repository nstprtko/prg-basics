def f(n):
    if n == 1 :
        return '*'
    elif n >= 2 :
        return ("*/" * n)
    
print(f(5))