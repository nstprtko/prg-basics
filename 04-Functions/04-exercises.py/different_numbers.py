def f(n1, n2, n3) :# ask for three arguments
    if n1<0 or n2<0 or n3<0:# check if at least one number is negative
        return True # if so, return true
    else:
        return False# otherwise return false 

print(f(1,-5,3))