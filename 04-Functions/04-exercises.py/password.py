def f(password):
    password_str = str(password)
    #password_str = password_str.lower()
    
    if len(password_str) < 6 :
        return False
    for char in password_str :
        if password_str.count(char) > 1:
            return False
        else:
            return True

    
print(f('f2water3'))