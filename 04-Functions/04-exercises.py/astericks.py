def f(n):# ask for one argument
    if n == 1 : # if the argument is 1 return only one asteriks 
        return '*'
    elif n >= 2 : # if the argument is more than 2
        return ("*/" * n)# return the said string n(argument) amount of times
    
print(f(5))