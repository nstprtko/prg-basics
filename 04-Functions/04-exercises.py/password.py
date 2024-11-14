def f(password):
    password_str = str(password)# convert inputted to string
    #password_str = password_str.lower()
    
    if len(password_str) < 6 : # check the length of the password
        return False
    for char in password_str : # for every character in converted input
        if password_str.count(char) > 1: # variable.count(char/digits)
            return False
        else:
            return True

    
print(f('A2water3'))